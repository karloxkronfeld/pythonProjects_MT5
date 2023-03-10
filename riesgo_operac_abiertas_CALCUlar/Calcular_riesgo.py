import MetaTrader5 as mt5
import pandas as pd
# import time

pd.set_option('display.max_columns', 500) # cuántas columnas mostramos
pd.set_option('display.width', 1500)      # máx. anchura del recuadro para la muestra
pd.options.mode.chained_assignment = None  # default='warn'

mt5.initialize()

def Calculadora_Riesgo():
    dataframe=pd.DataFrame(data=list(mt5.positions_get()),
                           columns=mt5.positions_get()[0]._asdict().keys()).set_index("symbol",drop=False)
    ACTIVOS = dataframe.symbol.values

    tick_Values=[]
    trade_tick=[]
    for x in ACTIVOS:
        print(mt5.symbol_info(x).trade_tick_value)

        tick_Values.append([mt5.symbol_info(x).trade_tick_value])

        trade_tick.append(mt5.symbol_info(x).trade_tick_size)

    dataframe["tick_values"]=tick_Values
    dataframe["trade_tick_size"]=trade_tick
    nuevo_df=dataframe.iloc[:,[9,-5,-11,-10,-2,-1]]
    nuevo_df=nuevo_df.reset_index(drop=True)


    nuevo_df["diferencia"]= abs(nuevo_df.price_open - nuevo_df.sl)
    nuevo_df["riesgo_pips"]= nuevo_df.diferencia/nuevo_df.trade_tick_size  # diferencia/tick_size
    nuevo_df["multiplicador"]= nuevo_df.volume*nuevo_df.tick_values  # vol*tick_values
    nuevo_df["riesgo"] = nuevo_df.riesgo_pips * nuevo_df.multiplicador



    k_inicial=8606.69 #mt5.account_info().balance
    suma_riesgo= sum(nuevo_df.riesgo)
    suma_ganancias= sum(dataframe.profit)
    nuevo_nuevo_df=nuevo_df[["volume", "symbol", "riesgo_pips", "riesgo"]]
    nuevo_nuevo_df["profit"]=dataframe.profit.values
    nuevo_df["profit"]=nuevo_nuevo_df.profit
    nuevo_df["riesgo %"]=100*nuevo_df.riesgo/k_inicial
    nuevo_df["riesgo %"]= nuevo_df['riesgo %'].map(lambda x : ('%.2f')%x+" %")
    nuevo_df["riesgo"] = nuevo_df['riesgo'].map(lambda x: ('%.2f') % x + " $")
    nuevo_df["profit"] = nuevo_df['profit'].map(lambda x: ('%.2f') % x + " $")




    # print("El riesgo total es: {:.2F}$ USD".format(suma_riesgo))
    # print("Esta arriesgando un {:.2f}% del capital total({})".format(100*suma_riesgo/mt5.account_info().balance,mt5.account_info().balance))
    # print("Esta ganando un {:.2f}% del capital total({})".format(100*suma_ganancias/mt5.account_info().balance,mt5.account_info().balance))
    # print("Hoy la ganancia/perdida ={:.2f}%".format(100*(((mt5.account_info().balance+suma_ganancias)/k_inicial)-1)))

    return "Capital={:>10}".format(mt5.account_info().balance)+\
           "\nEl riesgo total es: {:>10.2f}$ USD  ({:.2f}%)".format(suma_riesgo,100 * suma_riesgo / mt5.account_info().balance)+ \
           "\n\nEstoy ganando/perdiendo:{:>7.2f}$ USD ({:.2f}%)".format(sum(nuevo_nuevo_df.profit),100 * suma_ganancias / mt5.account_info().balance)+ \
           "\n\nHoy la ganancia/perdida {:>7.2f}$ USD ({:.2f}%)".format(mt5.account_info().balance - k_inicial, 100 * (((mt5.account_info().balance) / k_inicial) - 1)) + \
           "\n\nTOTAL {:>25.2f}$ USD ({:.2f}%)".format(mt5.account_info().balance +suma_ganancias - k_inicial, 100 * (((mt5.account_info().balance+suma_ganancias) / k_inicial) - 1)) + "\n\n" + \
           "\n {:}".format(nuevo_df[["symbol", "riesgo","riesgo %","profit","volume"]].sort_values("symbol").set_index("symbol")),nuevo_df[["symbol","profit"]]





# while True:
#
#     print("\r",Calculadora_Riesgo(),end=" ")
#     time.sleep(4)
#

