request2 = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY_STOP,
    "price": price,
    "sl": sl,
    "tp": tp,
    "deviation": 0,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

result = mt5.order_send(request2)
print("Orden pendiente enviada: {} {} lotes al precio {} ".format(symbol, lot, price));

if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("FALLO, retcode={}".format(result.retcode))
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
        if field == "request2":
            traderequest2_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest2_dict:
                print("       traderequest2: {}={}".format(tradereq_filed, traderequest2_dict[tradereq_filed]))
    mt5.shutdown()
    quit()  # #P


#













#
def riesgo():
    df = pd.DataFrame(list(mt5.positions_get()), columns=mt5.positions_get()[0]._asdict().keys()).set_index("symbol",drop=False)
    nuevo_df=df[["price_open","sl"]]
    mis_activos = {'EURUSD':100,
                   'XAUUSD':1000,
                   'USDX':1000,
                   'USDJPY':1000,
                   'USDCHF':1000,
                   'GBPJPY':1000,
                   'US500':1000,
                   'UK100':1000,
                   'GER40':10000,
                   'SpotBrent':1000,
                   'BTCUSD':10000}

    nuevo_df=nuevo_df.reset_index(drop=False)
    nuevo_df["pips_raw"]=abs(nuevo_df.price_open-nuevo_df.sl)
    nuevo_df["multiplicador"]=mis_activos.setdefault(nuevo_df.symbol)


    print(nuevo_df)
