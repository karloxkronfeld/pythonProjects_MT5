import pandas as pd
from pylab import *
datos = pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\GER40Enero.csv")
datos.index = pd.DatetimeIndex(datos.time).strftime("%Y-%m-%d %H:%m:%s")
# print(datos)

datos.plot(rot=60)
show()