import pandas as pd
from datetime import datetime

df=pd.read_csv("inventa.csv")
sell=pd.read_csv("ventas.csv")

modelo=[]             #       son listas 
color=[]              #       vacias
talla=[]                #       para el
vendida =[]             #       dicccionario 
dic_Venta= {                        #                       Columnas(key)
#    key     : value                    _________________________________________________
    "Modelo" : modelo,          # F (V) |  Modelo   | Color | Talla | Precio | Ganancia | 
    "Color"  : color,           # i (a) |___________|_______|_______|________|__________|
    "Talla"  : talla,           # l (l) | Italiano  | Negro | XL    | 1500   | 500      |
    "Precio" : vendida          # a (u) |___________|_______|_______|________|__________|
}

n_Ventas=int(input("Numero de prendas vendidas:\n"))
for i in range(n_Ventas):
    print(f"/*-----------{i+1}-----------*/")
    for key in dic_Venta:
        print(key)
        aux=input("-->")
        dic_Venta[key].append(aux)
df_Dicc = pd.DataFrame(dic_Venta)#el diccionario lo hace df
#union = pd.concat([sell,df_Dicc])#junta el df de almacen con el dfdiccionario guardandolo en la bariable 
#union.set_index("Modelo") #indexa el df con la columna del parametro
print(df_Dicc)#, "\ndf ventas\n", union)
#print(union.loc[['saul'],['Talla']])
#df.fillna(0, inplace=True) llena las filas NaN a 0