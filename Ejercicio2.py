#integrantes : 

#Declaracion de funciones:
def suma_matrix(m1,m2):#este metodo recibe como parametros de entrada 2 matrices de igual orden
    if len(m1) != 0 and len(m2) != 0: #aqui se comprueba que ambas matrices no esten vacias
        n1 = len(m1)# cantidad de filas matriz 1
        n11 = len(m1[1])# cantidad de columnas matriz 1
        n2 = len(m2)# cantidad de filas matriz 2
        n22 = len(m2[1])# cantidad de columnas matriz 2
        ms = [k[:] for k in m1] #copia de una matriz
        if n1 == n2 and n11 == n22: #aqui se comprueba que ambas matrices sean de igual orden, MxN
            for i in range(len(m1)):#a continuacion se recorre cada elemento de las matrices y se suman en simultaneo para ser agregados a la matriz de suma "ms"
                for j in range(len(m1[i])):
                    ms[i][j] = m1[i][j] + m2[i][j] #ejemplo: ms[0][0] = m1[0][0] + m2[0][0]
            return ms
        else:
            return "Las matrices no tienen el mismo orden"
    else:
        return "Una o ambas matrices estan vacias" 
    
    
def multiplicacion_matricial(m1,m2):#este metodo recibe como parametros de entrada 2 matrices de igual orden
    if len(m1) != 0 and len(m2) != 0:#aqui se comprueba que ambas matrices no esten vacias
        n1 = len(m1) #filas de la matriz m1
        n22 = len(m2[1])#columnas de la matriz m2
        m = [] #matriz que guardara el resultado de la multiplicacion de matrices
        if n1 == n22: #se comprueba que se cumpla la regla de multiplicacion de matrices. Cantidad de filas de matriz 1 igual a cantidad de columnas de matriz 2
            for i in range(n1):#cada elemento de la fila i de la matriz 1 multiplicara a un elemento de la columna j de la matriz 2.  
                fila = []
                for j in range(n22):
                    suma = 0#el resultado de cada multiplicacion sera almacenado en la variable suma para posteriormente ser registrado en la matriz resultante de la multiplicacion como el total de de la fila i de la matriz 1 respecto a la columna j de la matriz 2
                    for c in range(len(m2[j])):
                        suma += m1[i][c]*m2[c][j]
                    fila.append(suma)
                m.append(fila)      
            return m
        else:
            return "El tamano de las filas de la matriz 1 no coincide con el tamano de las columnas de la matriz 2"
    else:
        return "Una o ambas matrices estan vacias"  
    

def determinante(m):#Este metodo recibe como parametro de entrada una sola matriz
    if len(m) != 0: #Se verifica que la matriz no este vacia
        if len(m) == len(m[0]): #Solo se podra obtener determinante si la matriz es cuadrada o de orden n
            m2 = [k[:] for k in m] #copia de la matriz
            n = len(m) #orden de la matriz "n"
            suma = 0.0
            if n > 2: # Rango de la matriz (tamano n)
                for i in range(n):
                    factor = m2[0][i] # saca el factor de la primera fila i
                    signo = -2 * (i % 2) + 1 # calcula su signo
                    m2.remove(m2[0]) # Borra la primera fila
                    for j in range(0, n - 1):
                        m2[j].pop(i) # Quita, de cada fila de B, el factor i, o sea, quita esa columna.
                    suma = suma + factor * signo * determinante(m2) # El determinante es la suma anterior mas lo que calcule
                    m2 = [k[:] for k in m] # reconstruye la matriz B
                return suma # retorna la suma
            else:
                return (m2[0][0] * m2[1][1]) - (m2[0][1] * m2[1][0]) # devuelve el determinante del rango 2
        else:
            return "No es una matriz cuadrada"
    else:
        return "La matriz esta vacia"

def transpuesta(m):#Este metodo recibe como parametro de entrada solo 1 matriz
    if len(m) != 0: # Se verifica que la matriz no este vacia
        x = len(m) #cantidad de filas de la matriz
        y = len(m[0]) #cantidad de columnas de la matriz
        matriz = []
        for i in range(y): #se genera una matriz vacia
            matriz.append([])
            for j in range(x):
                matriz[i].append(None)
        for i in range(x):# al recorrer los elemento de la matriz va cambiando la posicion de los elementos remplazando la ubicacionde su fila por la de su columna y viceversa
            for j in range(y):
                matriz[j][i] = m[i][j]
        return matriz
    else:
        return     "La matriz esta vacia"
    
