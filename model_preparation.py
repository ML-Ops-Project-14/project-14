import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

df = pd.read_csv('dataset.csv')
print(df)

# Splitting the dataset
X = df.drop("wind_speed", axis=1)
Y = df['wind_speed']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Model training
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
print(y_pred)

# Model evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification report\n", classification_report(y_test, y_pred))

#Saving the model
pickle_filename = "weather_predict_model.pkl"
with open(pickle_filename, 'wb') as file:
    pickle.dump(lr, file)
print(f"✅ Model saved to {pickle_filename}")


