import pandas as pd

listCantidad, listModelo, listColor, listTalla, listPrecio =[1,1] ["Saul","Nancy"],["Negro", "Cafe"],["Xl","L"],["1500","1500"]
dicVentas={
    "Cantidad": listCantidad,
    "Modelo"  : listModelo,
    "Color"   : listColor,
    "Talla"   : listTalla,
    "Precio"  : listPrecio
}
def interaccion():
    n_Ventas= int(input("Prendas vendidas?:\n-->"))
    for x in range(n_Ventas):
        bandera=[]
        print(x+1, "de producto\n") #enumeracion de productos
        for i in dicVentas:
            print(f"{i}:", end=" ") #recorriendo diccionario
            aux = input('')
            aux=aux.capitalize()
            if aux not in dicVentas[i]:
            #si no esta repetida se agrega a la lista
                dicVentas[i].append(aux)
            else:
            #SI se repite agregamos una bandera 
                bandera.append(True)
        
    return dicVentas

def search():
    #depende de la libreria pandas
    busqueda=input("Introduce Modelo y Talla \n-->").title()
    busqueda=busqueda.split(" ")
    respuesta = dfInvetnario.loc[busqueda[0],
    ("Color", busqueda[1])]
    return respuesta

def eliminar():
#eliminar es una reaccion de vender
    dicVentas

dfVentas = pd.DataFrame(dicVentas,
# filas el producto y en columnas los parametros
index   = dicVentas["Modelo"], 
columns = ["Color","Talla","Precio"])

dfInvetnario = pd.read_csv("inventario.csv",
index_col = "Modelo")

respuesta = search()

print ("\n\t\t --DataFrame del Diccionario--\n", dfVentas)
print("\n\t\t --DataFrame del Inventario--\n"  , dfInvetnario)
print("\n\t\t --DataFrame de la Busqueda--\n"  , respuesta)

