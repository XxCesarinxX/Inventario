import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import datetime

#*/-------------------credenciales------------------------/'''
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = r"C:\Users\cesar\OneDrive\Documentos\noEntrar\key.json" 
SPREADSHEET_ID = '1NiiceNHdvZxlXNjgpC3k_droC_S4Mh5xbS-lMqGktCw'
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

def search(inve):
    dfInvetnario = leer(inve)
    #depende de la libreria pandas
    busqueda = input("Introduce:\n+________+________+\n| Modelo | Talla |\n+--------+--------+\n| ").title()
    busqueda = busqueda.split()
    respuesta = dfInvetnario.loc[busqueda[0],
    ("Color", busqueda[1])]
    print(respuesta)
    return respuesta

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

def leer(hoja):
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range= hoja # poner en rango el nombre de la hoja manda toda informacion
    ).execute()
    values = result.get('values',[])
    # Reemplazar los espacios en blanco por nulos
    values = [[None if x == '' else x for x in row] for row in values]
    df = pd.DataFrame(values[1:], columns=values[0])
    return df

def subir(hoja,listados):
    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=hoja,  
        valueInputOption='USER_ENTERED',
        body={'values': listados}
    ).execute()
    
def subirFila(hoja,fila):
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=hoja,  
        valueInputOption='USER_ENTERED',
        body={'values': fila}
    ).execute()

def consecuenciaVenta():
    """------------------------decrementacion-------------------------------"""
    df = leer("InventarioG")
    decrementacion(df,dicVentas)
    print(df)
    """-------------------------solicitar--------------------------------"""
    dicVentas.pop("Precio")
    listas=[]
    for i in range(len(listCantidad)):
        aux=[]
        for value in dicVentas.values():
            aux.append(value[i])      
        listas.append(aux)
    subirFila("SolicitaG",listas)
        
def inventario(hoja):
    df = leer(hoja)
    incrementacion(df, dicVentas)

def listado(dataf):
    encabezado,  filas = dataf.columns.tolist(),dataf.values.tolist()
    listas = [encabezado] + filas
    return listas

def listaprecios():
    SPREADSHEET_ID="1AwlS1NxhRBKn-G_vaiOBmPKW0AVnvQ6DDwb1ZJAYfRA"
    df=leer("ListaPre")
    print(df)

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
    subirFila("PedidosG",fila)

consecuenciaVenta()