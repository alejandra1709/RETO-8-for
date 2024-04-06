#PUNTO 1
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
if __name__  == "__main__":
    print("LISTA DE NÚMEROS DEL 1 AL 100 CON SU RESPECTIVO CUADRADO") #Imprime el 'título' de la lista.
    for numero in range(1,101): #Ciclo que nos indica que para cada elemento 'numero', en el rango 1 a 100 (ya que el 101 no cuenta) se va a avanzar de uno en uno y se realizará...
        cuadrado:int=numero**2 #Se evalúa el cuadrado de 'numero'.
        print(numero,"-",cuadrado) #Se imprime tanto el número como su cuadrado, separado por un guión.