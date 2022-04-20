from riesgo_operac_abiertas_CALCUlar.Calcular_riesgo import Calculadora_Riesgo
from Compra_Vender_MT5 import vender_de_todo, comprar_de_todo
from Cerrar_TODO.Cerrar_posicoines_algorithm import cerrar_posiciones
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
    Texto_riesgo.place(x=10,y=150)

boton_riesgo = tk.Button(root, text="Calcular Riesgo",command=_texto)
boton_riesgo.place(x=10, y=20)


boton_ventas = tk.Button(root, text="Comprar", command=comprar_de_todo.comprar)
boton_ventas.place(x=120, y=20)

boton_ventas = tk.Button(root, text="Vender", command=vender_de_todo.vender)
boton_ventas.place(x=200, y=20)

photo = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Pictures\panicbuton.png")
photo_image=photo.zoom(25).subsample(100)
boton_panico= tk.Button(root,image=photo_image,command=cerrar_posiciones)
boton_panico.place(x=290,y=20)






root.mainloop()

