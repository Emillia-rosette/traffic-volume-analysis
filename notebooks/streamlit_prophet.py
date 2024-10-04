# Streamlit Imports
import streamlit as st

# Standard Libraries
import pandas as pd
import numpy as np

# Plotting Libraries
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import month_plot

# Modeling Libraries
from prophet import Prophet
import xgboost as xgb

# Evaluation Metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

# Symmetric Mean Absolute Percentage Error (SMAPE)
def smape(y_true, y_pred):
    return 100 * np.mean(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred)))

# Streamlit Title and Description
st.title('Traffic Flow Time Series Forecasting and Regional Traffic Counts')
st.markdown("""
This application demonstrates time series forecasting using **Naive**, **Prophet**, and **XGBoost** models, along with **Seasonality** analysis and **Regional Traffic Counts** visualization. Use the sidebar to configure parameters and view results.
""")

# File paths for default datasets
traffic_counts_path = '/Users/emillianlandu/capstone-Emillia-rosette/data/uk_data/dft_traffic_counts_raw_counts.csv'
default_time_series_path = '/Users/emillianlandu/capstone-Emillia-rosette/data/monthly_data.csv'

# Load default dataset
def load_traffic_counts_data():
    return pd.read_csv(traffic_counts_path)

def load_default_time_series_data():
    return pd.read_csv(default_time_series_path)

# Sidebar Configuration
st.sidebar.title("Model and Data Configuration")

# Upload Time Series CSV file at the top of the sidebar
uploaded_file = st.sidebar.file_uploader("Upload your time series CSV file", type=["csv"])

# Load Regional Traffic Volume Data on app startup
region_data = load_traffic_counts_data()

# Filter by region in the sidebar
st.sidebar.write("### Filter by Region")
all_regions = region_data['region_name'].unique().tolist()
selected_region = st.sidebar.selectbox('Select a Region', ['All Regions'] + all_regions)

# Filter the dataset based on the selected region
if selected_region != 'All Regions':
    region_data = region_data[region_data['region_name'] == selected_region]

# Display Data Overview (for all regions or selected region)
st.write(f"## Data Overview ({selected_region})")
st.write(region_data.head())  # Show the first 5 rows in a table

# Group traffic data by region for the selected region
region_traffic_filtered = region_data.groupby('region_name')['all_motor_vehicles'].sum().reset_index()

# Plot the regional traffic volume
fig_region_filtered = px.bar(region_traffic_filtered, x='region_name', y='all_motor_vehicles', title=f"Regional Traffic Volumes ({selected_region})")
st.plotly_chart(fig_region_filtered)

# Load Time Series Data if not provided by the user
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = load_default_time_series_data()

