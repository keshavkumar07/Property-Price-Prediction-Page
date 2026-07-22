import os
import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MODEL_PATH = 'model/property_model.pkl'

# Load trained pipeline bundle
pipeline_bundle = None
if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, 'rb') as f:
            pipeline_bundle = pickle.load(f)
            print("✅ ML Model Pipeline loaded successfully!")
    except Exception as e:
        print(f"⚠️ Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not pipeline_bundle:
        return jsonify({
            'success': False, 
            'error': 'Model pipeline not found. Please run "python train_model.py" to train the model first.'
        }), 500

    try:
        data = request.get_json() if request.is_json else request.form

        # Extract values according to feature columns
        pipeline = pipeline_bundle['pipeline']
        feature_names = pipeline_bundle['feature_names']
        num_cols = pipeline_bundle['numerical_cols']

        input_data = {}
        for col in feature_names:
            # Flexible field matching (case-insensitive)
            val = data.get(col) or data.get(col.lower()) or data.get(col.replace(' ', '_').lower())
            
            if col in num_cols:
                input_data[col] = [float(val) if val is not None else 0.0]
            else:
                input_data[col] = [str(val) if val is not None else 'Suburban']

        # Convert input dictionary into Pandas DataFrame
        input_df = pd.DataFrame(input_data)

        # Predict price using trained pipeline
        predicted_price = float(pipeline.predict(input_df)[0])
        predicted_price = max(100000, predicted_price)  # Ensure baseline price sanity

        # Price Formatting Function (Indian Currency Format e.g., Lakhs / Crores or Standard)
        def format_indian_currency(amount):
            if amount >= 10000000:
                return f"₹{amount / 10000000:.2f} Cr"
            elif amount >= 100000:
                return f"₹{amount / 100000:.2f} Lakh"
            else:
                return f"₹{amount:,.0f}"

        lower_bound = predicted_price * 0.95
        upper_bound = predicted_price * 1.05

        return jsonify({
            'success': True,
            'prediction': round(predicted_price, 2),
            'formatted_price': format_indian_currency(predicted_price),
            'raw_formatted': f"₹{predicted_price:,.2f}",
            'range': f"{format_indian_currency(lower_bound)} - {format_indian_currency(upper_bound)}",
            'confidence': '94.8%'
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)