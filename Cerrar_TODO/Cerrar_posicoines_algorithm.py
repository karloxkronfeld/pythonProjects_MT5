import MetaTrader5 as mt5
import pandas as pd
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

pd.set_option('display.max_columns', 500) # cuántas columnas mostramos
pd.set_option('display.width', 1500)      # máx. anchura del recuadro para la muestra



def cerrar_posiciones():
    mt5.initialize()
    df = pd.DataFrame(list(mt5.positions_get()), columns=mt5.positions_get()[0]._asdict().keys()).set_index("symbol",drop=False)
    messagebox.showinfo(message="El resultado final es \n{:.2}".format(sum(df.profit)), title="RESULTADO")




    for nro_simbolos in range(len(df)): #nro_simbolos son el #de operaciones abiertas en metatrader

        symbol=df.symbol[nro_simbolos]
        lot= df.volume[nro_simbolos]

        if (df.iloc[nro_simbolos].type==mt5.ORDER_TYPE_BUY): #Si la orden es compra, entonces preparamos una venta al precio de venta
            tipo_orden=mt5.ORDER_TYPE_SELL
            price=mt5.symbol_info_tick(symbol).bid
        else:
            tipo_orden=mt5.ORDER_TYPE_BUY
            price=mt5.symbol_info_tick(symbol).ask

        position_id = int(df.ticket[nro_simbolos])  #ticket y el identifier es el mismo numero
        deviation= 0

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": tipo_orden,
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
        print("Se cerro la posicion#{}: de {} con volumen {} lots al precio {}".format(position_id, symbol, lot, price,));

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("CUIDADO. order_send failed, retcode={}".format(result.retcode))
            print("   result", result)
        else:
            print("CERRADO #{} closed, {}".format(position_id, result))
            # solicitamos el resultado en forma de diccionario y lo mostramos elemento por elemento
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))



root=Tk()
root.title("Botón de panico, CERRAR TODO")
photo = PhotoImage(file=r"C:\Users\Personal\OneDrive\Pictures\panicbuton.png")
photo_image=photo.subsample(1,1)
Button(root,image=photo_image,command=cerrar_posiciones).pack(side=BOTTOM,pady=0,)
mainloop()


