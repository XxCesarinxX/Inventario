import pandas as pd
from datetime import datetime

df=pd.read_csv("lista_de_precios.csv")
df2=pd.read_csv("inventa.csv")
sell=pd.read_csv("ventas.csv")

modelo=[]
color=[]
talla=[]
vendida =[]
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
dic_Venta.pop('Modelo')

df_Concatena = pd.DataFrame(dic_Venta, index=modelo)
save= pd.concat([sell,df_Concatena])
print(df_Concatena, "\ndf ventas\n", save)
