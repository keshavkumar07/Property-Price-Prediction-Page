import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error

def train_and_save_model():
    csv_path = 'data/House Price Prediction Dataset.csv'
    
    if not os.path.exists(csv_path):
        print(f"Error: Could not find dataset at '{csv_path}'. Please check your file path.")
        return

    # 1. Load Dataset
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()  # Clean column spaces

    # Identify target column (e.g., 'Price', 'price', 'House_Price')
    target_candidates = [col for col in df.columns if 'price' in col.lower()]
    if not target_candidates:
        raise ValueError("Could not find a 'Price' column in your dataset.")
    target_col = target_candidates[0]

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Categorize feature types
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

    print(f"Features Detected - Numerical: {numerical_cols}, Categorical: {categorical_cols}")

    # 2. Build Preprocessor & Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
        ]
    )

    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42))
    ])

    # 3. Train Test Split & Fitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_pipeline.fit(X_train, y_train)

    # 4. Evaluation
    y_pred = model_pipeline.predict(X_test)
    accuracy = r2_score(y_test, y_pred) * 100
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("--------------------------------------------------")
    print(f"✅ Model Trained Successfully!")
    print(f"📊 Accuracy (R² Score): {accuracy:.2f}%")
    print(f"📉 Root Mean Squared Error: {rmse:,.2f}")
    print("--------------------------------------------------")

    # 5. Save Pipeline Bundle
    os.makedirs('model', exist_ok=True)
    with open('model/property_model.pkl', 'wb') as f:
        pickle.dump({
            'pipeline': model_pipeline,
            'feature_names': list(X.columns),
            'numerical_cols': numerical_cols,
            'categorical_cols': categorical_cols
        }, f)

    print("💾 Pipeline saved to 'model/property_model.pkl'")

if __name__ == '__main__':
    train_and_save_model()