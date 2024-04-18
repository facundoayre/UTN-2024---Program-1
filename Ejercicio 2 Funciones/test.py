#Ejercicio 1
'''
Ejercicio 01: Escribir una funcion que calcule el area de un circulo. La funcion debe recibir el radio como parametro y devolver el area.
'''

def calcular_area_circulo(radio):
    '''
    recibe el radio y retorna el area
    '''
    return 3.14 * (radio**2)

#Ejercicio 2
'''
Ejercicio 02: Escribir una funcion que verifique si un numero es par o impar. La funcion debe imprimir un mensaje indicando si el numero es par o impar.
'''

def verificacion_paridad(numero):
    if (numero % 2 == 0):
        print("El numero es par ")
    else:
        print("El numero es impar ")


#Ejercicio 3
'''
Ejercicio 03: Definir una funcion que encuentre el maximo de tres numeros. La funcion debe aceptar tres argumentos y devolver el numero mas grande.
'''

def maximo_tres_numeros(numero1,numero2,numero3):
    maximo = numero1
    if (numero2 > maximo):
        maximo = numero2
    
    if (numero3 > maximo):
        maximo = numero3

    return maximo




#Ejercicio 4
'''
Ejercicio 04: Diseñar una funcion que calcule la potencia de un numero. La funcion debe recibir la base y el exponente como argumentos y devolver el resultado.
'''

def calcular_potencia(base,exponente):
    return base ** exponente

'''
Nota: Todas las funciones deben estar probadas y se podra acceder a cada una de ellas mediante un menu de opciones.
'''

respuesta = 1

while(respuesta != 0):
    respuesta = int(input("Elija una opción: \n opcion 1: Calcular el area de un circulo\n opcion 2: Verificar la paridad de un numero\n opcion 3: Elegir maximo entre 3 numeros\n opcion 4: Calcular la potencia de un numero\n o ingrese 0 para salir: "))
    match(respuesta):
        case 0:
            print("Muchas gracias por usar nuestros servicios. ")

        case 1:
            radio = int(input("Ingrese el radio de un círculo: "))
            print(f"El área del circulo es de: {calcular_area_circulo(radio)}")
        case 2:
            numero = int(input("Ingrese un número: "))
            verificacion_paridad(numero)
        case 3:
            numero_uno = float(input("Ingrese el primer número: "))
            numero_dos =  float(input("Ingrese el segundo número: "))
            numero_tres = float(input("Ingrese el tercer número: "))

            print(f"El número máximo es: {maximo_tres_numeros(numero_uno, numero_dos, numero_tres)}")

        case 4:
            numero_base = int(input("Ingrese la base: "))
            numero_exponente = int(input("Ingrese el exponente: "))
            respuesta = calcular_potencia(numero_base,numero_exponente)

            print(f"La base es: {numero_base} y el exponente es: {numero_exponente} siendo así el resultado: {respuesta} ")