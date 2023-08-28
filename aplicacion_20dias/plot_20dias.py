import datetime
import MetaTrader5 as meta
import pandas as pd
from pylab import *


meta.initialize()
fecha= datetime.datetime.today()-datetime.timedelta(days=30)

datos=pd.DataFrame(meta.copy_rates_range("EURUSD",meta.TIMEFRAME_M1,fecha,datetime.datetime.today()))[["time","close"]].set_index("time")
datos.index=pd.to_datetime(datos.index,unit="s",)
datos.index=pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")

lista_dias=datos.index.unique()
dia=[]
for x in range(len(lista_dias)):
    dia.append(datos.loc[lista_dias[x]])
    # dia[x] = dia[x].groupby("time").mean()
    # dia[x]["contar"] = range(1, len(dia[x]) + 1)
print(dia[1])
ultimos_20dias= figure(figsize=(30,30))
for i in range(len(dia)):
    diferencia= 100*(dia[i].close[-1] - dia[i].close[0])/dia[i].close[0]



    if dia[i].close[0] < dia[i].close[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"

    subplot(5, 5, i + 1, frameon=True, xticks=[], yticks=[], facecolor=color_fondo)

    dia_sem=pd.to_datetime(lista_dias[i]).strftime("%d-%a")
    text_titulo = f"{dia_sem} [{diferencia:.2f}%]"
    title(text_titulo)
    plot(dia[i].values, color="k")

subplots_adjust(top=0.9,bottom=0.01, hspace=0.2, wspace=0.1,left=0.01,right=0.99)

show()
#
# print(fecha)
# df=pd.DataFrame(meta.copy_rates_range("EURUSD",meta.TIMEFRAME_D1,datetime.datetime(2000,1,1),datetime.datetime.today())).set_index("time")
# df.index=pd.to_datetime(df.index,unit="s",)
# df.index=pd.DatetimeIndex(df.index).strftime("%Y-%m-%d")
#
#
# df['diferencia'] = df['close'] - df['open']
# df['cambio'] = df['diferencia'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
# df['dias_continuos'] = df.groupby((df['cambio'] != df['cambio'].shift(1)).cumsum()).cumcount() + 1
# print(df.dias_continuos.value_counts())
# print(df)
