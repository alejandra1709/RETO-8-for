#RETO 2
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
if __name__  == "__main__":
    print("NÚMEROS IMPARES 1 - 999") #Se imprime el 'título' de números impares.
    for n in range(1,1000,2): print(n) #Ciclo que nos indica que para cada elemento 'n', en el rango 1 a 999 (no incluye el 1000), se irá avanzando de dos en dos para solo tener los números impares y se irán imprimiendo.
    print("NÚMEROS PARES 2 - 1000") #Se imprime el 'título' de números pares.
    for m in range(2,1001,2): print(m) #Ciclo que nos indica que para cada elemento 'm', en el rango 2 a 1000 (no incluye el 1001), se irá avanzando de dos en dos para solo tener los números pares y se irán imprimiendo.