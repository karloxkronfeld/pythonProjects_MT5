
import MetaTrader5 as meta
import pandas as pd
from pylab import *


meta.initialize()
fecha= datetime.datetime.today()-datetime.timedelta(days=20)

datos=pd.DataFrame(meta.copy_rates_range("XAUUSD",meta.TIMEFRAME_M10,fecha,datetime.datetime.today()))[["time","close","open"]].set_index("time")

datos.index=pd.to_datetime(datos.index,unit="s",)


datos['diferencia'] = datos['close'] - datos['open']
datos['cambio'] = datos['diferencia'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
datos['dias_continuos'] = datos.groupby((datos['cambio'] != datos['cambio'].shift(1)).cumsum()).cumcount() + 1
dias_continuos= pd.DataFrame(datos.dias_continuos.value_counts())
dias_continuos["probabilidades"]=[100*x/1932 for x in dias_continuos.dias_continuos]
print(dias_continuos)




