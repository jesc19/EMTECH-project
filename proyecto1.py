#!/usr/bin/env python
# coding: utf-8

# # PROYECTO 1 EMTECH 

# Javier Emilio Salas Catonga , Septimebre 2020

# In[ ]:


from lifestore_file import *
productos=lifestore_products
busquedas=lifestore_searches
ventas=lifestore_sales

id_productos=[]
for producto in productos:
    id_productos.append(producto[0])
    
conjunto_datos=[busquedas, ventas]    


print('''¿Qué le gustaría conocer?

        1 top busquedas
        2 top 50 ventas
        
        ''')

consulta=int(input())

for datos in conjunto_datos:
    
    frecuencia_producto=[]
    
    for id_producto in id_productos:
        contador=0
        for tupla in datos:
            if (tupla[1]==id_producto):
                contador+=1
            else:
                contador+=0
        frecuencia_producto.append([contador, id_producto])

    
    if (consulta==1 and datos==busquedas):
        top_n_productos=96
        frecuencia_producto
        top_productos=sorted(frecuencia_producto, reverse=True)
        top_productos=top_productos[0:top_n_productos]
    
        top=0
        print('Lugar', '"Producto"', 'Cantidad')
        for tupla in top_productos:
            for producto in productos:
                if (producto[0]==tupla[1]):
                    top+=1
                    print(top,'"'+str(producto[1])+'"', tupla[0])
    elif(consulta==2 and datos==ventas):
        top_n_productos=50
        frecuencia_producto
        top_productos=sorted(frecuencia_producto, reverse=True)
        top_productos=top_productos[0:top_n_productos]
    
        top=0
        print('Lugar', '"Producto"', 'Cantidad')
        for tupla in top_productos:
            for producto in productos:
                if (producto[0]==tupla[1]):
                    top+=1
                    print(top,'"'+str(producto[1])+'"', tupla[0])  

