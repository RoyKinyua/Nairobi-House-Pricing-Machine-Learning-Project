# Nairobi-House-Pricing-Machine-Learning-Project
A machine learning project that predicts property prices in Nairobi using real estate listing data, feature engineering, and regression models.

   _Project Overview_

Nairobi’s real estate market varies significantly across neighborhoods, property sizes, and amenities.

This project builds a data-driven pricing system that:

Collects and structures Nairobi property listings

Cleans and engineers predictive features

Trains machine learning models

Evaluates model performance



   _Objectives_

Understand price behavior across Nairobi neighborhoods

Identify key price drivers

Build a baseline Linear Regression model

Improve performance using Random Forest
| Column        | Description                       |
| ------------- | --------------------------------- |
| location      | Nairobi neighborhood              |
| property_type | Apartment / House / Maisonette    |
| bedrooms      | Number of bedrooms                |
| bathrooms     | Number of bathrooms               |
| size_sqft     | Property size (square feet)       |
| amenities     | Comma-separated amenities         |
| price_kes     | Listing price in Kenyan Shillings |
| listing_date  | Date listed                       |



  _Data Cleaning & Feature Engineering_

Key preprocessing steps:

Removed duplicate listings

Handled missing values

Standardized location names

Converted size units to sqft

Removed extreme outliers

   _Engineered Features_

price_per_sqft

amenity_score

month



   _Exploratory Data Analysis_

Key insights:

Karen, Runda, and Lavington are among the most expensive areas.

Property size strongly correlates with price.

More amenities increase property value.



   _Modeling_

Baseline Model: Linear Regression

MAE: 4066916.1396219344
RMSE: 6203656.491063047
R2: 0.2249746495877959

Comparrison Model:

Random Forest MAE: 4639232.1873
Random Forest RMSE: 6608925.4834372355
Random Forest R2: 0.12040625085698009

