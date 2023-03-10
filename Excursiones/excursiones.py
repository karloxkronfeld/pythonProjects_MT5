from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
mt5.initialize()

historial = mt5.history_orders_get(datetime(2020,1,1), datetime.now())
# historial = mt5.history_deals_get(datetime(2020,1,1), datetime.now())
columnas=historial[0]._asdict().keys()
dataframe=pd.DataFrame(list(historial),columns=columnas)
# dataframe['time_setup'] = pd.to_datetime(dataframe['time_setup'], unit='s')
# dataframe['time_done'] = pd.to_datetime(dataframe['time_done'], unit='s')


# mis_datos=dataframe[["time_setup","time_done","symbol"]]
#
#
# mis_datos["fecha_hora_inicio"]=[mis_datos.time_setup.iloc[x].strftime("%d/%m %H:%M") for x in range(len(mis_datos))]
# mis_datos["fecha_hora_fin"]=[mis_datos.time_done.iloc[x].strftime("%d/%m %H:%M") for x in range(len(mis_datos))]
#
# el_precio= pd.DataFrame(mt5.copy_rates_range("BRENT",mt5.TIMEFRAME_H1,datetime(2022,1,1),datetime.now()))
#




# print(mis_datos[300:])
# print(dataframe["time_setup"]==dataframe["time_expiration"])
print(dataframe)