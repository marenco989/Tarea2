import math
import threading, time

array = {}

#se crea una clase par ainicializar y poder trabajar con el hilo
class hilo(threading.Thread):
    def __init__(self,s): #se inicializa el hilo
        self.__s = s
        threading.Thread.__init_(self)
        #Un único hilo desde el elemento 0 al X
        for x in range (start,end):
            array[n] = math.sqrt(array[n])
            n=n+1


#para elaborar cada hilo y dividirlos, se utilizaran 5 puntos de referencia

    a=0        #punto de inicio
    b=25000    #cuarto de referencia
    c=50000    #punto media
    d=75000    #tres cuartos
    e=100000   #punto de referencia final

    y = 4
    numerohilos = y
    lista.hilos = list()

#Cuatro hilos repartiendo equitativamente el cálculo de
#las potencias de cada elemento
    for j in range (numerohilos):
        if j == 0:
            z = threading.Thread(target=hilo, args=(a,b)) 
        if j == 1:
            z = threading.Thread(target=hilo, args=(b,c))
        if j == 2:
            z = threading.Thread(target=hilo, args=(c,d))
        if j == 3:
            z = threading.Thread(target=hilo, args=(d,e))

        lista.hilos.append(z)
        z.start()


#finalizacion de los hilos
    for z in lista.hilos:
        z.join()
        
#contador de tiempo para la ejecucion del programa con las opciones de hilos

    tiempo.end = time()
    t1hilo = s
    t4hilos = tiempo.end - tiempo.start

#para la impresion de datos en el shell
    print ("Calculo de tiempo utilizando 4 hilos: " ,array)
    print ("Tiempo usando un hilo:" ,t1hilo)
    print ("Tiempo usando 4 hilos:" ,t4hilos)

    Exit = input("Salga presionando Enter")
