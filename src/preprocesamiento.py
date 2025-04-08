import pandas as pd

def cargar_y_preprocesar(filepath):
    df = pd.read_csv(filepath)
    df['fecha'] = pd.to_datetime(df['fecha'])

    df['mes'] = df['fecha'].dt.month
    df['dia_semana'] = df['fecha'].dt.dayofweek

    df['producto_id'] = df['producto_id'].astype('category').cat.codes
    df['sucursal'] = df['sucursal'].astype('category').cat.codes

    return df