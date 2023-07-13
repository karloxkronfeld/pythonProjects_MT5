import datetime
import MetaTrader5 as meta
import pandas as pd
from pylab import *

meta.initialize()
fecha = datetime.datetime.today() - datetime.timedelta(days=30)

datos = pd.DataFrame(meta.copy_rates_range("US500", meta.TIMEFRAME_M1, fecha, datetime.datetime.today()))[["time", "close"]].set_index("time")
datos.index = pd.to_datetime(datos.index, unit="s")

lista_dias = datos.index.unique()
dia = []
for x in range(len(lista_dias)):
    dia.append(datos.loc[lista_dias[x]])

fig, axes = subplots(5, 5, figsize=(20, 20), subplot_kw={'xticks': [], 'yticks': []})
for i, ax in enumerate(axes.flat):
    diferencia = 100 * (dia[i].close[0] - dia[i].close[-1]) / dia[i].close[0]
    if dia[i].close[0] < dia[i].close[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"
    ax.set_facecolor(color_fondo)
    ax.set_title(lista_dias[i].strftime("%Y-%m-%d"))
    ax.plot(dia[i].values, color="k")

    # Agregar el texto con la diferencia porcentual
    texto = f"Diferencia: {diferencia:.2f}%"
    ax.text(0.5, 0.5, texto, horizontalalignment='center', verticalalignment='center', fontsize=12)

tight_layout()
show()
