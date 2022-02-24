import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = ttk.Button(text="¡Hola, mundo!")
boton.place(x=50, y=50)
root.mainloop()








import time
import MetaTrader5 as mt5

# mostramos los datos sobre el paquete MetaTrader5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establecemos la conexión con el terminal MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# preparamos la estructura de la solicitud de compra
symbol = "EURUSD"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

# si el símbolo no está disponible en MarketWatch, lo añadimos
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol, True):
        print("symbol_select({}}) failed, exit", symbol)
        mt5.shutdown()
        quit()

lot = 0.01
point = mt5.symbol_info(symbol).point
position_id = 43302188
price = mt5.symbol_info_tick(symbol).bid
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}
# enviamos la solicitud comercial
result = mt5.order_send(request)
# comprobamos el resultado de la ejecución
print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, symbol, lot, price,
                                                                                     deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send failed, retcode={}".format(result.retcode))
    print("   result", result)
else:
    print("4. position #{} closed, {}".format(position_id, result))
    # solicitamos el resultado en forma de diccionario y lo mostramos elemento por elemento
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

# finalizamos la conexión con el terminal MetaTrader 5
mt5.shutdown()
