import MetaTrader5 as mt5


mt5.initialize()
LOS_ACT=["EURUSD","XAUUSD","USDJPY","USDCHF","GBPJPY","EURCHF","GER40","NAS100","US500","UK100","BTCUSD"]
indices=["GER40","NAS100","US500","UK100","USDX"]

def comprar():

    for x in LOS_ACT:
        symbol = x  #<<<<x son los activos desde el eurusd hasta el btc

        if x in indices:   #>>> el lote de los indices es diferente al de divisas
            lot = 0.1
        else:
            lot = 0.01

        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).bid
        deviation = 0

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": price - 10 * point,
            "tp": price + 50 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "100 y 100python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        # print("{:<7}|{:>10f}".format(x,point))

        # enviamos la solicitud comercial
        result = mt5.order_send(request)
        # comprobamos el resultado de la ejecución
        print("Orden enviada en {} {} lots al precio {}".format(symbol, lot, price));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("ERROR: {} ".format(result.comment))

            # mt5.shutdown()


