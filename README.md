# 🏡 EstimaAI — Smart Property Price Prediction

> A modern Machine Learning web application that predicts property prices using a trained Scikit-Learn model and a Flask backend.

---

## 📖 Table of Contents

- About the Project
- Features
- Tech Stack
- Project Structure
- Getting Started
- Machine Learning Pipeline
- API Endpoint
- Future Improvements
- Contributing
- Author
- License

---

# 📌 About the Project

**EstimaAI** is an end-to-end Machine Learning web application that estimates property prices based on user inputs such as area, bedrooms, bathrooms, location, and property age.

The project combines a trained **Random Forest Regression model** with a **Flask backend** and a modern **Glassmorphism-based frontend** to provide instant, real-time property price predictions without reloading the page.

---

# ✨ Features

- 🤖 Machine Learning price prediction using Random Forest Regressor
- ⚡ Real-time AJAX predictions (no page refresh)
- 🎨 Responsive Glassmorphism user interface
- 📱 Mobile-friendly design
- 📊 Displays estimated valuation range
- 💰 Formats prices into Lakhs and Crores
- 📈 Shows confidence score for predictions
- 🔄 Interactive sliders for user input

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Python, Flask |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Frontend | HTML5, Tailwind CSS, JavaScript |
| Model Serialization | Pickle |

---

# 📁 Project Structure

```text
property-price-prediction/
│
├── data/
│   └── House Price Prediction Dataset.csv
│
├── model/
│   └── property_model.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Prerequisites

- Python 3.8 or above
- Git (Optional)

---

## 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/property-price-prediction.git
```

or navigate into the project folder

```bash
cd property-price-prediction
```

---

## 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Train the Model

```bash
python train_model.py
```

This script:

- Loads the dataset
- Preprocesses the data
- Trains the Random Forest model
- Saves the trained pipeline to:

```
model/property_model.pkl
```

---

## 6️⃣ Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# ⚙️ Machine Learning Pipeline

The application follows an end-to-end Machine Learning workflow.

### Step 1 — Data Preprocessing

Using **ColumnTransformer**

Numeric Features

- Area
- Bedrooms
- Bathrooms
- Property Age

↓

Standardized using

```
StandardScaler
```

Categorical Feature

- Location

↓

Encoded using

```
OneHotEncoder(handle_unknown="ignore")
```

---

### Step 2 — Model Training

The processed data is trained using

```
RandomForestRegressor
```

which learns the relationship between property features and market prices.

---

### Step 3 — Pipeline Serialization

The complete preprocessing pipeline and trained model are saved together as

```
model/property_model.pkl
```

This prevents feature mismatch during prediction.

---

### Step 4 — Prediction

When the user submits the form:

```
User Input
      ↓
AJAX Request
      ↓
Flask API
      ↓
ML Pipeline
      ↓
Predicted Price
      ↓
Formatted Result
```

The prediction is returned instantly without refreshing the page.

---

# 🔌 API Endpoint

## POST `/predict`

### Request

```json
{
  "area": 1500,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "Downtown",
  "age": 4
}
```

---

### Response

```json
{
  "success": true,
  "prediction": 6250000.0,
  "formatted_price": "₹62.50 Lakh",
  "raw_formatted": "₹6,250,000.00",
  "range": "₹59.38 Lakh - ₹65.63 Lakh",
  "confidence": "94.8%"
}
```

---

# 📈 Future Improvements

Some planned improvements include:

- User Authentication
- Database Integration
- More ML Algorithms
- Property Image Upload
- Location Map Integration
- Model Explainability (SHAP)
- Deployment on AWS/Render

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👨‍💻 Author

**Keshav Kumar**

- GitHub: https://github.com/keshavkumar07
- LinkedIn: https://www.linkedin.com/in/keshav-k-1401642a9/

---

# 📄 License

This project is open-source and available under the **MIT License**.
