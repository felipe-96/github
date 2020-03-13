<<<<<<< HEAD
#integrantes :  Hola
=======
#integrantes : buen dia
>>>>>>> 3ecf4036f0078e4461b2a5dd16af502b05323b76

#Declaracion de funciones:
def media_x(l):#La funcion de moda recibe como parametro de entrada una lista "l"
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia. La funcion len() devuelve el largo de la lista.
        suma = 0.0 #Se inicia la variable "suma" en 0, esta almacenara la suma de datos de la lista "l"
        for i in l:#Se comienza el recorrido de la lista "l" siendo "i" un elemento de la lista
            suma = suma + i #Se suma el elemento de la lista a la variable "suma"
        cantidad = len(l) #La funcion len(l) determina el tamano de la lista, es decir, la cantidad de datos que se sumaron para obtener el promedio
        media = suma/cantidad #Se obtiene la media a traves del cuociente entre la suma de los elementos y la cantidad de elementos
        return media #La funcion retorna el valor de la media de la lista "l"
    else: #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo
        return "La lista esta vacia"



def moda_x(l): #Esta funcion recibe como datos de entrada una lista con elementos
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia
        elemento = [] #Esta lista guardara aquellos elemento que compartan la moda debido a que tienen igual cantidad de repeticiones en la lista
        contador = 0 #Representa la cantidad de presencias que tiene el(los) elemento(s)  moda(s) en la lista
        for i in l: #Se recorre la lista y se cuenta la cantidad de repeticiones que presenta un elemento en la lista gracias a la funcion .count() 
            aux = l.count(i)
            if aux > contador:# Si el contador del elemento en revision es mayor al elemento guardado anteriormente como mas repetido, entonces se esta en presencia de una nueva moda
                elemento = [] # Al tratarse de una nueva moda se vacia la lista de elementos anteriormente reconocidos como modas
                contador = aux # Se actualiza la la cantidad de repeticiones de la nueva moda
                elemento.append(i) #Se agrega el elemento de la moda a una lista de elemento que compartan el "titulo" de moda
            elif (aux == contador): #Si se encuentra un elemento con igual cantidad de repeticiones que el contador actual entonces solamente se agrega el elemento moda a la lista
                elemento.append(i)
        elemento = sorted(elemento) #Se ordena la lista de elementos moda para retornar 
        return [contador, elemento] #Se retorna un arreglo con el numero de repeticiones que tuvo cada elemento moda y la lista de elementos moda
    else:
        return ["La lista esta vacia","La lista esta vacia"] #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo

def mediana_x(l):#La funcion de moda recibe como parametro de entrada una lista "l"
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia
        l_ordenada = sorted(l) #En primer lugar se debe ordenar la lista de entrada con la funcion de python sorted() para listas, la cual recibe como parametro una lista y retorna una lista ordenada
        cantidad = len(l) #Luego se obtiene el largo de la lista para identificar que estrategia seguir
        mod = cantidad % 2 # Con el fin de determinar si es par o impar, se oparara la cantidad de elementos de la lista con el modulo de 2, de esta manera si es una cantidad de elementos par el resto sera 0, si es un numero impar de elementos entonces el  resto sera 1
        mediana = 0 #La variable "mediana" sera retornada por la funcion
        cant= cantidad - 1 #Las listas en python funcionan desde indice 0 por ende se debe hacer un ajuste respecto a la cantidad de datos para poder hacer un correcto uso de los indices
        if (mod == 1): #Como se dijo anteriormente si el modulo era 1 entonces la cantidad de elementos de la lista era impar por ende la estrategia a seguir es la siguiente
            indice = (cant + 1)/2 #Se obtiene el indice del elemento en la lista al sumarle 1 a la cantidad de elementos ("cant") de la lista y dividir el resultado de eso en 2.
            mediana = l_ordenada[indice]*1.0#Se busca el elemento de la lista ordenada. Se multiplica por 1.0 para convertir la variable a flotante
        else:#En este caso el modulo resulto ser 0, lo que quiere decir que existe una catidad par de elementos en la lista, en tal caso se procede con la siguiente estrategia
            indice_1 = cant/2 #La mediana sera el resultado de la suma de los 2 elementos centrales divididos en 2, el primer elemento se obtiene gracias al indice de la lista que da por resultado de la operacion de dividir en 2 la cantidad de elementos de la lista
            indice_2 = (cant/2) + 1 #El sigueinte elemento a utilizar de la lista se obtiene al sumarle 1 al indice del elemento anterior, por consiguiente es el elemento inmediatamente sucesor del elemento 1
            mediana = (l_ordenada[indice_1] + l_ordenada[indice_2])/2.0 #Finalmente se obtiene la mediana al dividir entre 2 la suma de ambos elementos
        return mediana #Se retorna la mediana de la lista
    else: #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo
        return "La lista esta vacia"     
    
