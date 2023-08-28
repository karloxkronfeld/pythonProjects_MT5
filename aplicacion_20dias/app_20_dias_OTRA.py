import datetime
import MetaTrader5 as meta
import pandas as pd
from pylab import *

meta.initialize()
fecha = datetime.datetime.today() - datetime.timedelta(days=30)

datos = pd.DataFrame(meta.copy_rates_range("US500", meta.TIMEFRAME_M1, fecha, datetime.datetime.today()))[["time", "close"]].set_index("time")
datos.index = pd.to_datetime(datos.index, unit="s")
datos.index = pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")

lista_dias = datos.index.unique()
dia = []
for x in range(len(lista_dias)):
    dia.append(datos.loc[lista_dias[x]])

fig, axes = subplots(5, 5, figsize=(30, 30), subplot_kw={'xticks': [], 'yticks': []})
for i, ax in enumerate(axes.flat):
    diferencia= 100*(dia[i].close[-1] - dia[i].close[0])/dia[i].close[0]
    if dia[i].close[0] < dia[i].close[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"
    ax.set_facecolor(color_fondo)
    dia_sem = pd.to_datetime(lista_dias[i]).strftime("%d-%a")
    titulo1 = f"{dia_sem}"
    titulo2 = f"[{diferencia:.2f}%]"
    ax.set_title(titulo1, loc="center", fontsize=14, fontweight="bold")
    ax.set_title(titulo2, loc="right", fontsize=12, fontweight="bold")

    ax.plot(dia[i].values, color="k")

subplots_adjust(top=0.9, bottom=0.01, hspace=0.2, wspace=0.1, left=0.01, right=0.99)

show()
