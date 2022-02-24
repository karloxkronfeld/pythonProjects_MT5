import MetaTrader5 as mt5
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)  # cuántas columnas mostramos
pd.set_option('display.width', 1500)  # máx. anchura del recuadro para la muestra

mt5.initialize()

simbolo="US500"

datos = pd.DataFrame(mt5.copy_ticks_from(simbolo, datetime(2022, 2, 1, 19), 100000000, mt5.COPY_TICKS_ALL))
datos["time"]=pd.to_datetime(datos.time,unit="s")


datos_signal = pd.DataFrame(index=datos.index,data=datos.time)
datos_signal["precio"] = (datos.bid+datos.ask)/2
datos_signal = datos_signal.set_index("time")
datos_signal = datos_signal.resample("4h").mean()                     #<<<<<<<TEMPORALIDAD
datos_signal["diferencia_"] = datos_signal.precio.diff()

datos_signal["signal"] = 0.0
datos_signal["signal"] = np.where(datos_signal["diferencia_"]>0 , 1.0 , 0.0) #donde la diferencia es > que 0 escribe 1 si no 0
datos_signal["posicion"] = datos_signal["signal"].diff()
datos_signal= datos_signal.dropna()

def graficar_signal():
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel="Precio de {} en Febrero  ".format(simbolo))
    datos_signal['precio'].plot(ax=ax1, color='b', lw=2.)

    ax1.plot(datos_signal.loc[datos_signal.posicion == 1.0].index,  datos_signal.precio[datos_signal.posicion == 1.0], '^', markersize=5, color='g')

    ax1.plot(datos_signal.loc[datos_signal.posicion == -1.0].index,  datos_signal.precio[datos_signal.posicion == -1.0], 'v', markersize=5, color='r')

    plt.show()

capital_inicial=10000
posiciones=pd.DataFrame(index=datos_signal.index.fillna(0))
portafolio=pd.DataFrame(index=datos_signal.index.fillna(0))
posiciones["activo"]=datos_signal.signal
portafolio["posiciones"]=posiciones.multiply(datos_signal.precio,axis=0)
portafolio["cash"]=capital_inicial-(posiciones.diff().multiply(datos_signal.precio,axis=0)).cumsum()
portafolio["total"]=portafolio.posiciones+portafolio.cash
print("{} TOTAL\n{} EFECTIVO\n{} POSICIONES ABIERTAS".format(portafolio.total[-1],portafolio.cash[-1],portafolio.posiciones[-1]))





def graficar_portafolio():

    fig = plt.figure(figsize=(17, 7), frameon=False)
    fig.add_axes
    fig.add_subplot(131)
    portafolio.cash.plot()
    plt.legend()
    fig.add_subplot(132)
    portafolio.posiciones.plot()
    plt.legend()
    fig.add_subplot(133)
    portafolio.total.plot()
    plt.text(portafolio.index[-1], portafolio.total[-1], f'{portafolio.total[-1]:,.0f}',     size=30, ha="right", color="r")
    plt.legend()

    plt.show()
def graficar_portafolio2():
    if portafolio.total[-1] > 1000:
        color_letra = "g"
    else:
        color_letra = "r"

    fig, ax = plt.subplots(4, sharex="col")
    ax[0].plot(datos_signal.precio)

    ax[1].plot(portafolio.cash, label="cash")

    ax[2].plot(portafolio.posiciones, label="posicion")

    ax[3].plot(portafolio.total, label="Total")
    plt.text(portafolio.index[-1], portafolio.total[-1], f'{portafolio.total[-1]:,.0f}',
         size=30, ha="right", color=color_letra)
    plt.show()

def graficar_portafolio3():
    portafolio.plot()
    plt.text(portafolio.index[-1],portafolio.cash[-1],portafolio.cash[-1])
    plt.text(portafolio.index[-1],portafolio.posiciones[-1],portafolio.posiciones[-1])
    plt.text(portafolio.index[-1],portafolio.total[-1],portafolio.total[-1])
    plt.hlines(capital_inicial,portafolio.index[0],portafolio.index[-1],color="r",lw=3)

    plt.show()


graficar_portafolio()
print(portafolio)
# print(datos_signal)
# print(datos)