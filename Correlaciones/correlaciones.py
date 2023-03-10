import MetaTrader5
import MetaTrader5 as meta
import pandas as pd
from pylab import *

meta.initialize()

temporalidad= meta.TIMEFRAME_M1

ACTIVOS=["NAS100","EURUSD"]
# ACTIVOS=["USDX","EURUSD","XAUUSD","USDJPY",]
         # "USDCHF","GBPJPY","GER40","NAS100","US500","UK100","BTCUSD"]

los_precios=[]
for simbolos in ACTIVOS:
    datos = pd.DataFrame(meta.copy_rates_from_pos(simbolos, temporalidad, 0, 10000))[["time", "close"]].set_index("time")
    datos.index = pd.to_datetime(datos.index, unit='s')
    los_precios.append(datos)
dataframe=pd.DataFrame(columns=ACTIVOS)
for una_x in range(len(ACTIVOS)):
    dataframe[ACTIVOS[una_x]]=los_precios[una_x]
dataframe=dataframe.fillna(method="bfill")
# dataframe=dataframe.pct_change()
dataframe=dataframe[1000:]
# print(dataframe.pct_change()*100)

correlacion1=dataframe[ACTIVOS[0]].rolling(1000).corr(dataframe[ACTIVOS[1]])


subplot(2,1,1)
correlacion1.plot()
subplot(2,1,2)
dataframe[ACTIVOS[0]].plot(color="g")


twinx()

dataframe[ACTIVOS[1]].plot(color="r")
legend()
show()

#
# import MetaTrader5 as meta
# import pandas as pd
# from pylab import *
#
# meta.initialize()
# ACTIVOS=["EURUSD","EURCHF","XAUUSD","USDJPY","USDCHF","GBPJPY","GBPUSD",]
# time_frame= meta.TIMEFRAME_M1
#
# datos=pd.DataFrame()
# for simbolos in ACTIVOS:
#   datos[simbolos]=meta.copy_rates_from_pos(simbolos, time_frame, 0, 1000)["close"]
#
# datos_porcentaje=datos.pct_change()
# datos_cum=datos.pct_change().cumsum()
#
# mis_numeros=[]
# for alfa in range(1,7):
#     mis_numeros.append(alfa)
# for beta in range(1,6):
#     mis_numeros.append(7+beta+1)
# for gamma in range(1,5):
#     mis_numeros.append(14+gamma+2)
# for delta in range(1,4):
#     mis_numeros.append(21+delta+3)
# for epsilon in range(1,3):
#     mis_numeros.append(35+epsilon+4)
#
#
# ## es mas facil seleccionar todos los numeros uno por uno num=[1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 17, 18, 19, 20, 25, 26, 27, 40, 41]
#
# mis_numeros=sorted(mis_numeros)
# print(mis_numeros)
# print(len(mis_numeros))
#
# todas_las_correlaciones=[]
# LOS_TITULOS=[]
# for x in range(7):
#     for y in range(7):
#         todas_las_correlaciones.append(datos_porcentaje[ACTIVOS[x]].rolling(100).corr(datos_porcentaje[ACTIVOS[y]]))
#         LOS_TITULOS.append("{}/{}".format(ACTIVOS[x],ACTIVOS[y]))
#
# todo_fig=figure(figsize=(20,20),)
#
# for i in range(len(mis_numeros)):
#
#     subplot(4, 5, i +1, frameon=False, xticks=[])
#     title(LOS_TITULOS[mis_numeros[i]])
#     todas_las_correlaciones[mis_numeros[i]][-100:].plot()
#     todo_fig.tight_layout(pad=3.0)
# #
# show()
# # # #
# # # # #
#
