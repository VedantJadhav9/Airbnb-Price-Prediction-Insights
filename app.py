import gradio as gr
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Prediction Function
def predict_price(
    accommodates,
    bathrooms,
    bedrooms,
    beds,
    reviews,
    rating
):

    # Prepare input data
    input_data = np.array([[
        accommodates,
        bathrooms,
        bedrooms,
        beds,
        reviews,
        rating
    ]])

    # Predict log price
    prediction = model.predict(input_data)

    # Convert to INR
    price = round(np.exp(prediction[0]) * 83, 2)

    # Property Category + Image
    if price < 4000:
        category = "🏠 Budget Stay"
        image = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"

    elif price < 9000:
        category = "🏢 Mid-Range Apartment"
        image = "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"

    else:
        category = "✨ Luxury Stay"
        image = "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688"

    # Final Result
    result = f"""
# 💰 Estimated Price

# ₹ {price} / night

---

## 🏷 Property Category
### {category}
"""

    return result, image


# DARK AIRBNB STYLE CSS
css = """

body {
    background: #121212;
}

.gradio-container {
    max-width: 1100px !important;
    margin: auto;
    font-family: Arial, sans-serif;
    color: white !important;
}

.result-box {
    background: #1e1e1e !important;
    color: white !important;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.5);
}

label {
    color: white !important;
    font-weight: bold;
}

textarea {
    color: white !important;
    background: #1e1e1e !important;
}

footer {
    visibility: hidden;
}

"""

# APP LAYOUT
with gr.Blocks(

    css=css,

    theme=gr.themes.Base(
        primary_hue="rose",
        neutral_hue="slate"
    )

) as app:

    # HEADER
    gr.Markdown(
        """
        <h1 style='
            text-align:center;
            font-size:48px;
            font-weight:900;
            color:#FF5A5F;
            margin-bottom:10px;
        '>
        🏠 Airbnb Smart Price Predictor
        </h1>

        <p style='
            text-align:center;
            font-size:20px;
            color:#d1d1d1;
            margin-bottom:30px;
        '>
        Predict Airbnb property prices instantly
        </p>
        """
    )

    # MAIN CONTENT
    with gr.Row():

        # LEFT COLUMN
        with gr.Column():

            accommodates = gr.Slider(
                1,
                16,
                value=4,
                step=1,
                label="👥 Number of Guests"
            )

            bathrooms = gr.Slider(
                1,
                8,
                value=1,
                step=1,
                label="🛁 Bathrooms"
            )

            bedrooms = gr.Slider(
                0,
                10,
                value=2,
                step=1,
                label="🛏 Bedrooms"
            )

            beds = gr.Slider(
                1,
                18,
                value=2,
                step=1,
                label="🛌 Beds"
            )

            reviews = gr.Slider(
                0,
                600,
                value=50,
                step=1,
                label="⭐ Number of Reviews"
            )

            rating = gr.Slider(
                20,
                100,
                value=95,
                step=1,
                label="🌟 Review Score"
            )

            predict_btn = gr.Button(
                "Predict Price",
                variant="primary"
            )

        # RIGHT COLUMN
        with gr.Column():

            output = gr.Markdown(
                """
                ## 🏡 Prediction Result

                Your estimated Airbnb price will appear here.
                """,
                elem_classes="result-box"
            )

            image = gr.Image(
                value="https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
                label="Recommended Property Style"
            )

    # BUTTON ACTION
    predict_btn.click(

        fn=predict_price,

        inputs=[
            accommodates,
            bathrooms,
            bedrooms,
            beds,
            reviews,
            rating
        ],

        outputs=[
            output,
            image
        ]
    )

# Launch App
app.launch()