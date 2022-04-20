import pandas as pd
import numpy as np

datos_enero = pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\XAUUSDEnero.csv")
datos_febrero = pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\XAUUSDFebrero.csv")
datos=pd.concat([datos_enero, datos_febrero]).set_index("time")
datos.index = pd.DatetimeIndex(datos.index)
datos = datos.resample("1h").mean()

goog_data_signal = pd.DataFrame(index=datos.index)
goog_data_signal['price'] = datos['precio']

bin_width=200
data=goog_data_signal

data['sup_tolerance'] = pd.Series(np.zeros(len(data)))
data['res_tolerance'] = pd.Series(np.zeros(len(data)))
data['sup_count'] = pd.Series(np.zeros(len(data)))
data['res_count'] = pd.Series(np.zeros(len(data)))
data['sup'] = pd.Series(np.zeros(len(data)))
data['res'] = pd.Series(np.zeros(len(data)))
data['positions'] = pd.Series(np.zeros(len(data)))
data['signal'] = pd.Series(np.zeros(len(data)))
in_support=0
in_resistance=0


for x in range((bin_width - 1) + bin_width, len(data)):
     data_section = data[x - bin_width:x + 1]
     support_level=min(data_section['price'])
     resistance_level=max(data_section['price'])
     range_level=resistance_level-support_level
     data['res'][x]=resistance_level
     data['sup'][x]=support_level
     data['sup_tolerance'][x]=support_level + 0.2 * range_level
     data['res_tolerance'][x]=resistance_level - 0.2 * range_level
     if data['price'][x]>=data['res_tolerance'][x] and data['price'][x] <= data['res'][x]:
        in_resistance+=1
        data['res_count'][x]=in_resistance
     elif data['price'][x] <= data['sup_tolerance'][x] and \
        data['price'][x] >= data['sup'][x]:
        in_support += 1
        data['sup_count'][x] = in_support
     else:
        in_support=0
        in_resistance=0
     if in_resistance>2:
        data['signal'][x]=1
     elif in_support>2:
        data['signal'][x]=0
     else:
        data['signal'][x] = data['signal'][x-1]
data['positions']=data['signal'].diff()
# trading_support_resistance(goog_data_signal)

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
goog_data_signal['sup'].plot(ax=ax1, color='g', lw=2.)
goog_data_signal['res'].plot(ax=ax1, color='b', lw=2.)
goog_data_signal['price'].plot(ax=ax1, color='r', lw=2.)
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index, goog_data_signal.price[goog_data_signal.positions == 1.0], '^', markersize=7, color='k',label='buy')
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index, goog_data_signal.price[goog_data_signal.positions == -1.0], 'v', markersize=7, color='k',label='sell')
plt.legend()
plt.show()
