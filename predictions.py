import pandas as pd
import joblib

# Define your new data for prediction
new_data = pd.DataFrame({'feature1': [new_value1], 'feature2': [new_value2]})

# Load the previously trained models
models = []
for i in range(4):  # Assuming you had 4 threads and 4 models
    model_filename = f'model_thread_{i}.joblib'
    model = joblib.load(model_filename)
    models.append(model)

# Generate predictions using the ensemble of models
predictions = []
for model in models:
    prediction = model.predict(new_data)
    predictions.append(prediction)

# You can aggregate predictions from multiple models (e.g., take a majority vote)
# For binary classification, you can use the mode function
final_prediction = pd.Series(predictions).mode()[0]

print("Final Prediction:", final_prediction)
