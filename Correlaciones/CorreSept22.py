import MetaTrader5 as meta
import pandas as pd
from pylab import *

meta.initialize()
ACTIVOS=["EURUSD","EURCHF","XAUUSD","USDJPY","USDCHF","GBPJPY","GBPUSD",]
time_frame= meta.TIMEFRAME_M1

datos=pd.DataFrame()
for simbolos in ACTIVOS:
  datos[simbolos]=meta.copy_rates_from_pos(simbolos, time_frame, 0, 1000)["close"]




datos_porcentaje=datos.pct_change()
datos_cum=datos.pct_change().cumsum()



todas_las_correlaciones=[]
LOS_TITULOS=[]
for x in range(7):
    for y in range(7):
        todas_las_correlaciones.append(datos_porcentaje[ACTIVOS[x]].rolling(100).corr(datos_porcentaje[ACTIVOS[y]]))
        LOS_TITULOS.append("{}/{}".format(ACTIVOS[x],ACTIVOS[y]))

print(LOS_TITULOS)


todo_fig=figure(figsize=(20,20),)

for i in range(len(todas_las_correlaciones)):

    subplot(7, 7, i +1, frameon=False, xticks=[])
    title(LOS_TITULOS[i])
    todas_las_correlaciones[i].plot()
    todo_fig.tight_layout(pad=3.0)
#
show()
# # #
# # # #

