import MetaTrader5
import MetaTrader5 as mt5
from datetime import datetime,timedelta
import pandas as pd
import numpy as np

mt5.initialize()

ACTIVO= "SpotBrent"
fecha= datetime.today()-timedelta(days=30)
datos =pd.DataFrame(mt5.copy_ticks_from(ACTIVO, fecha, 9000000, mt5.COPY_TICKS_ALL))
datos.index=pd.to_datetime(datos.time,unit="s")

datos["precio"]= (datos.bid+datos.ask)/2
datos=datos["precio"]
print(datos.groupby(datos.index).mean())

lista_dias=datos.index.strftime("%Y-%m-%d").unique()

print(datos)


# ticks_frame = pd.DataFrame(ticks)
# ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')


