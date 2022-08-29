import MetaTrader5 as meta
import pandas as pd
from pylab import *

time_frame=meta.TIMEFRAME_D1
el_uno=".US500Cash"
el_dos="EURUSD"



meta.initialize()

activo1=pd.DataFrame(meta.copy_rates_from_pos(el_uno,time_frame,0,1000)).close
activo_porcentaje1=pd.DataFrame(meta.copy_rates_from_pos(el_uno,time_frame,0,1000)).close.pct_change()

activo2=pd.DataFrame(meta.copy_rates_from_pos(el_dos,time_frame,0,1000)).close
activo_porcentaje2=pd.DataFrame(meta.copy_rates_from_pos(el_dos,time_frame,0,1000)).close.pct_change()

correlacion_activo=activo1.rolling(2).corr(activo2)
correlacion=activo_porcentaje1.rolling(2).corr(activo_porcentaje2)
# print(correlacion)
# df.sp500.rolling(100).corr(df.nas100).plot()

subplot(2,3,1,)
title(el_uno)
activo_porcentaje1.plot(color="red")
subplot(2,3,2)
title(el_dos)
activo_porcentaje2.plot()
subplot(2,3,3)
title("correlacion")
correlacion.plot(color="g")
############################3
subplot(2,3,4)
activo1.plot(color="red")
subplot(2,3,5)
activo2.plot()
subplot(2,3,6)
correlacion_activo.plot(color="g")
show()