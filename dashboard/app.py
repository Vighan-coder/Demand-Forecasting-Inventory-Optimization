import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Demand Forecasting & Inventory Optimization",
    layout="wide"
)

st.sidebar.title("Dashboard")

st.sidebar.write(
    "Demand forecasting and inventory optimization "
    "for retail stores."
)

st.sidebar.divider()

st.sidebar.subheader("Project")

st.sidebar.write(
    "Model: Random Forest"
)

st.sidebar.write(
    "Forecasting MAE: 761.19"
)

st.sidebar.write(
    "MAE Improvement: 39.13%"
)

st.title("Demand Forecasting & Inventory Optimization")
st.write(
    "Retail demand forecasting and inventory decision-support dashboard"
)

# Load project outputs
forecast_results = pd.read_csv("data/forecast_results.csv")
inventory_policy = pd.read_csv("data/final_inventory_policy.csv")
model_comparison = pd.read_csv("data/model_comparison.csv")
feature_importance = pd.read_csv("data/feature_importance.csv")
project_summary = pd.read_csv("data/project_summary.csv")

st.divider()

st.subheader("Project Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Training Rows",
    "941,389"
)

col2.metric(
    "Validation Rows",
    "68,015"
)

col3.metric(
    "Forecasting MAE",
    "761.19"
)

col4.metric(
    "MAE Improvement",
    "39.13%"
)

st.divider()

st.subheader("Actual vs Predicted Sales")

chart_data = forecast_results.head(100).copy()

chart_data["Date"] = pd.to_datetime(chart_data["Date"])

chart_data = chart_data.set_index("Date")

st.line_chart(
    chart_data[["Actual_Sales", "Predicted_Sales"]]
)

st.divider()

st.subheader("Inventory Optimization")

top_reorder = (
    inventory_policy
    .sort_values("Reorder_Point", ascending=False)
    .head(10)
    .copy()
)

top_reorder = top_reorder.set_index("Store")

st.bar_chart(
    top_reorder["Reorder_Point"]
)

st.divider()

st.subheader("Model Performance")

performance_data = model_comparison.set_index("Model")

st.bar_chart(
    performance_data[["MAE", "RMSE"]]
)

st.divider()

st.subheader("Forecasting Feature Importance")

importance_data = (
    feature_importance
    .sort_values("Importance", ascending=False)
    .set_index("Feature")
)

st.bar_chart(
    importance_data["Importance"]
)

st.divider()

st.subheader("Store-Level Forecast")

selected_store = st.selectbox(
    "Select a Store",
    sorted(forecast_results["Store"].unique())
)

store_data = forecast_results[
    forecast_results["Store"] == selected_store
].copy()

store_data["Date"] = pd.to_datetime(store_data["Date"])
store_data = store_data.set_index("Date")

st.line_chart(
    store_data[["Actual_Sales", "Predicted_Sales"]]
)

st.divider()

st.subheader("Store Inventory Policy")

selected_inventory = inventory_policy[
    inventory_policy["Store"] == selected_store
].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Daily Demand",
    f"{selected_inventory['Average_Daily_Demand']:,.0f}"
)

col2.metric(
    "Safety Stock",
    f"{selected_inventory['Safety_Stock']:,.0f}"
)

col3.metric(
    "Reorder Point",
    f"{selected_inventory['Reorder_Point']:,.0f}"
)