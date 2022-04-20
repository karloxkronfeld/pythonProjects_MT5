from riesgo_operac_abiertas_CALCUlar.Calcular_riesgo import Calculadora_Riesgo
import tkinter as tk



def actualizar_etiqueta():

    Texto_riesgo.delete("1.0", tk.END)
    Texto_riesgo.insert("end", Calculadora_Riesgo()[0])

    root.after(2000, actualizar_etiqueta)






root = tk.Tk()
root.config(width=1600, height=600)
root.title("Consola de Trading")

Texto_riesgo= tk.Text(root,)
Texto_riesgo.config(font=("Courier", 14),)
Texto_riesgo.insert("end", Calculadora_Riesgo()[0])
Texto_riesgo.place(x=10,y=50)





root.after(2000, actualizar_etiqueta)
root.mainloop()

