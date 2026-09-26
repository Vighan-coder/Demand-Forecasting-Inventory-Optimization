# Demand Forecasting & Inventory Optimization

An end-to-end machine learning project that forecasts retail store demand and converts forecast uncertainty into practical inventory decisions such as safety stock and reorder points.

## Project Overview

Retail stores need to maintain enough inventory to satisfy customer demand while avoiding unnecessary overstock.

This project builds a data-driven pipeline:

**Historical Sales → Demand Forecasting → Forecast Error Analysis → Safety Stock → Reorder Point**

The project uses the Rossmann Store Sales dataset and develops a Random Forest forecasting model with historical demand features.

## Dashboard

An interactive Streamlit dashboard was built to explore:

- Actual vs predicted sales
- Model performance
- Feature importance
- Store-level forecasts
- Safety stock and reorder points

## Objectives

- Explore historical retail sales data
- Identify important demand patterns
- Engineer time-based and historical demand features
- Build a baseline Random Forest model
- Improve forecasting using lag and rolling features
- Evaluate forecasting performance using MAE and RMSE
- Estimate forecast uncertainty
- Calculate store-level safety stock
- Calculate reorder points for inventory replenishment

## Dataset

The project uses the Rossmann Store Sales dataset.

Main data sources:

- `train.csv` — historical store sales
- `test.csv` — future observations
- `store.csv` — store-level characteristics

Important variables include:

- Store
- Date
- Sales
- Customers
- DayOfWeek
- Promo
- StateHoliday
- SchoolHoliday
- StoreType
- Assortment
- CompetitionDistance
- Promo2

## Project Structure

```text
Demand-Forecasting-Inventory-Optimization/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── store.csv
│   ├── feature_importance.csv
│   ├── model_comparison.csv
│   ├── forecast_results.csv
│   ├── inventory_policy.csv
│   ├── final_inventory_policy.csv
│   └── project_summary.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│
├── dashboard/
│
├── README.md
└── requirements.txt



Methodology
1. Exploratory Data Analysis

The dataset was inspected for:

Missing values
Sales distribution
Zero-sales observations
Weekly demand patterns
Promotional effects
Daily, weekly and monthly sales trends
Relationship between customers and sales
2. Feature Engineering

Time-based features were extracted from the date:

Year
Month
Day
Week of year
Weekend indicator

Categorical variables were converted using one-hot encoding.

Store-level features such as store type, assortment, competition distance and promotion information were incorporated.

3. Baseline Model

A Random Forest Regressor was trained using a chronological train/validation split.

The baseline model achieved:

Metric	Result
MAE	1250.55
RMSE	1891.15
4. Historical Demand Features

The forecasting model was improved using:

Previous-day sales
Previous-week sales
Seven-day rolling average sales

The rolling average was calculated using previous observations only to avoid using the current day's sales as an input.

5. Forecasting Model

A second Random Forest model was trained using the historical demand features.

Results:

Metric	Baseline	With Lag Features
MAE	1250.55	761.19
RMSE	1891.15	1447.47

The lag-feature model reduced validation MAE by approximately 39.13%.

Inventory Optimization

Forecasting is followed by an inventory decision layer.

Forecast Error

Forecast error was calculated as:

Actual Sales − Predicted Sales

The validation forecast errors were used to estimate demand uncertainty for each store.

Safety Stock

A simplified 95% service-level assumption was used:

Safety Stock = 1.645 × Forecast Error Standard Deviation

Reorder Point

A 1-day replenishment lead time was assumed:

Reorder Point = Average Daily Demand × Lead Time + Safety Stock

This produces a store-level inventory threshold for triggering replenishment.

Example Inventory Policy
Store	Avg Daily Demand	Safety Stock	Reorder Point
1	3958	1508	5466
2	4113	1343	5457
3	5720	2653	8373
4	7989	2433	10422
9	5364	2712	8076
Key Results
941,389 training observations
68,015 validation observations
Forecasting MAE: 761.19
Forecasting RMSE: 1,447.47
MAE improvement over baseline: 39.13%
Store-level safety stock calculated
Store-level reorder points calculated
Key Model Features

The forecasting model identified the following features as important:

Day of week
Seven-day rolling sales
Previous-day sales
Previous-week sales
Promotion
School holiday
Store
Limitations

This project is intended as a portfolio-level forecasting and inventory optimization system rather than a production inventory platform.

Current limitations include:

The forecasting model does not currently use the Open feature.
Closed-store days can therefore produce non-zero predictions.
A 1-day replenishment lead time is assumed.
Safety stock uses a simplified normal-error assumption.
Current inventory levels are not available.
Actual supplier lead-time variability is not available.
Product-level inventory is not modeled.

A production system would incorporate real inventory levels, product-level demand, supplier lead times, service-level requirements, ordering constraints and operational costs.

## Future Improvements

- Improve the handling of closed-store days using the `Open` feature
- Experiment with additional forecasting models
- Add product-level inventory forecasting
- Incorporate actual supplier lead times
- Add current inventory levels and reorder alerts
- Improve safety-stock estimation using lead-time variability
- Deploy the Streamlit dashboard publicly

Author

Vighan Raj Verma

B.Tech Computer Science & Engineering

GitHub: github.com/Vighan-coder

LinkedIn: linkedin.com/in/vighan-raj-verma-4992b2317
