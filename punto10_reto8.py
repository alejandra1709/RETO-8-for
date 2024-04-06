#PUNTO 10
#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1],
#utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
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
