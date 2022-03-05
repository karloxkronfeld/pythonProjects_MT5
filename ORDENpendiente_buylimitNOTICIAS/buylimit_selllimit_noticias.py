import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()

LOS_SIMBOLOS=["EURUSD","XAUUSD","USDJPY","USDCHF","GBPJPY","BTCUSD","ETHUSD"]
# LOS_SIMBOLOS=["XAUUSD"]
for un_simbolo in LOS_SIMBOLOS:
    symbol = un_simbolo
    porcentaje=0.02
    lot = 0.01
    point = mt5.symbol_info(symbol).point
    price = (mt5.symbol_info_tick(symbol).ask + mt5.symbol_info_tick(symbol).bid)/2

    price1 = price*(1+porcentaje/100)
    sl1= price*(1-porcentaje/100)
    tp1= price*(1+porcentaje*2.5/100)  #2.5 es la relacion arriesgo 1:2.5

    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY_STOP,
        "price": price1,
        "sl": sl1,
        "tp": tp1,
        "deviation": 0,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    price2 = price*(1-porcentaje/100)
    sl2= price*(1+porcentaje/100)
    tp2= price*(1-porcentaje*2.5/100)  #2.5 es la relacion arriesgo 1:2.5

    result = mt5.order_send(request)
    print("Orden pendiente enviada: {} {} lotes al precio {} ".format(symbol, lot, price));

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("FALLO, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field, result_dict[field]))
            # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        mt5.shutdown()
        quit()  #    #P
    #

    request2 = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL_STOP,
        "price": price2,
        "sl": sl2,
        "tp": tp2,
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










