import statistics
import pandas as pd
from pylab import *


def hacer_grafico_OpenSea(data):
    moda = statistics.mode(data.precio)
    media = statistics.mean(data.precio)
    lista_dias = data.index.unique()

    dia=[] #Son todos los dias del mes separados cada uno en dataframes
    for x in range(len(lista_dias)):
        dia.append(data.loc[lista_dias[x],["precio"]])
    # print(len(dia))
    mensual=figure(figsize=(30,30),) #mensual es la figura que voy a llenar de graficas

    lista_maximos, lista_minimos, lista_promedios = [], [], []
    text(0, 0, "HOLA", color="r", ha="right",size=100)  # MAXIMO DEL DIA
    for i in range(0, len(dia)):
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
        mensual.tight_layout(pad=10.0)
        title(pd.to_datetime(lista_dias[i]).strftime("%d-%a"),size=10)

        plot(dia[i].values, color="k")

        text(0, maximo, "%.3f" % maximo, color="r", ha="right")  # MAXIMO DEL DIA
        hlines(maximo, 0, len(dia[i]), colors="r")
        text(0, minimo, "%.3f" % minimo, color="g", ha="right")  # MINIMO DEL DIA
        hlines(minimo, 0, len(dia[i]), colors="g")
        text(0, promedio, "%.3f" % promedio, color="b", ha="right")  # PROMEDIO DEL DIA
        hlines(promedio, 0, len(dia[i]), colors="b")

        # hlines(media,0,len(dia[i]),colors="white",ls=":")

        text(0, dia[i].precio[0], "%.3f" % dia[i].precio[0], ha="right",size=8)  # PRECIO APERTURA
        text(len(dia[i]), dia[i].precio[-1], "%.3f" % dia[i].precio[-1], ha="left",size=8)  # PRECIO CIERRE

    # print(data)
    # data.plot()
    show()


lista_archivos = ["EURUSDAbril.csv", "XAUUSDAbril.csv", "USDXAbril.csv", "USDJPYAbril.csv", "EURCHFAbril.csv", "USDCHFAbril.csv", "GBPJPYAbril.csv", "GER40Abril.csv", "NAS100Abril.csv", "US500Abril.csv", "BTCUSDAbril.csv", "ETHUSDAbril.csv"]
# lista_archivos = ["ETHUSDAbril.csv"]

for equis in lista_archivos:
    datos = pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\\" + equis)
    datos.index = pd.DatetimeIndex(datos.time).strftime("%Y-%m-%d")
    data=datos
    print(equis[:-4])
    hacer_grafico_OpenSea(data=data)




























