'''La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante. OK
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.'''

bandera_primero_barbijo = True
precio_barbijo_mas_caro = 0
fabricante_barbijo_mas_caro = ""
cantidad_unidades_mas_caro = 0
fabricante_mayor_cantidad = ""
tipo_mas_fabricado = ""
acumuladorJabon = 0


for i in range (2):
    tipo_Ingresado = input("Ingrese el tipo de producto. ")
    tipo_Ingresado = tipo_Ingresado.lower()

    while (tipo_Ingresado != 'barbijo' and tipo_Ingresado != 'jabon' and tipo_Ingresado != 'alcohol'):
        tipo_Ingresado = input("Reingrese un tipo de producto valido. ")


    precio_Ingresado = float(input("Ingrese el precio del producto. "))

    while (precio_Ingresado < 100 or precio_Ingresado > 300):
        precio_Ingresado = float(input("Reingrese un precio entre 100 y 300. "))


    cantidad_Ingresada = int(input("Ingrese la cantidad del producto. "))

    while (cantidad_Ingresada <= 0 or cantidad_Ingresada > 1000):
        cantidad_Ingresada  = int(input("Reingrese una cantidad valida. "))


    marca_Ingresada = input("Ingrese la marca del producto. ")

    fabricante_Ingresado = input("Ingrese el fabricante del producto. ")

    if (tipo_Ingresado == "barbijo"):
        if(bandera_primero_barbijo == True or precio_Ingresado > precio_barbijo_mas_caro):
            precio_barbijo_mas_caro = precio_Ingresado
            fabricante_barbijo_mas_caro = fabricante_Ingresado
            cantidad_unidades_mas_caro = cantidad_Ingresada
            bandera_primero_barbijo = False
    elif(tipo_Ingresado == "jabon"):
        acumuladorJabon = acumuladorJabon + cantidad_Ingresada

    if(i == 0 or maxima_Cantidad < cantidad_Ingresada):
        maxima_Cantidad = cantidad_Ingresada
        tipo_mas_fabricado = tipo_Ingresado
        fabricante_mayor_cantidad= fabricante_Ingresado

   


if(bandera_primero_barbijo == True):
    print("No se ingresaron barbijos")
else:
    print(f"El mas caro de los barbijos tiene una cantidad de {cantidad_unidades_mas_caro} unidades y es fabricado por: {fabricante_barbijo_mas_caro}")

print(f"El item con mas unidades es {tipo_mas_fabricado} y su fabricante es: {fabricante_mayor_cantidad}")

if(acumuladorJabon == 0):
    (print("No se ingresaron jabones"))
else:
    print(f"La cantidad de jabones es: {acumuladorJabon}")
    