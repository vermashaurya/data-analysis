import pandas as pd
from sklearn.metrics import mean_squared_log_error, mean_absolute_percentage_error
from datetime import datetime
import streamlit as st

st.title("Error Metrics Calculation for Performance Index")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Dataset Preview:")
    st.dataframe(data.head())

    data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

    X = data[['Extracurricular Activities']]

    y_true = data['Performance Index']

    y_pred = [y_true.mean()] * len(y_true)

    st.write("Dataset with mapped 'Extracurricular Activities' column:")
    st.dataframe(data.head())

    msle = mean_squared_log_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)

    st.write(f"The calculated MSLE is: {msle:.4f} or {msle * 100:.4f}%")
    st.write(f"The calculated MAPE is: {mape:.2f} or {mape * 100:.2f}%")

    current_dateTime = datetime.now()
    st.write("Timestamp:")
    st.write(current_dateTime)
