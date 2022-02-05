import pandas as pd

ACTIVOS=["EURUSD","XAUUSD","USDX","USDJPY","USDCHF","GBPJPY","GER40","NAS100","US500","BTCUSD","ETHUSD"]

for acti in ACTIVOS:
    ACTIVO=pd.read_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\\"+acti+"Enero.csv").set_index("time")
    ACTIVO.index=pd.DatetimeIndex(ACTIVO.index).strftime( "%Y-%m-%d %H:%M:%S")
    ACTIVO = ACTIVO[~ACTIVO.index.duplicated(keep='first')]
    ACTIVO=ACTIVO['2022-01-01':'2022-01-31']
    ACTIVO.to_csv(r"C:\Users\Personal\Downloads\pythonProjects_MT5\LeerDatosFromMT5\\"+acti+"Enero.csv")
    print(acti,"   hecho",end="\r")
    print(ACTIVO)



# datos = pd.read_csv(r"C:\Users\Personal\Downloads\PRojectosPython\BasesDeDatos(conScript)\\" + equis).set_index("time")
# datos.index = pd.DatetimeIndex(datos.index).strftime("%Y-%m-%d")