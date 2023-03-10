
import MetaTrader5 as meta
import pandas as pd
from pylab import *


meta.initialize()
simbolo="US500"
fecha= datetime.datetime.today()-datetime.timedelta(days=30)

datos=pd.DataFrame(meta.copy_rates_range(simbolo,meta.TIMEFRAME_M1,fecha,datetime.datetime.today()))[["time","close"]].set_index("time")
datos.index=pd.to_datetime(datos.index,unit="s",).strftime("%Y-%m-%d %H:%M")
datos["time"]=pd.to_datetime(datos.index).strftime("%H:%M")
datos.index=pd.to_datetime(datos.index).strftime("%Y-%m-%d")


lista_dias = datos.index.unique()
dia = []
for i in range(len(lista_dias)):
    dia.append(datos.loc[lista_dias[i]].set_index("time"))
    dia[i] = dia[i].groupby("time").mean()
    dia[i]["contar"] = range(1, len(dia[i]) + 1)

media_global=datos.close.mean()

mensual = figure(figsize=(20, 20))
lista_maximos, lista_minimos, lista_promedios = [], [], []
for i in range(len(lista_dias)):
    maximo = max(dia[i].close)
    minimo = min(dia[i].close)
    promedio = dia[i].values.mean()

    lista_maximos.append(maximo)
    lista_minimos.append(minimo)
    lista_promedios.append(promedio)

    if dia[i].close[0] < dia[i].close[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"

    subplot(5, 5, i + 1, frameon=True, yticks=[], facecolor=color_fondo)
    subplots_adjust(bottom=0.1, right=0.8, top=1)
    title(pd.to_datetime(lista_dias[i]).strftime("%d-%a"), fontdict={'verticalalignment': 'top'})

    dia[i].close.plot(color="k", xlabel="")
    vlines(dia[i][dia[i].index == "18:00"].contar, minimo, maximo, )
    vlines(dia[i][dia[i].index == "21:00"].contar, minimo, maximo, )
show()