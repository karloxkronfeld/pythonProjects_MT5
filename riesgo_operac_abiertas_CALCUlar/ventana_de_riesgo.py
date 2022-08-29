import pandas as pd

from riesgo_operac_abiertas_CALCUlar.Calcular_riesgo import Calculadora_Riesgo
import tkinter as tk


guardar_profits=[]
def actualizar_etiqueta():

    Texto_riesgo.delete("1.0", tk.END)
    Texto_riesgo.insert("end", Calculadora_Riesgo()[0])

    root.after(2000, actualizar_etiqueta)

###Desde linea 15-25---- es para calcular la diferencia entre el periodo 0 (cuando inicia el algoritmo) y el presente(actual)
    profit = Calculadora_Riesgo()[1].profit
    guardar_profits.append(profit)
    el_menos_1=guardar_profits[-1].str.replace("$","", regex=True).map(lambda x: float(x))
    el_cero=guardar_profits[0].str.replace("$","", regex=True).map(lambda x: float(x))
    la_diferencia= el_menos_1-el_cero
    df_la_diferencia = pd.DataFrame(data=[la_diferencia,Calculadora_Riesgo()[1].symbol]).T.set_index("symbol")
    Texto_riesgo2 = tk.Text(root, )
    Texto_riesgo2.config(font=("Courier", 14), )
    Texto_riesgo2.insert("end", df_la_diferencia)
    Texto_riesgo2.place(x=600, y=50)



root = tk.Tk()
root.config(width=1200, height=600)
root.title("Consola de Trading")

Texto_riesgo= tk.Text(root,)
Texto_riesgo.config(font=("Courier", 14),)
Texto_riesgo.insert("end", Calculadora_Riesgo()[0])
Texto_riesgo.place(x=10,y=50)






root.after(2000, actualizar_etiqueta)
root.mainloop()

