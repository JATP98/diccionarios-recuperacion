
#Ejercicio 1
#Dado el siguiente diccionario:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
ordenar=[]
#Realiza las siguientes acciones:
#Añade una clave al inventario llamada ‘pocket’.
#Establece el valor de ‘pocket’ para que sea una lista de las cadenas ‘seashell’, ‘strange berry’
#y ‘lint’.
#Ordena los elementos en la lista almacenada en la clave ‘backpack’.
#Elimina ‘dagger’ de la lista de elementos almacenados en la calve ‘backpack’.
#Añádele 50 al número almacenado en la clave ‘gold’
cadena=('seashell' , 'strange berry' , 'lint')
inventory['pocket']=cadena
print("cadena añadida ", inventory)
print("")
inventory['backpack'].sort()
print ("lista ordenada ", inventory['backpack'])
print("")
inventory['backpack'].remove('dagger')
print("dagger borrado ", inventory)
print("")
listaparagold=[500, 50]
inventory['gold']=listaparagold
print("50 añadido a lista gold", inventory)
print("")
