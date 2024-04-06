#PUNTO 6
#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
if __name__  == "__main__":
    n:int=int(input("Escriba un número natural: ")) #Se solicita un número natural.
    x:float=float(input("Escriba un número real: ")) #Se solicita un número real.
    pot:float=1 #Se inicializa la variable 'pot' en 1.
    for i in range(1, n+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'n', aumentando de uno en uno...
            pot *= x #Cada vez que se pase por acá, 'pot' se irá multiplicando por 'x'.
    print(pot) #Se imprime el 'pot' final.