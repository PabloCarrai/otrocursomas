from funciones_aritmeticas import sumar, restar, multiplicar, dividir


def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")


def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input("Escriba la operacion a Ejecutar:  "))
                break
            except TypeError as e:
                print(f"Error {e}, ha digitado un valor invalido")
        print()
        if opcion == 0:
            break
        elif 1 <= opcion <= 4:
            while True:
                try:
                    numero_1 = int(input("Escriba el numero 1:  "))
                    break
                except TypeError as e:
                    print(f"Error {e}, ha digitado un valor invalido")

            while True:
                try:
                    numero_2 = int(input("Escriba el numero 2:  "))
                    break
                except TypeError as e:
                    print(f"Error {e}, ha digitado un valor invalido")

        elif opcion == 1:
            resultado = sumar(numero_1, numero_2)
        elif opcion == 2:
            resultado = restar(numero_1, numero_2)
        elif opcion == 3:
            resultado = multiplicar(numero_1, numero_2)
        elif opcion == 4:
            try:
                resultado = dividir(numero_1, numero_2)
            except ZeroDivisionError as e:
                print(f"Error {e}")

    print()
    print("El programa ha terminado ")
