import streamlit as st
from src.preprocesamiento import cargar_y_preprocesar
from src.modelo import entrenar_modelo
import os

st.set_page_config(page_title="SuperFresh - Ventas 2024", layout="wide")
st.title("SuperFresh - Ventas 2024")

# Generar o cargar datos
data_path = "data/ventas_superfresh.csv"

if not os.path.exists(data_path):
    os.makedirs("data", exist_ok=True)

# Cargar y mostrar parte del dataset
df = cargar_y_preprocesar(data_path)
num_filas = st.slider("Selecciona el número de filas a mostrar", min_value=5, max_value=100, value=20)
st.subheader("Vista previa")
st.dataframe(df.head(num_filas))

# Entrenar el modelo
st.subheader("Predicción de Ventas")
modelo, X_test, y_test, predicciones, mse = entrenar_modelo(df)
st.write(f"Predicción de Ventas de este mes: **{mse:.2f}**")
