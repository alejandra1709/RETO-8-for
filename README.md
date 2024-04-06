# RETO 8 - for
>***1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.***
```python
if __name__  == "__main__":
    print("LISTA DE NÚMEROS DEL 1 AL 100 CON SU RESPECTIVO CUADRADO") #Imprime el 'título' de la lista.
    for numero in range(1,101): #Ciclo que nos indica que para cada elemento 'numero', en el rango 1 a 100 (ya que el 101 no cuenta) se va a avanzar de uno en uno y se realizará...
        cuadrado:int=numero**2 #Se evalúa el cuadrado de 'numero'.
        print(numero,"-",cuadrado) #Se imprime tanto el número como su cuadrado, separado por un guión.
```
>***2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.***
```python
if __name__  == "__main__":
    print("NÚMEROS IMPARES 1 - 999") #Se imprime el 'título' de números impares.
    for n in range(1,1000,2): print(n) #Ciclo que nos indica que para cada elemento 'n', en el rango 1 a 999 (no incluye el 1000), se irá avanzando de dos en dos para solo tener los números impares y se irán imprimiendo.
    print("NÚMEROS PARES 2 - 1000") #Se imprime el 'título' de números pares.
    for m in range(2,1001,2): print(m) #Ciclo que nos indica que para cada elemento 'm', en el rango 2 a 1000 (no incluye el 1001), se irá avanzando de dos en dos para solo tener los números pares y se irán imprimiendo.
```
>***3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado***
```python
if __name__  == "__main__":
    num:int=int(input("Escriba un número ≥ 2: ")) #Se solicita un número 'num'.
    if num%2!=0: num-=1 #Si 'num' es impar se le resta 1 para obtener el número par inmediatamente anterior.
    for i in range(num,1,-2): print(i) #Ciclo que nos indica que para cada elemento 'i', en el rango 'num' a 1, disminuyendo de 2 en 2 (para obtener solo pares), se imprimirá 'i'.
```
>***4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial***
```python
if __name__  == "__main__":
    num:int=int(input("Escriba un número natural: ")) #Se solicita un número natural.
    for i in range(1,num+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'num', se irá avanzando de uno en uno y... 
        factorial : int = 1 #Se inicia la variable 'factorial' en 1.
        for j in range(1, i+1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 'i', se irá avanzando de uno en uno y...
            factorial *= j #La variable factorial se irá modificando, cada vez multiplicándoce por el atual 'j'.
        print(i,"-",factorial) #Se imprimen tanto el número 'i' el cual llegará hasta 'num' y al lado su respectivo factorial.
```
>***5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.***
```python
if __name__  == "__main__":
    num:int=int(input("Escriba la potencia n a la cual quiere elevar 2: ")) #Se solicita un número para la potencia n.
    pot : int = 1 #Se inicia la variable 'pot en 1.
    for i in range(1, num+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'num', aumentando de 1 en 1 ...
            pot *= 2 #Se multiplicará el actual 'pot' por 2.
    print("2 ^",num,"=",pot) #Se imprime 'pot'.
```
>***6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).***
```python
if __name__  == "__main__":
    n:int=int(input("Escriba un número natural: ")) #Se solicita un número natural.
    x:float=float(input("Escriba un número real: ")) #Se solicita un número real.
    pot:float=1 #Se inicializa la variable 'pot' en 1.
    for i in range(1, n+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 'n', aumentando de uno en uno...
            pot *= x #Cada vez que se pase por acá, 'pot' se irá multiplicando por 'x'.
    print(pot) #Se imprime el 'pot' final.
```
>***7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.***
```python
if __name__  == "__main__":
    print("TABLAS DE MULTIPLICAR") #Se imprime el 'título'.
    for i in range(1,10,1): #Ciclo que nos indica que para cada elemento 'i', en el rango 1 a 10 (para llegar hasta 9), avanzando de uno en uno, se hará lo siguiente...
        print("Esta es la tabla del",i) #Se imprime el título individual de cada tabla.
        for j in range(1,11,1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 11 (para llegar hasta 10), avanzando de uno en uno, se hará lo siguiente...
            mult=i*j #Se multiplica el 'i' actual por cada 'j' y se guadra en 'mult'.
            print(i,"*",j,"=",mult) #Junto a un texto, se imprime cada 'mult'.
```
>***8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.***
```python
import math #Se importa math para usar función exp() y verificar valor.
def factorial (i:int) ->int: #Función para calcular el factorial, recibe entero y entrega entero.
    fact=1 #Se inicia variable 'fact' en 1.
    for j in range(1,i+1,1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 'i' de uno en uno, se hará...
        fact*=j #Se multiplica 'fact' por 'j' y se guarda el nuevo valor en 'fact'
    return fact #Se devuelve el valor de 'fact' final.
def exponencial (x:float,n:int) ->float: #Función para calcular el valor de la función exponencial aproximado.
    exex=0 #Se inicia la variable 'exex' en 0.
    for i in range(0,n+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 0 a 'n' de uno en uno, se hará...
        ex=(x**i)/(factorial(i)) #En la variable 'ex' se realiza la ecuación para el valor 'i' que se tiene.
        exex+=ex #Se suma 'ex' al actual 'exex' y se guarda este nuevo valor en 'exex'.
    return(exex) #se devuelve 'exex'.
if __name__  == "__main__":
    x:float=float(input("ingrese el valor de x al que quiere calcular la función exponencial: ")) #Se solicita el exponente.
    n:int=int(input("¿Hasta qué término de la serie de Maclaurin desea utilizar? ")) #Se solicita la cantidad de términos que se desean usar.
    aproximacion=exponencial(x,n) #Se evalúa el valor aproximado con la función exponencial(), enviando como argumentos x y n.
    valor_real=math.exp(x) #Se calcula el valor real con la función exp() de math.
    print("El valor aproximado es:",aproximacion) #Se imprime el valor aproximado.
    print("El valor real es:",valor_real) #Se imprime el valor real.
    dif=valor_real-aproximacion #Se calcula la diferenecia entre los valores.
    print("La diferencia entre el valor real y el aproximado es de:",dif) #Se imprime la diferencia.
    porcentaje=((aproximacion-valor_real)/valor_real)*100 #Se calcula el porcentaje de error.
    if porcentaje<=0: porcentaje=-porcentaje #Si el porcentaje es negativo, se multiplica por menos para que dé positivo.
    print("El porcentaje de error del valor aproximado es de:",porcentaje,"%") #Se imprime el porcentaje de error.
    error_pedido:float=0.1 #Error máximo solicitado.
    while True: #Ciclo mientras.
        if porcentaje<error_pedido:  #Si el porcentaje de error es menor a 0.1...
            print ("El número de términos para que dé un error menor a 0.1% es de:",n) #Se imprime el número de términos que se usaron.
            break #Se sale del while.
        else: n+=1 #Sino se suma uno a los términos y se evalúa de nuevo.
```
>***9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.***
```python
import math #Se importa math para usar función exp() y verificar valor.
def factorial (i:int) ->int: #Función para calcular el factorial, recibe entero y entrega entero.
    fact=1 #Se inicia variable 'fact' en 1.
    for j in range(1,i+1,1): #Ciclo que nos indica que para cada elemento 'j', en el rango 1 a 'i' de uno en uno, se hará...
        fact*=j #Se multiplica 'fact' por 'j' y se guarda el nuevo valor en 'fact'
    return fact #Se devuelve el valor de 'fact' final.
def seno (x:float,n:int) ->float: #Función para calcular el valor de la función seno aproximado.
    sen=0 #Se inicia la variable 'sen' en 0.
    for i in range(0,n+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 0 a 'n' de uno en uno, se hará...
        denom=2*i+1 #Variable con los elementos del denominador.
        senn=((-1)**i)*((x**denom)/(factorial(denom))) #En la variable 'senn' se realiza la ecuación para el valor 'i' que se tiene.
        sen+=senn #Se suma 'senn' al actual 'sen' y se guarda este nuevo valor en 'sen'.
    return(sen) #se devuelve 'sen'.
if __name__  == "__main__":
    x:float=float(input("ingrese el valor de x al que quiere calcular la función senoidal: ")) #Se solicita el ángulo.
    n:int=int(input("¿Hasta qué término de la serie de Maclaurin desea utilizar? ")) #Se solicita la cantidad de términos que se desean usar.
    aproximacion=seno(x,n) #Se evalúa el valor aproximado con la función seno(), enviando como argumentos x y n.
    valor_real=math.sin(x) #Se calcula el valor real con la función sin() de math.
    print("El valor aproximado es:",aproximacion) #Se imprime el valor aproximado.
    print("El valor real es:",valor_real) #Se imprime el valor real.
    dif=valor_real-aproximacion #Se calcula la diferenecia entre los valores.
    print("La diferencia entre el valor real y el aproximado es de:",dif) #Se imprime la diferencia.
    porcentaje=((aproximacion-valor_real)/valor_real)*100 #Se calcula el porcentaje de error.
    if porcentaje<=0: porcentaje=-porcentaje #Si el porcentaje es negativo, se multiplica por menos para que dé positivo.
    print("El porcentaje de error del valor aproximado es de:",porcentaje,"%") #Se imprime el porcentaje de error.
```
>***10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.***
```python
import math #Se importa math para usar función atan() y verificar valor.
def arctan (x:float,n:int) ->float: #Función para calcular el valor de la función arcotangente aproximado.
    atan=0 #Se inicia la variable 'sen' en 0.
    for i in range(0,n+1): #Ciclo que nos indica que para cada elemento 'i', en el rango 0 a 'n' de uno en uno, se hará...
        denom=2*i+1 #Variable con los elementos del denominador.
        tanarc=((-1)**i)*((x**denom)/(denom)) #En la variable 'tanarc' se realiza la ecuación para el valor 'i' que se tiene.
        atan+=tanarc #Se suma 'tanarc' al actual 'atan' y se guarda este nuevo valor en 'atan'.
    return(atan) #se devuelve 'atan'.
if __name__  == "__main__":
    x:float=float(input("ingrese el valor de x al que quiere calcular la función arcotangente: ")) #Se solicita el ángulo.
    n:int=int(input("¿Hasta qué término de la serie de Maclaurin desea utilizar? ")) #Se solicita la cantidad de términos que se desean usar.
    aproximacion=arctan(x,n) #Se evalúa el valor aproximado con la función arctan(), enviando como argumentos x y n.
    valor_real=math.atan(x) #Se calcula el valor real con la función atan() de math.
    print("El valor aproximado es:",aproximacion) #Se imprime el valor aproximado.
    print("El valor real es:",valor_real) #Se imprime el valor real.
    dif=valor_real-aproximacion #Se calcula la diferenecia entre los valores.
    print("La diferencia entre el valor real y el aproximado es de:",dif) #Se imprime la diferencia.
    porcentaje=((aproximacion-valor_real)/valor_real)*100 #Se calcula el porcentaje de error.
    if porcentaje<=0: porcentaje=-porcentaje #Si el porcentaje es negativo, se multiplica por menos para que dé positivo.
    print("El porcentaje de error del valor aproximado es de:",porcentaje,"%") #Se imprime el porcentaje de error.
```
