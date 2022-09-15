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
