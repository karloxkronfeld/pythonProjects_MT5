import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # cuántas columnas mostramos
pd.set_option('display.width', 1500)      # máx. anchura del recuadro para la muestra

mt5.initialize()

dataframe=pd.DataFrame(data=list(mt5.positions_get()),
                       columns=mt5.positions_get()[0]._asdict().keys()).set_index("symbol",drop=False)
ACTIVOS = dataframe.symbol.values

tick_Values=[]
trade_tick=[]
for x in ACTIVOS:
    tick_Values.append(mt5.symbol_info(x).trade_tick_value)
    trade_tick.append(mt5.symbol_info(x).trade_tick_size)

dataframe["tick_values"]=tick_Values
dataframe["trade_tick_size"]=trade_tick
nuevo_df=dataframe.iloc[:,[9,-5,-11,-10,-2,-1]]
nuevo_df=nuevo_df.reset_index(drop=True)
# print(dataframe)

nuevo_df["diferencia"]= abs(nuevo_df.price_open - nuevo_df.sl)
nuevo_df["riesgo_pips"]= nuevo_df.diferencia/nuevo_df.trade_tick_size  # diferencia/tick_size
nuevo_df["multiplicador"]= nuevo_df.volume*nuevo_df.tick_values  # vol*tick_values
nuevo_df["riesgo"] = nuevo_df.riesgo_pips * nuevo_df.multiplicador

k_inicial= 977.49
suma_riesgo= sum(nuevo_df.riesgo)
suma_ganancias= sum(dataframe.profit)
# print(nuevo_df.sort_values("riesgo"))

print("El riesgo total es: {:.2F}$ USD".format(suma_riesgo))
print("Esta arriesgando un {:.2f}% del capital total({})".format(100*suma_riesgo/mt5.account_info().balance,mt5.account_info().balance))

print("Esta ganando un {:.2f}% del capital total({})".format(100*suma_ganancias/mt5.account_info().balance,mt5.account_info().balance))
print("Hoy la ganancia/perdida ={:.2f}%".format(100*(((mt5.account_info().balance+suma_ganancias)/k_inicial)-1)))
