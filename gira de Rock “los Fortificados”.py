entradas_fortificados=[]
entradas_fortificados_puente_alto=[]
entradas_fortificados_muelle_baron_valpo=[]
entradas_fortificados_muelle_vergara_viña=[]
stock_fortificados=500
stock_fortificados_puente_alto=1300
stock_fortificados_muelle_baron_valpo=100
stock_fortificados_muelle_vergara_viña=50

def opcion_1():
    global stock_fortificados
    nombre=input("ingrese el nombre: ").lower()
    for existe in entradas_fortificados:
        if existe["nombre"]==nombre:
            print("este nombre ya existe")
            return
    codigo=input("ingrese el codigo de confirmacion: ")
    errores=False
    if len(codigo)<6:
        print("debe tener minimo 6 digitos")
        errores=True
    if not any(mayus.isupper() for mayus in codigo):
        print("debe tener al menos 1 letra mayuscula")
        errores=True
    if not any(numero.isdigit() for numero in codigo):
        print("debe tener al menos 1 numero")
        errores=True
    if errores:
        print("el codigo es incorrecto")
    else:
        print("se ha registrado su entrada")

        diccionario_fortificados={
            "nombre":nombre,
            "codigo":codigo
        }
        stock_fortificados-=1
        entradas_fortificados.append(diccionario_fortificados)
        print(f"quedan {stock_fortificados} entradas")

def opcion_2():
    global stock_fortificados_puente_alto
    nombre=input("ingrese el nombre: ").lower()
    for buscar in entradas_fortificados_puente_alto:
        if buscar ["nombre"]==nombre:
            print("este nombre ya esta registrado")
            return
    try:
        cantidad_entradas=int(input("ingrese la cantidad de entradas: "))
        if cantidad_entradas<0 or cantidad_entradas>3:
            print("solo se puede comprar entre 1 a 3 entradas por persona")
        else:
            print("se ha registrado con exito su entrada")
            diccionario_puente_alto={
                "nombre":nombre,
                "cantidad":cantidad_entradas
            }
            entradas_fortificados_puente_alto.append(diccionario_puente_alto)
            stock_fortificados_puente_alto-=1
            print(f"quedan {stock_fortificados_puente_alto} entradas")
    except ValueError:
        print("tiene que ingresar numeros enteros")

def opcion_3():
    global stock_fortificados_muelle_baron_valpo
    nombre=input("ingrese el nombre: ").lower()
    for buscar in entradas_fortificados_muelle_baron_valpo:
        if buscar["nombre"]==nombre:
            print("ese nombre ya existe")
            return
    codigo=input("ingrese el codigo de confirmacion: ")
    print("se ha registrado su entrada")
    diccionario_muelle_baron_valpo={
        "nombre":nombre,
        "codigo":codigo
    }
    entradas_fortificados_muelle_baron_valpo.append(diccionario_muelle_baron_valpo)
    stock_fortificados-=1
    print(f"quedan {stock_fortificados_muelle_baron_valpo} entradas")

def opcion_4():
    global stock_fortificados_muelle_vergara_viña
    nombre=input("ingrese el nombre: ")
    for buscar in entradas_fortificados_muelle_vergara_viña:
        if buscar["nombre"]==nombre:
            print("ese nombre ya existe")
            return
    tipo_entrada=input("seleccione tipo entrada Sun (sunset) o Ni (night): ").lower()
    if tipo_entrada=="sun":
        print("se ha seleccionado sun")
    elif tipo_entrada=="night":
        print("se ha seleccionado night")
    else:
        print("opcion invalida")
        return
    diccionario_viña={
        "nombre":nombre,
        "tipo_entrada":tipo_entrada
    }
    entradas_fortificados_muelle_vergara_viña.append(diccionario_viña)
    stock_fortificados_viña-=1
    print(f"quedan {stock_fortificados_muelle_vergara_viña} entradas")
def opcion_5():
    print("programa terminado...")

while True:
    print("""TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE
1.- Comprar entrada en Concepción.
2.- Comprar entrada en Puente Alto.
3.- Comprar entrada en Muelle Barón, Valparaíso.
4.- Comprar entrada en Muelle Vergara, Viña del Mar.
5.- Salir.
""")
    try:
        opcion=int(input("ingrese una opcion: "))
        if opcion <1 or opcion >5:
            print("opcion invalida")
            continue
    except ValueError:
        print("debes ingresar solo numeros enteros")
    if opcion == 1:
        if stock_fortificados<1:
            print("no tenemos stock")
        else:
            opcion_1()
    elif opcion == 2:
        if stock_fortificados_puente_alto<1:
            print("no tenemos stock")
        else:
            opcion_2()
    elif opcion == 3:
        if stock_fortificados_muelle_baron_valpo<1:
            print("no tenemos stock")
        else:
            opcion_3()
    elif opcion == 4:
        if stock_fortificados_muelle_vergara_viña<1:
            print("no tenemos stock")
        else:
            opcion_4()
    elif opcion == 5:
        opcion_5()

    