# Ensure the data has the required columns for time series forecasting
if 'timestamp' in data.columns and 'all_motor_vehicles' in data.columns:
    # Data Preprocessing
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.rename(columns={'timestamp': 'ds', 'all_motor_vehicles': 'y'})

    # Train-Test Split based on the 'ds' column
    train_data = data[data['ds'] <= "2020-12-01"]
    test_data = data[data['ds'] > "2020-12-01"]

    # Sidebar for Seasonality Plot Selection (Checkbox)
    seasonality_plot = st.sidebar.checkbox("Show Seasonality Plot", value=True)

    if seasonality_plot:
        st.subheader("Seasonality Plot")

        # Aggregating the data monthly for seasonality analysis
        monthly_data = data.copy()
        monthly_data['month'] = monthly_data['ds'].dt.month
        monthly_data = monthly_data.set_index('ds').resample('M').sum()

        # Create the seasonal plot using `month_plot` from statsmodels
        fig, ax = plt.subplots(figsize=(12, 6))
        month_plot(monthly_data["y"], ax=ax)
        plt.title("Seasonal Motor Vehicles per Month")
        st.pyplot(fig)

    # Sidebar for Model Selection
    st.sidebar.write("### Model Selection")
    model_choice = st.sidebar.selectbox("Choose a Forecasting Model", ["None", "Naive", "Prophet", "XGBoost"])

    # Ensure that a new plot is created each time a new model is selected
    if model_choice == "Naive":
        # Naive Forecasting
        st.header("Naive Forecasting Model")
        test_data['naive_forecast'] = test_data['y'].shift(1)

        # Plot Naive Forecast vs Actual
        fig_naive = go.Figure()
        fig_naive.add_trace(go.Scatter(x=test_data['ds'], y=test_data['y'], mode='lines', name='Actual', line=dict(color='gray')))
        fig_naive.add_trace(go.Scatter(x=test_data['ds'], y=test_data['naive_forecast'], mode='lines', name='Naive Forecast', line=dict(color='blue', dash='dash')))
        fig_naive.update_layout(title='Naive Model Forecast vs Actual', xaxis_title='Date', yaxis_title='Traffic Volume')
        st.plotly_chart(fig_naive)

        # Metrics
        y_true_naive = test_data['y'][1:]
        y_pred_naive = test_data['naive_forecast'][1:]
        mae_naive = mean_absolute_error(y_true_naive, y_pred_naive)
        rmse_naive = math.sqrt(mean_squared_error(y_true_naive, y_pred_naive))
        smape_naive = smape(y_true_naive, y_pred_naive)
        st.write(f"**Symmetric Mean Absolute Percentage Error (SMAPE)**: {smape_naive:.2f}%")

    elif model_choice == "Prophet":
        # Prophet Forecasting
        st.header("Prophet Forecasting Model")
        
        # Initialize and fit Prophet model
        prophet_model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        prophet_model.add_country_holidays(country_name='UK')
        prophet_model.fit(train_data)
        
        # Create a DataFrame for future predictions
        future = prophet_model.make_future_dataframe(periods=len(test_data), freq='MS')
        forecast = prophet_model.predict(future)
        
        # Plot Prophet Forecast
        fig_prophet = make_subplots(rows=1, cols=1)
        fig_prophet.add_trace(go.Scatter(x=test_data['ds'], y=test_data['y'], mode='lines', name='Actual'))
        fig_prophet.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
        st.plotly_chart(fig_prophet)
        
        # Metrics
        y_true_prophet = test_data['y'].values
        y_pred_prophet = forecast['yhat'].values[-len(test_data):]
        mae_prophet = mean_absolute_error(y_true_prophet, y_pred_prophet)
        rmse_prophet = math.sqrt(mean_squared_error(y_true_prophet, y_pred_prophet))
        smape_prophet = smape(y_true_prophet, y_pred_prophet)
        st.write(f"**Symmetric Mean Absolute Percentage Error (SMAPE)**: {smape_prophet:.2f}%")

    elif model_choice == "XGBoost":
        # XGBoost Forecasting
        st.header("XGBoost Forecasting Model")
        
        # Create lagged features for XGBoost
        for lag in range(1, 4):
            data[f'lag_{lag}'] = data['y'].shift(lag)
        
        # Drop NaNs after creating lags
        xgb_data = data.dropna()
        
        # Feature Selection
        features = [f'lag_{i}' for i in range(1, 4)]
        
        # Train-Test Split
        train_x, test_x = xgb_data[features][xgb_data['ds'] <= "2020-12-01"], xgb_data[features][xgb_data['ds'] > "2020-12-01"]
        train_y, test_y = xgb_data['y'][xgb_data['ds'] <= "2020-12-01"], xgb_data['y'][xgb_data['ds'] > "2020-12-01"]
        
        # Initialize and train XGBoost model
        xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
        xgb_model.fit(train_x, train_y)
        
        # Make predictions
        xgb_preds = xgb_model.predict(test_x)

        # Plot XGBoost Predictions
        fig_xgb = go.Figure()
        fig_xgb.add_trace(go.Scatter(x=test_data['ds'], y=test_y, mode='lines', name='Actual', line=dict(color='gray')))
        fig_xgb.add_trace(go.Scatter(x=test_data['ds'], y=xgb_preds, mode='lines', name='XGBoost Predictions', line=dict(color='green')))
        # fig_xgb.update_layout(title='XGBoost Predictions vs
        fig_xgb.update_layout(title='XGBoost Predictions vs Actual', xaxis_title='Date', yaxis_title='Traffic Volume')
        st.plotly_chart(fig_xgb)

        # Metrics
        mae_xgb = mean_absolute_error(test_y, xgb_preds)
        rmse_xgb = math.sqrt(mean_squared_error(test_y, xgb_preds))
        smape_xgb = smape(test_y, xgb_preds)
        st.write(f"**Symmetric Mean Absolute Percentage Error (SMAPE)**: {smape_xgb:.2f}%")

else:
    st.write("Please upload a CSV file to proceed.")