import MetaTrader5 as mt5


mt5.initialize()
mt5.login(61046869, password="lcyVgq5a")


symbol = "EURUSD"
lot = 0.01
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 0

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": price,
    "sl": price + 100 * point,
    "tp": price - 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

# enviamos la solicitud comercial
result = mt5.order_send(request)
# comprobamos el resultado de la ejecución
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    # solicitamos el resultado en forma de diccionario y lo mostramos elemento por elemento
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    mt5.shutdown()
    quit()
