import datetime
import MetaTrader5 as meta
import pandas as pd
from pylab import *


meta.initialize()
fecha= datetime.datetime.today()-datetime.timedelta(days=30)

datos=pd.DataFrame(meta.copy_rates_range("EURUSD",meta.TIMEFRAME_M1,fecha,datetime.datetime.today()))[["time","close"]].set_index("time")
datos.index=pd.to_datetime(datos.index,unit="s",)
datos.index=pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")
print(datos)
lista_dias=datos.index.unique()
dia=[]
for x in range(len(lista_dias)):
  dia.append(datos.loc[lista_dias[x]])
#

ultimos_20dias= figure(figsize=(20,20))
for i in range(len(dia)):
    if dia[i].close[0] < dia[i].close[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"

    subplot(5, 5, i + 1, frameon=True, xticks=[], yticks=[], facecolor=color_fondo)
    title(pd.to_datetime(lista_dias[i]).strftime("%d-%a"))

    plot(dia[i].values, color="k")
    # vlines(dia[i][dia[i].index == "18:00"].contar, minimo, maximo, )
    # vlines(dia[i][dia[i].index == "21:00"].contar, minimo, maximo, )
show()
