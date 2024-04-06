#PUNTO 4
#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.
if __name__  == "__main__":
    num:int=int(input("Escriba un número natural: ")) #Se solicita un número natural.
    for i in range(1,num+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'num', se irá avanzando de uno en uno y... 
        factorial : int = 1 #Se inicia la variable 'factorial' en 1.
        for j in range(1, i+1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 'i', se irá avanzando de uno en uno y...
            factorial *= j #La variable factorial se irá modificando, cada vez multiplicándoce por el atual 'j'.
        print(i,"-",factorial) #Se imprimen tanto el número 'i' el cual llegará hasta 'num' y al lado su respectivo factorial.