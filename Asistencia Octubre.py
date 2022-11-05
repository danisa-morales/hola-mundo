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

    
  
# Fernando Calisaya
class Aritmetica:
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    def sumar(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(49, 7)
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'la resta de los números es: {aritmetica1.resta()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La división de los números es: {aritmetica1.dividir():.2f}')
# ------------------------------------


# Facundo Pereyra 


class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
