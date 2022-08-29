#>> CUIDADO modificar el mes linea 8, 11 y 12

import pandas as pd

ACTIVOS=["EURUSD","XAUUSD","USDX","USDJPY","USDCHF","EURCHF","GBPJPY","GER40","NAS100","US500","BTCUSD","ETHUSD"] ##para todos

for acti in ACTIVOS:
    ACTIVO=pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\\"+acti+"Mayo.csv").set_index("time") #MODIFICAR >>>>>>>>>>>>>
    ACTIVO.index=pd.DatetimeIndex(ACTIVO.index).strftime( "%Y-%m-%d %H:%M:%S")
    ACTIVO = ACTIVO[~ACTIVO.index.duplicated(keep='first')]
    ACTIVO=ACTIVO['2022-05-01':'2022-05-31'] # MODIFICAR  >>>>>>>>>>>>>>>>>>>>>>>>>>> cambiar el mes!!!
    ACTIVO.to_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\\"+acti+"Mayo.csv")   ##MODIFICAR >>>>>>>>>>>>>
    print(acti,"   hecho",end="\r")
    print(ACTIVO)



# datos = pd.read_csv(r"C:\Users\Personal\Downloads\PRojectosPython\BasesDeDatos(conScript)\\" + equis).set_index("time")
# datos.index = pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")