#Rodolfo Anibal ALtamirano Sánchez, A01377949
#Un programa que calcula el resiuo y cociete de una division,y que ve el mayor de una serie numerica


def dividir(mayor,menor):
    contador = 0
    while mayor > menor:
        mayor = mayor - menor
        contador = contador + 1
    return print(menor*contador+mayor,"/",menor, "=",contador, "sobra", mayor)


def encontrarMayor():
    def leer():
        numero = int(input("Teclea un numero [-1 para salir]: "))
        return numero

    def calcularMayor():
        numero = leer()
        numeroMayor = 0
        while numero != -1 and numero >= 0:
            if numero >= numeroMayor:
                numeroMayor = numero
            numero = leer()

        print("El mayor es", numeroMayor)

    calcularMayor()


def leerSelector():
    print("Misión 07. Ciclos while")
    print("Autor: Rodolfo Anibal Altamirano Sánchez")
    print("Matrícula: A01377949")
    print("1. Calcular divisiones")
    print("2. Enontrar el mayor")
    print("3. Salir")
    selector = int(input("Teclea tu opción: "))
    return selector

def main():
    selector = leerSelector()
    while selector !=3:
        if selector == 1:
            print()
            mayor = int(input("Dividendo: "))
            menor = int(input("Divisor: "))
            dividir(mayor, menor)
            print()

        elif selector== 2:
           print()
           encontrarMayor()
           print()

        elif selector <= 0 or selector > 3:
            print("ERROR, teclea 1, 2 o 3")
            print()
        selector = leerSelector()




main()
