from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def entrenar_modelo(df):
    X = df[['producto_id', 'sucursal', 'mes', 'dia_semana', 'precio_unitario']]
    y = df['unidades_vendidas']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)
    mse = mean_squared_error(y_test, predicciones)

    return modelo, X_test, y_test, predicciones, mse