# House-price-predictor using Linear Regression 

This Python program predicts the price of a house based on various features such as area, number of bedrooms, bathrooms, stories, parking, and whether it is located on the main road, has a basement, or is in a preferred area. It uses a linear regression model to make the prediction based on a dataset containing these features.
The accuracy of the code is 60% 

Requirements
Python 3.x
Pandas
Scikit-learn

Dataset
The program requires a CSV file housing.csv, which should contain the following columns:
area: Area of the house in square feet
bedrooms: Number of bedrooms
bathrooms: Number of bathrooms
stories: Number of stories in the house
parking: Number of parking spaces
mainroad: Whether the house is located on the main road (yes/no)
basement: Whether the house has a basement (yes/no)
prefarea: Whether the house is in a preferred area (yes/no)
price: Price of the house (target variable)

How to Use
Place the housing.csv file in the same directory as this script.
Run the script.
Input the house details when prompted to get a price prediction.

Example Output
Mean squared error: 1.234567
R-squared score: 0.876543
Enter details of the house
Enter the area of the house (in sq.feet): 1500
Enter the number of bedrooms: 3
Enter the number of bathrooms: 2
Enter the number of stories: 2
Enter the number of parking spaces: 1
Is the house on main road (yes/no): yes
Does the house have a basement (yes/no): no
Is the house in your preferred area (yes/no): yes
Predicted price for the given house details: 250,000.00



