#PUNTO 5
#Calcular el valor de 2 elevado a la potencia n usando ciclos for.
if __name__  == "__main__":
    num:int=int(input("Escriba la potencia n a la cual quiere elevar 2: ")) #Se solicita un número para la potencia n.
    pot : int = 1 #Se inicia la variable 'pot en 1.
    for i in range(1, num+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'num', aumentando de 1 en 1 ...
            pot *= 2 #Se multiplicará el actual 'pot' por 2.
    print("2 ^",num,"=",pot) #Se imprime 'pot'.