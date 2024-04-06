#PUNTO 7
#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
if __name__  == "__main__":
    print("TABLAS DE MULTIPLICAR") #Se imprime el 'título'.
    for i in range(1,10,1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 10 (para llegar hasta 9), avanzando de uno en uno, se hará lo siguiente...
        print("Esta es la tabla del",i) #Se imprime el título individual de cada tabla.
        for j in range(1,11,1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 11 (para llegar hasta 10), avanzando de uno en uno, se hará lo siguiente...
            mult=i*j #Se multiplica el 'i' actual por cada 'j' y se guadra en 'mult'.
            print(i,"*",j,"=",mult) #Junto a un texto, se imprime cada 'mult'.
