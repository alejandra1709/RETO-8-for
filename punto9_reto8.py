#PUNTO 9
#Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), 
#utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
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
