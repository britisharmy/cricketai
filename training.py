import mysql.connector
import threading
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Function to fetch data from MySQL
def fetch_data(thread_id):
    conn = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM cricket_data"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    # Process the data (you may need to adjust this part based on your dataset)
    df = pd.DataFrame(data, columns=['feature1', 'feature2', 'label'])
    X = df[['feature1', 'feature2']]
    y = df['label']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Hyperparameter tuning using GridSearchCV
    param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20, 30]}
    model = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)
    model.fit(X_train, y_train)

    # Save the trained model
    model_filename = f'model_thread_{thread_id}.joblib'
    joblib.dump(model, model_filename)

    # Make predictions and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Thread {thread_id}: Accuracy = {accuracy}")

# Number of threads
num_threads = 4

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=fetch_data, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Merge models and create an ensemble (optional)
models = []
for i in range(num_threads):
    model_filename = f'model_thread_{i}.joblib'
    model = joblib.load(model_filename)
    models.append(model)

# Generate predictions using the ensemble of models
# X_test_new is your new data for prediction
X_test_new = pd.DataFrame({'feature1': [value1], 'feature2': [value2]})
predictions = []
for model in models:
    prediction = model.predict(X_test_new)
    predictions.append(prediction)

# You can aggregate predictions from multiple models (e.g., take a majority vote)

# Now you can use 'predictions' for further analysis or applications.
