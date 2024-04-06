#PUNTO 3
#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.
if __name__  == "__main__":
    num:int=int(input("Escriba un número ≥ 2: ")) #Se solicita un número 'num'.
    if num%2!=0: num-=1 #Si 'num' es impar se le resta 1 para obtener el número par inmediatamente anterior.
    for i in range(num,1,-2): print(i) #Ciclo que nos indica que para cada elemento 'i', en el rango 'num' a 1, disminuyendo de 2 en 2 (para obtener solo pares), se imprimirá 'i'.