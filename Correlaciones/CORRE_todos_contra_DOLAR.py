import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
from statsmodels.tsa.stattools import coint
import numpy as np
import seaborn
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)  # cuántas columnas mostramos
pd.set_option('display.width', 1500)  # máx. anchura del recuadro para la muestra

mt5.initialize()
# mt5.login(61046869, password="lcyVgq5a")

LOS_ACT=["EURUSD","XAUUSD","USDJPY","USDCHF","GBPJPY","GER40","NAS100","US500","UK100","BTCUSD"]
# LOS_ACT=["EURUSD"]
for todos in LOS_ACT:
    ACTIVOS=[todos ,"USDX"]

    los_precios=[]
    for simbolos in ACTIVOS:
        ticks =  mt5.copy_ticks_from(simbolos, datetime(2022, 2, 15, 19), 100000000, mt5.COPY_TICKS_ALL)
        ticks_frame = pd.DataFrame(ticks)
        ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

        ticks_frame["precio"]=(ticks_frame.bid+ticks_frame.ask)/2

        ticks_frame=ticks_frame[["time","precio"]].set_index("time")
        ticks_frame=ticks_frame.resample("1min").mean()
        los_precios.append(ticks_frame)

    dataframe=pd.DataFrame(columns=ACTIVOS)

    for este in range(len(ACTIVOS)):
        dataframe[ACTIVOS[este]]=los_precios[este]
    dataframe=dataframe.fillna(method="bfill")
    dataframe=dataframe.dropna()




    Symbol1_prices = dataframe.iloc[:,0][-11000:]
    Symbol2_prices = dataframe.iloc[:,1][-11000:]

    score, pvalue, _ = coint(Symbol1_prices, Symbol2_prices)

    def zscore(series):
        return (series-series.mean())/np.std(series)

    ratios=Symbol1_prices/Symbol2_prices

    # zscore(ratios).plot()
    # plt.axhline(zscore(ratios).mean(), color="black")
    # plt.axhline(1.0, color="red")
    # plt.axhline(-1.0, color="green")
    # plt.title(Symbol1_prices.name)
    # plt.show()

    ratios.plot()
    buy = ratios.copy()
    sell = ratios.copy()
    buy[zscore(ratios) > -1] = 0
    sell[zscore(ratios) < 1] = 0
    buy.plot(color="g", linestyle="None", marker="^")
    sell.plot(color="r", linestyle="None", marker="v")
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, ratios.min(), ratios.max()))

    plt.legend(["Ratio", "Buy Signal", "Sell Signal",],loc="upper left")
    plt.twinx()
    Symbol1_prices.plot()
    plt.legend(loc="upper right")
    plt.show()