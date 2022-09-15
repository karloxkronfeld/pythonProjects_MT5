import MetaTrader5 as meta

meta.initialize()
activos=["EURUSD","BTCUSD","XAUUSD","USDJPY","USDCHF","GBPJPY","EURCHF",".USTECHCash",".US500Cash",
         "GBPUSD","BRENT","AUDJPY","EURJPY","CHFJPY","CADJPY"]

#
# simbolos=meta.symbols_get()
#
# for x in simbolos:
#     print(x.name)
# for x in activos:
#     print(meta.symbol_info(x).trade_tick_size)
#
print(meta.symbol_info("EURCHF").trade_tick_size)
print(meta.symbol_info("EURCHF").trade_tick_value)