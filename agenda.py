agenda={}
agendacontactos=[]
numcontactos=int(input("Cuantos contactos quieres añadir: "))
for contactos in range (numcontactos):
	agenda={}
	nombre=input("Introduce el nombre: ")
	agenda['nombre']=nombre
	numero=int(input("Dime el numero de telefono: "))
	agenda['telefono']=numero
	print ("A continuación puede insertar campos adicionales, introduzca 1 o 2")
	seguir=int(input("1 para seguir, 2 para finalizar: "))
	while seguir != 2:
		nombre1=input("Dime el nombre del campo: ")
		valor1=input("Valor del campo: ")
		agenda[nombre1]=valor1
		seguir=int(input("1 para seguir, 2 para finalizar: "))
	agendacontactos.append(agenda)
print (agendacontactos)