# Ejercicio 11: Agenda Telefonica
# Hacer un programa que simule una agenda de contactos.
# Crear un diccionario donde la clave sea el nombre del usuario
# y el valor sea el telefono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

agenda = {}
while True:
    print("\t.:MENÚ:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    print()
    opcion = int(input("Digite una opción de menú: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el número de teléfono: ")
        if opcion not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente!")
        else:
            print("Este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Se eliminó el contacto requerido")
        else:
            print("El contacto solicitado no existe en la agenda")
    elif opcion == 3:
        print("AGENDA DE CONTACTOS")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("La opción de menú ingresada no existe")
    print()


