from riesgo_operac_abiertas_CALCUlar.Calcular_riesgo import Calculadora_Riesgo
import tkinter as tk


#BOTON RIESGO
root = tk.Tk()
root.config(width=600, height=600)
root.title("Consola de Trading")

def _texto():
    Texto_riesgo= tk.Text(root,)
    Texto_riesgo.config(font=("Courier", 14),)

    Texto_riesgo.insert("end", Calculadora_Riesgo())
    Texto_riesgo.config(state="disable")
    Texto_riesgo.place(x=10,y=50)

boton_riesgo = tk.Button(root, text="Calcular Riesgo",command=_texto)
boton_riesgo.place(x=10, y=20)



root.mainloop()

