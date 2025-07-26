def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    return cadena[-1] + invertir_cadena(cadena[:-1])

def suma_n(numero):
    if numero == 0:
        return 0
    return numero + suma_n(numero - 1)

def cuenta(numero):
    if numero == 0:
        return 0
    return f"{numero} {cuenta(numero - 1)}"

def suma_digitos(numero):
    if len(numero) == 0:
        return 0
    temp = int(numero[0])
    return temp + suma_digitos(numero[1:])



while True:
    print("\n==== MENU DE RECURSIVIDAD ====")
    print("1. Invertir cadena de texto")
    print("2. Calcular la suma de los primeros N numeros naturales")
    print("3. Cuenta regresiva desde N hasta 1")
    print("4. Sumar los digitos de un numero")
    print("5. Contar los digitos de un numero")
    print("6. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        cadena_ingreso = input("Ingrese una cadena de texto: ")
        print(f"Resultado: {invertir_cadena(cadena_ingreso)}")

    elif opcion == "2":
        num = int(input("Ingrese un numero: "))
        print(f"Resultado: {suma_n(num)}")

    elif opcion == "3":
        num = int(input("Ingrese un numero: "))
        print(f"Resultado: {cuenta(num)}")

    elif opcion == "4":
        num = input("Ingrese un numero: ")
        print(f"Resultado: {suma_digitos(num)}")

    elif opcion == "5":