def escalar(a,m):#Este metodo se encarga de realizar una multiplicacion escalar de una matriz, es decir, la multiplicacion de un numero escalar y una matriz
    if len(m) != 0:# se comprueba que la matriz no este vacia
        x = len(m) #cantidad de filas de la matriz
        y = len(m[0])# cantidad de columnas de la matroz
        matriz = []
        for i in range(x):#se genera una matriz vacia
            matriz.append([])
            for j in range(y):
                matriz[i].append(None)
        for i in range(x): #En esta parte simplemente se le multiplica el valor del escalar a cada elemento de la matriz
            for j in range(y):
                matriz[i][j] = a*m[i][j]
        return matriz
    else:
        return     "La matriz esta vacia"
    
def adjunta(m): #este metod recibe como parametro de entrada una matriz y devuleve su matriz adjunta. La matriz adjunta sera necesaria para obtener la matriz inversa.
    if len(m) != 0: #Se comprueba que la matriz no este vacia
        if len(m) == len(m[0]): #es necesario que la matriz sea cuadrada para poder obtener determinantes
            m2 = [k[:] for k in m] #copia de la matriz
            final = [a[:] for a in m] #En esta variable se almacenara la matriz adjunta resultante
            final = escalar(0,final) #se resetea la matriz generada 
            n = len(m) #se determina el orden de la matriz "n"
            if n > 2: # Rango de la matriz (tamano n)
                for c in range(n):
                    for i in range(n):
                        signo = (-1)**(c+i) # calcula su signo
                        m2.remove(m2[c]) # Borra la primera fila
    
                        for j in range(0, n - 1):
                            m2[j].pop(i) # Quita, de cada fila de B, el factor i, o sea, quita esa columna.
                        final[c][i] = signo*determinante(m2) # El determinante + el signo
                        m2 = [k[:] for k in m] # reconstruye la matriz B
                return final # retorna la suma
            else:#en caso de ser una matriz de orden 2           
                aux = [k[:] for k in m]
                aux[0][0] = m[1][1]
                aux[1][1] = m[0][0]
                aux[0][1] = m[1][0]*(-1)
                aux[1][0] = m[0][1]*(-1)             
                return aux # devuelve el determinante del rango 2
        else:
            return "No es una matriz cuadrada"
    else:
        return "La matriz esta vacia"

    
def inversa(m):
    if len(m) != 0: #Se verifica que la matriz no este vacia
        if len(m) == len(m[0]): #Solo se podra obtener determinante si la matriz es cuadrada o de orden n
            det = determinante(m) #para comenzar se necesita saber si se cumple la regla principal para matrices inversas. Determinante distinto de 0
            if det != 0 :#Si el determinante no es 0 entonces se procede a calcular la matriz inversa
                adj = adjunta(m) #para calcular la matriz inversa se utilizara el determinante, y la matriz adjunta
                adj_t = transpuesta(adj) #para continuar con el proceso del calculo de matriz inversa se procede a calcular la transpuesta de la matriz adjunta
                inversa = escalar((1.0/det),adj_t)#finalmente se obtiene la matriz inversa
                return inversa
            else:
                return "El determinante es 0"
        else:
            return "No es una matriz cuadrada"
    else: 
        return "La matriz esta vacia"
    
    

def resumen_matriz(m1,m2,a):
    suma = suma_matrix(m1,m2)
    mult = multiplicacion_matricial(m1,m2)
    det = determinante(m1)
    trans = transpuesta(m1)
    escal = escalar(a,m1)
    adj = adjunta(m1)
    inv = inversa(m1)
    print "Matriz 1: ",m1
    print "Matriz 2: ",m2
    print "Suma m1 + m2: ", suma
    print "Multiplicacion matricial m1 * m2: ", mult
    print "Determinante Matriz 1: ", det
    print "Matriz transpuesta m1: ", trans
    print "Multiplicacion escalar ",a, "* m1: ", escal
    print "Matriz adjunta m1: ", adj
    print "Matriz inversa m1: ", inv
