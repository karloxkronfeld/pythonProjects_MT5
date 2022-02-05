import statistics

import pandas as pd
from pylab import *

def leer_datos(temporalidad="10min"):

    lista_archivos = ["GER40Enero.csv"]
    for equis in lista_archivos:
        datos = pd.read_csv(r"C:\Users\Personal\Downloads\PRojectosPython\BasesDeDatos(conScript)\\" + equis).set_index("time")
        datos.index = pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")
        # datos=datos.groupby(pd.Grouper(freq=str(temporalidad))).mean().dropna()
    return datos

data=leer_datos()

moda=statistics.mode(data.precio)
media=statistics.mean(data.precio)
lista_dias=data.index.unique()

dia=[] #Son todos los dias del mes separados cada uno en dataframes
for x in range(len(lista_dias)):
    dia.append(data.loc[lista_dias[x],["precio"]])
# print(dia)

print(len(dia))

mensual=figure(figsize=(30,30)) #mensual es la figura que voy a llenar de graficas

# for i in range(0,22):
#     subplot(4,6,i+1,frameon=True,xticks=[],yticks=[])
#     plot(dia[i].values)
#     title(pd.to_datetime(lista_dias[i]).strftime("%d-%a"))


lista_maximos, lista_minimos, lista_promedios = [], [], []
for i in range(0, 21):
    maximo = max(dia[i].precio)
    minimo = min(dia[i].precio)
    promedio = dia[i].values.mean()

    lista_maximos.append(maximo)
    lista_minimos.append(minimo)
    lista_promedios.append(promedio)

    if dia[i].precio[0] < dia[i].precio[-1]:
        color_fondo = "lightgreen"
    else:
        color_fondo = "lightcoral"

    subplot(5, 5, i + 1, frameon=True, xticks=[], yticks=[], facecolor=color_fondo)
    title(pd.to_datetime(lista_dias[i]).strftime("%d-%a"),size=10)

    plot(dia[i].values, color="k")

    text(0, maximo, "%.3f" % maximo, color="r", ha="right")  # MAXIMO DEL DIA
    hlines(maximo, 0, len(dia[i]), colors="r")
    text(0, minimo, "%.3f" % minimo, color="g", ha="right")  # MINIMO DEL DIA
    hlines(minimo, 0, len(dia[i]), colors="g")
    text(0, promedio, "%.3f" % promedio, color="b", ha="right")  # PROMEDIO DEL DIA
    hlines(promedio, 0, len(dia[i]), colors="b")

    # hlines(moda,0,len(dia[i]),colors="white",ls=":")

    text(0, dia[i].precio[0], "%.3f" % dia[i].precio[0], ha="right",size=8)  # PRECIO APERTURA
    text(len(dia[i]), dia[i].precio[-1], "%.3f" % dia[i].precio[-1], ha="left",size=8)  # PRECIO CIERRE

# print(data)
# data.plot()
show()





























#
#
#
# # data=data[~data.index.duplicated()]  ## quitar indices duplicados
#
# data[data.index.dayofweek < 5].plot()
# # data.plot()
# # data.plot()
# show()
