import pandas as pd

datos = pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\GER40Enero.csv")
datos.index = pd.DatetimeIndex(datos.time).strftime("%Y-%m-%d")
print(datos)