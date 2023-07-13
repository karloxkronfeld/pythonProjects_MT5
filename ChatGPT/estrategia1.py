import tensorflow as tf
import matplotlib.pyplot as plt
import datetime
import MetaTrader5 as meta
import pandas as pd

meta.initialize()
# Importar datos históricos
fecha= datetime.datetime.today()-datetime.timedelta(days=21)

data = pd.DataFrame(meta.copy_ticks_from("US500", datetime.datetime(2023, 3, 1, 19), 100000, meta.COPY_TICKS_ALL)).set_index("time")  #año,mes,dia,hora
data["Close"]=(data.bid+data.ask)/2
data.index=pd.to_datetime(data.index,unit="s").strftime("%Y-%m-%d %H:%M")
data=data[["Close"]]
data=data.groupby("time").mean()

print(data)

# Normalizar los datos
data_norm = (data - data.mean()) / data.std()

# Preparar los datos de entrenamiento y prueba
train_size = int(len(data_norm) * 0.8)
train_data = data_norm[:train_size]
test_data = data_norm[train_size:]

# Definir la arquitectura del modelo de red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilar el modelo y definir la función de pérdida y el optimizador
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenar el modelo
history = model.fit(
    train_data.drop(columns=['Close']),
    train_data['Close'],
    epochs=100,
    validation_data=(
        test_data.drop(columns=['Close']),
        test_data['Close']
    )
)

# Graficar la función de pérdida durante el entrenamiento
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Hacer predicciones sobre los precios de las acciones
train_preds = model.predict(train_data.drop(columns=['Close'])).reshape(-1)
test_preds = model.predict(test_data.drop(columns=['Close'])).reshape(-1)

# Graficar los precios reales y las predicciones
plt.plot(data['Close'][:train_size])
plt.plot(data['Close'][train_size:])
plt.plot(train_data.index, train_preds)
plt.plot(test_data.index, test_preds)
plt.legend(['Training Data', 'Testing Data', 'Training Predictions', 'Testing Predictions'])
plt.show()

# Calcular los retornos diarios y hacer las decisiones de trading
data['Returns'] = data['Close'].pct_change()
data['Signal'] = 0
data.loc[data_norm['Close'].shift(-1) > test_preds, 'Signal'] = 1
data.loc[data_norm['Close'].shift(-1) < test_preds, 'Signal'] = -1
data['Strategy'] = data['Signal'] * data['Returns']

# Calcular el rendimiento de la estrategia de trading
print(f"Total Returns: {data['Strategy'].sum()}")
