#Ejercicio 1
#Dado el siguiente diccionario:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
#Realiza las siguientes acciones:
#Añade una clave al inventario llamada ‘pocket’.
#Establece el valor de ‘pocket’ para que sea una lista de las cadenas ‘seashell’, ‘strange berry’
#y ‘lint’.
#Ordena los elementos en la lista almacenada en la clave ‘backpack’.
#Elimina ‘dagger’ de la lista de elementos almacenados en la calve ‘backpack’.
#Añádele 50 al número almacenado en la clave ‘gold’
cadena=('seashell' , 'strange berry' , 'lint')
inventory['pocket']=cadena
print(inventory)
cadenaordenada=cadena
cadenaordenada.short()
inventory['backpack']=cadenaordenada
print (cadenaordenada)
print (inventory)
