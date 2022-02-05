import MetaTrader5 as mt5

from datetime import datetime

import pandas as pd
# import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)  # cuántas columnas mostramos
pd.set_option('display.width', 1500)  # máx. anchura del recuadro para la muestra

mt5.initialize()
mt5.login(61046869, password="lcyVgq5a")



# # MIS DATOS #####################################
# datos_mi_cuenta=mt5.account_info()._asdict()
# for organiza in datos_mi_cuenta:
#     print("  {}={}".format(organiza, datos_mi_cuenta[organiza]))

ACTIVOS=["EURUSD","XAUUSD","USDX","USDJPY","USDCHF","GBPJPY","GER40","NAS100","US500","BTCUSD","ETHUSD"]

for simbolos in ACTIVOS:
    ticks =  mt5.copy_ticks_from(simbolos, datetime(2022, 1, 1, 13), 100000000, mt5.COPY_TICKS_ALL)
    ticks_frame = pd.DataFrame(ticks)
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    ticks_frame["precio"]=(ticks_frame.bid+ticks_frame.ask)/2

    ticks_frame=ticks_frame[["time","precio"]].set_index("time")
    # ticks_frame.to_csv(simbolos+".csv")
    ticks_frame.to_csv(simbolos+"Enero.csv")
    print("el Excel de ",simbolos, "esta listo")


