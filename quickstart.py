import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import datetime

#*/-------------------credenciales------------------------/'''
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = r"C:\Users\cesar\OneDrive\Documentos\noEntrar\key.json" 
SPREADSHEET_ID = {
    "inventarioGuerrero" :'1NiiceNHdvZxlXNjgpC3k_droC_S4Mh5xbS-lMqGktCw',
    "ListasDePrecios"    :'1AwlS1NxhRBKn-G_vaiOBmPKW0AVnvQ6DDwb1ZJAYfRA',
    "HistorialdeCompras" :'1RlDAkYJCeFAq-mMrLwrzshcXxpHeVTj3rvq1EeGqD4E'}
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
#*/------------------------------------------------------/'''
listCantidad = [1,1,1,1]
listModelo   = ["Abraham","Alejandra","Alejandra","TopGun"]
listColor    = ["Cafe","Negro", "Cafe", "Cafe"]
listTalla    = ["2Xl","Xl","L","L"]
listPrecio   = ["1500","1500","1500","1500",]
dicVentas    = {
    "Cantidad": listCantidad,
    "Modelo"  : listModelo,
    "Color"   : listColor,
    "Talla"   : listTalla,
    "Precio"  : listPrecio
}

def leer(hoja,nombreID):
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID[nombreID],
        range= hoja # poner en rango el nombre de la hoja manda toda informacion
    ).execute()
    values = result.get('values',[])
    # Reemplazar los espacios en blanco por nulos
    values = [[None if x == '' else x for x in row] for row in values]
    df = pd.DataFrame(values[1:], columns=values[0])
    
    columnas_a_convertir = ["S", "M", "L", "Xl", "2Xl", "3Xl", "5Xl"]
    # Itera a través de las columnas y convierte su tipo de dato a int64
    for columna in columnas_a_convertir:
        # Reemplaza los valores None por 0 en las columnas especificadas
        df[columnas_a_convertir] = df[columnas_a_convertir].fillna(0)
        # Convierte las columnas al tipo de dato int64
        df[columna] = df[columna].astype('int64')

    return df

def interaccion():
    n_Ventas= int(input(" vendPrendasidas?:\n-->"))
    for x in range(n_Ventas):
        print(x+1, "de producto\n") #enumeracion de productos
        for i in dicVentas:
            print(f"{i}:", end=" ") #recorriendo diccionario
            aux = input('')
            aux=aux.capitalize()
            dicVentas[i].append(aux)     
    return dicVentas

def search():
    dfInventario = leer("InventarioG" ,"inventarioGuerrero")
    #depende de la libreria pandas
    busqueda = input("Introduce:\n+________+________+\n| Modelo | Talla |\n+--------+--------+\n| ").title()
    busqueda = busqueda.split()
    print(busqueda)
    #filtra las filas que cumplen con las condiciones
    filtro = (dfInventario['Modelo'] == busqueda[0]) & (dfInventario[busqueda[1]] > 0)
    #una vez filtrado por lo que buscamos solo implementamos los datos que interesan
    resultado = dfInventario.loc[filtro, ["Modelo", "Color", busqueda[1]]]
    return resultado

def decrementacion(dFrame, dicci):
    for i in range(len(dicci["Modelo"])):
        aux = dFrame.loc[(dFrame['Modelo'] == dicci["Modelo"][i]) & (dFrame['Color'] == dicci["Color"][i]), dicci["Talla"][i]].astype(int)
        aux-=1
        dFrame.loc[(dFrame['Modelo'] == dicci["Modelo"][i]) & (dFrame['Color'] == dicci["Color"][i]), dicci["Talla"][i]]=aux

def incrementacion(dFrame, dicci):
    for i in range(len(dicci["Modelo"])):
        aux = dFrame.loc[(dFrame['Modelo'] == dicci["Modelo"][i]) & (dFrame['Color'] == dicci["Color"][i]), dicci["Talla"][i]].astype(int)
        aux+=1
        dFrame.loc[(dFrame['Modelo'] == dicci["Modelo"][i]) & (dFrame['Color'] == dicci["Color"][i]), dicci["Talla"][i]]=aux


def subir(hoja,listados,nombreID):
    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID[nombreID],
        range=hoja,  
        valueInputOption='USER_ENTERED',
        body={'values': listados}
    ).execute()
    
def subirFila(hoja,fila,nombreID):
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID[nombreID],
        range=hoja,  
        valueInputOption='USER_ENTERED',
        body={'values': fila}
    ).execute()

def listado(dataf):
    if isinstance(dataf, dict):
        # Si es un diccionario, conviértelo en un DataFrame
        df = pd.DataFrame(dataf)
        dataf = df
    
    encabezado =  dataf.columns.tolist()
    filas      = dataf.values.tolist()
    listas = [encabezado] + filas
    return listas

def listaprecios():
    df=leer("Hoja 1","HistorialdeCompras")
    print(df)

def listaveticaldic():
    listas=[]
    for i in range(len(listCantidad)):
        aux=[]
        for value in dicVentas.values():
            aux.append(value[i])      
        listas.append(aux)
    return listas
        
def consecuenciaVenta():
    """------------------------decrementacion-------------------------------"""
    df = leer("InventarioG","inventarioGuerrero")
    decrementacion(df,dicVentas)
    print(df)
    """------------------------HistorialdeCompras-------------------------------"""
    
    """-------------------------solicitar--------------------------------"""
    dicVentas.pop("Precio")
    subir("SolicitaG",listado(dicVentas),"inventarioGuerrero")

def pedidos():

    peticion  = input("\n--Separado por COMAS--\n| Modelo | Talla | Color | Peticion | Numero | Nombre | Acuenta | Costo |\n")
    peticion  = list(peticion.split(","))
    resultado = {
        "Fecha"   :  datetime.today().strftime('%Y-%m-%d %H:%M'),
        "Modelo"  : peticion[0],
        "Talla"   : peticion[1],
        "Color"   : peticion[2],
        "Peticion": peticion[3],
        "Numero"  : peticion[4],
        "Nombre"  : peticion[5],
        "Acuenta" : peticion[6],
        "Resta"   : int(peticion[7]) - int(peticion[6]),
        "Estado"  : "Pedido"
    }
    fila = [] + [list(resultado.values())]
    subirFila("PedidosG",fila,"inventarioGuerrero")

while True:
    opcion = input("\nElija una opcion\n1.-Anotar Ventas\n2.-Buscar\n3.-Salir\n> ")

    if opcion =="1":
        consecuenciaVenta()


    elif opcion=="2":
        print(search())
    
    elif opcion=="3":
        print("Saliendo...")
        break
    else: 
        print("XXXXXXXX\tLa opcion que solicitas no es valida\tXXXXXXXX")