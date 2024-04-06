#Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real),
#utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia
#entre el valor real y la aproximación.
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