def minimo_x(l):#La funcion de moda recibe como parametro de entrada una lista "l"
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia
        minimo = float('inf') #En python se representa un numero exageradamente grande de esta manera y flotante (float = decimal)
        for i in l: #Se recorre la lista preguntando si el valor i es menor que el actualmente guardado como minimo en la variable "minimo"
            if i < minimo: #Solamente si el valor i es menor que el minimo actualmente guardado, se asigna a la variable minimo el valor i como nuevo valor menor de la lista
                minimo = i
        return minimo #una vez recorrida toda la lista se retorna el ultimo valor registrado como minimo
    else: #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo
        return "La lista esta vacia"

def maximo_x(l):#La funcion de moda recibe como parametro de entrada una lista "l"
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia
        maximo = 0 #Se asigna a la variable maximo el valor mas pequeno posible, 0
        for i in l: #Se recorre la lista preguntando si el valor i es mayor que el actualmente guardado como maximo en la variable "maximo"
            if i > maximo: #Solamente si el valor i es mayor que el maximo actual guardado, se asigna a la variable maximo el valor i como nuevo valor mayor de la lista
                maximo= i
        return maximo #una vez recorrida toda la lista se retorna el ultimo valor registrado como maximo
    else: #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo
        return "La lista esta vacia"
    
def varianza_x(l):#La funcion de moda recibe como parametro de entrada una lista "l"   
    if (len(l)) > 0: #En caso que la lista contenga elementos y no este vacia
        suma = 0.0#Para calcular la varianza se utilizara una variable que guarde las sumas de los cuadrados de la diferencia entre el elemento menos la media, dividido en n de elementos menos 1
        x = media_x(l) #Se calcula la media utilizando el metodo anteriormente definido como media_x()
        n = len(l)   #N elementos de la lista (tamano)      
        for i in l: #Se recorre la lista y se van sumando los cuadrados
            suma = suma + (((i-x)**2))
        suma = suma/(n-1)#una vez sumado todos los cuadrados se divide el total en la cantidad de elementos "n" menos 1
        return suma #Finalmente se retorna el valor asociado a la varianza de la lista
    else: #En caso de utilizar una lista vacia, la funcion retornara un 0 en representacion de un valor nulo
        return 0

def desviacion_estandar_x(l):
    if l == None:# En caso que la lista este vacia (NONE) se retornara un 0 en representacion de un nulo
        return 0
    else: #Si la lista tiene elementos entonces se procede a calcular la desviacion estandar
        varianza = varianza_x(l) #El calculo de la desviacion estandar se hace a partir de la varianza, para ello se utiliza el metodo anteriormente definido como varianza_x()
        return varianza**(1/2.0) #Para finalizar se retorna el valor de la desviacion estandar el cual se representa por la raiz cuadrada de la varianza, en este caso se utilizara un exponente de un medio (1/2) en vez de una funcion para calcular la raiz. En cualquier caso el resultado es el mismo.
    
def resumen_estadistico(l):
    media = media_x(l)
    mediana = mediana_x(l)
    moda = moda_x(l)
    minimo = minimo_x(l)
    maximo = maximo_x(l)
    varianza = varianza_x(l)
    desviacion = desviacion_estandar_x(l)
    print "Lista de elementos: ", l
    print "Media: ", media
    print "Mediana: ", mediana
    print "Moda: ", moda[1], "             Cantidad de apariciones: ", moda[0]
    print "Minimo: ", minimo
    print "Maximo: ", maximo
    print "varianza: ", varianza    
    print "Desviacion estandar: ", desviacion    
