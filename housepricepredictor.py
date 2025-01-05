import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('housing.csv')

#converted string to boolean values so it can be split in train and test data in array as all other values are numerical
data['mainroad'] = data['mainroad'].map({'yes': 1, 'no': 0})
data['basement'] = data['basement'].map({'yes': 1, 'no': 0})
data['prefarea'] = data['prefarea'].map({'yes': 1, 'no': 0})

# Feature selection
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'mainroad', 'basement', 'prefarea']]
Y = data['price']

# Split the dataset into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=41)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict the prices
Y_pred = model.predict(X_test)

# Calculate Mean Squared Error and R-squared score
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# # Print performance metrics
print(f"Mean squared error: {mse}")
print(f"R-squared score: {r2}")

# Collect house details for prediction
print("Enter details of the house")
try:
    area = float(input("Enter the area of the house (in sq.feet): "))
    bedrooms = int(input("Enter the number of bedrooms: "))
    bathrooms = int(input("Enter the number of bathrooms: "))
    stories = int(input("Enter the number of stories: "))
    parking = int(input("Enter the number of parking spaces: "))

    # Ensure the boolean inputs are correctly handled and debug their values
    mainroad_input = input("Is the house on main road (yes/no): ").strip().lower()
    basement_input = input("Does the house have a basement (yes/no): ").strip().lower()
    prefarea_input = input("Is the house in our preferred area (yes/no): ").strip().lower()

    # Convert inputs to boolean values (True/False)
    mainroad = True if mainroad_input == 'yes' else False
    basement = True if basement_input == 'yes' else False
    prefarea = True if prefarea_input == 'yes' else False

    # Prepare the input features for prediction (make sure they're in correct format)
    factors = [[area, bedrooms, bathrooms, stories, parking, mainroad, basement, prefarea]]

    # Make the prediction
    prediction = model.predict(factors)

    print(f"\nPredicted price for the given house details: {prediction[0]:,.2f}")
except ValueError as e:
    print(f"\nInvalid input: {e}")
except Exception as e:
    print(f"\nAn error occurred: {e}")
