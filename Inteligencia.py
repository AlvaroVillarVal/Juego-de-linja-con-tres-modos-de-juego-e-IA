## Author: Álvaro Villar Val
## Nombre: Inteligencia
## Version: 1.0
## Fecha: 08/11/2023
#Declaramos los imports
import numpy as np
from Linja import Linja
import copy
class Inteligente():
    #Definimos el constructor de la clase objeto
    ############################################################################################################## 
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)
    #############################################################################################################              
                     
    #Definimos las función del turno del ordenador, en ella haremos la función min y max, recibimos el estado del juego
    #############################################################################################################
    def jugarTurnoOrdenador(self,juego:Linja):
        #Hacemos la funcion minmax en el estado actual del juego para encontrar el moviemnto oprimo
        for i in range(9): #en caso de no funcionar con una profundidad de 8 ya que no tendría, 
            #4 o 5 más a futuro reducimos la profundidad hasta que haga el unico movimiento que puede hacer
            hijoOptimo,alfabet=self.minMax([juego,0,0,0,0,0],0,juego.turno,0,0,8-i)#LLamamos al miniMax y recibimos el hijo optimo
            if(hijoOptimo!=0):
                movimientoOptimo=[hijoOptimo[1],hijoOptimo[2],hijoOptimo[4],hijoOptimo[5]]
                return movimientoOptimo #devolvemos el movimiento optimo
        #Guardamos el movimiento optimo para que lo pueda recivir la UI y usarlo de manera efectiva
       
       
    #############################################################################################################

    #Definimos una funcion  que mueva la ficha al primer sitio que encuentre que no este en la lista de excluisiones
    #############################################################################################################
    def moverPrimerSitio(self,juego:Linja,origen,excluidos):
        movimientoTemp=juego.movimiento  #Guardamos cuantas casillas puede moverse en el segundo movimiento del turno
        if juego.turno==1:    #Si es el turno Negro
            if(juego.movimiento==0): #si el moviemto es 0 significa que estamos en la primera parte del turno
                for i in range (5, -1, -1):  #Recorremos la fila a la que se puede mover la ficha
                    if ([origen[0]+1,i] not in excluidos): #si la posición destino no esta en la lista de excluidos
                         # Si se puede mover la ficha a esa posición se mueve y si se mueve entramos en el if
                        if(juego.moveArbitrado(origen,[origen[0]+1,i])):
                            return [origen[0]+1,i] #Devuelve la posición a la que se ha movido
            else: #Si no es 0 el movimiento
                for i in range (5, -1, -1): #Recorremos la fila a la que se moveria con el movimiento 
                     #si la posición destino no esta en la lista de excluidos
                    if([origen[0]+juego.movimiento,i] not in excluidos):
                        # Si se puede mover la ficha a esa posición se mueve y si se mueve entramos en el if
                        if(juego.moveArbitrado(origen,[origen[0]+juego.movimiento,i])):
                            return [origen[0]+movimientoTemp,i] #Devuelve la posición a la que se ha movido
        else: # Si es el turno rojo
            if(juego.movimiento==0): #si el moviemto es 0 significa que estamos en la primera parte del turno
                for i in range (6): #Recorremos la fila a la que se puede mover la ficha
                    if ([origen[0]-1,i] not in excluidos):#si la posición destino no esta en la lista de excluidos
                        # Si se puede mover la ficha a esa posición se mueve y si se mueve entramos en el if
                        if(juego.moveArbitrado(origen,[origen[0]-1,i])):
                            return [origen[0]-1,i]#Devuelve la posición a la que se ha movido
            else: #Si no es 0 el movimiento
                for i in range (6):  #Recorremos la fila a la que se puede mover la ficha
                    #si la posición destino no esta en la lista de excluidos
                    if([origen[0]-juego.movimiento,i] not in excluidos):
                        # Si se puede mover la ficha a esa posición se mueve y si se mueve entramos en el if
                        if(juego.moveArbitrado(origen,[origen[0]-juego.movimiento,i])):
                            return [origen[0]-movimientoTemp,i] #Devuelve la posición a la que se ha movido
        return False #Devuelve false en caso de que falle algo
    #############################################################################################################

    #Definimos el metodo para hallar la primera posición a la que se pueda mover ua ficha
    #############################################################################################################
    def posPrimFich(self,juego:Linja,excluidos):
    #Recorremos el tablero saltandonos la primera fila, ya que en ella no habra filas, y si las hay no se pueden mover
        for j in range(7): 
            for i in range(6):
                
                if(juego.turno==1):#Si estamos en el turno negro
                    if [j,i] not in excluidos: #Si la posición no esta en la lista de excluidos 
                        #Si en la posicion en la que se encuentra hay una ficha del turno que buscamos
                        if(juego.tablero[j][i]==1): 
                            return [j,i] #Devuelve la posción que cumple las condiciones que bucamos
                else:# Si estamos en el turno rojo
                    if [7-j,5-i] not in excluidos: #Si la posición no esta en la lista de excluidos
                        #Si en la posicion en la que se encuentra hay una ficha del turno que buscamos
                        #Ademas al ser el turno negro, se recorre el tablero a la contraria
                        if(juego.tablero[7-j][5-i]==2): 
                            return [7-j,5-i] #Devuelve la posción que cumple las condiciones que bucamos
        return False #Si falla se devuelve false por que no se ha comletado la operación
    #############################################################################################################

    #Definimos una fución que nos devuelve los hijos posibles de un estado
    #############################################################################################################
    def obtenerHijos(self,pap,turnOrg):
            estadoPap=pap[0] #guardamos el estado del juego de la primera posición de pap
            hijos=[] #Instaciamos la lista de hijos que bamos a obtener
            origExcluido=[] #Instanciamos la lista de posiciones de origen a las que no les quedan hijos validos
            counts=[] # Aqui guardaos la puntuación de cada uno de los hijos
            destExluido=[] #Aqui guardamos los detinos que nos darían una puntuación que ya hayamos obtenido
            for i in range(3): #Definimos cuantos hijos queremos obtener del estado de juego actual
                comprobador=True #Comprobador de que no hemos encontrado un hijo valido
                while(comprobador): #Bucle para buscar un hijo valido
                    #Obtenemos la posición de laprimera ficha que se pueda mover
                    cordFich=self.posPrimFich(estadoPap,origExcluido) 
                     #Si no hay una posición de una ficha valida, se habra devuelto false, lo que significa que no hay un hijo valido
                    if(cordFich==False): 
                        print("No tiene hijo valido") #Notificamos que no tiene un hijo valido
                        comprobador=False #Salimos del bucle por que no vamos a encontrar un hijo valido
                    else: #Si la posición es valida
                        temp=copy.deepcopy(estadoPap) #Copiamos el estado del padre en temp
                        #movemos la ficha desde la coordenada de origen al primer sitio que se pueda y guardamos el destino
                        destino=self.moverPrimerSitio(temp,cordFich,destExluido) 
                        if(destino==False): #Si no hay un destino valido
                            origExcluido.append(cordFich) #Guardamos el origen en la lista de origenes excluidos
                            destExluido=[] #Reseteamos, la lista de destinos exlusivos
                        else: #si hay un destino valido
                            #Instanciamos el hijo con:
                            # (el estado del juego), (la coordenada de origen), (la coordenada de destino),
                            #(los puntos que tiene el estado resultado),(la coordenada origen del proximo movimiento (la desconocemos))
                            #y finalmente (la coordenada destino del proximo movimiento(estos ultimos valores se usaran para ascender en el minmax))
                            hijo=[temp,cordFich,destino,temp.countInteligente()[turnOrg-1],[0,0],[0,0]]
                            if(hijo[3] not in counts): # Si los puntos del hijo ya se han obtenido antes no se acepta como hijo valido
                                #Si el hijo tiene una puntuación valida
                                hijos.append(hijo) #se añade el hijo a la lista de hijos 
                                counts.append(hijo[3]) #añadimos la puntuación a la lista de puntuaciones
                                comprobador=False #Salimos del while por que hemos encontrado un hijo valido
                            destExluido.append(hijo[2]) #Añadimos el destino a la lista de destinos excluidos
            return hijos #Devolvemos la lista de hijos
    #############################################################################################################
    
    #Definimos la función minMax que hara el algoritmo minMax y devolvera el mejor movimiento posible para el turno 
    # que lo llama
    #############################################################################################################
    def minMax(self, papa,prof,turnOrg,alfa,beta,profMax):
        if(prof==0): #lo instanciamos en la primera llamada del minmax
            alfa=-10000 #Ponemos a alfa en un numero muy muy pequeño que sea imposible de llegar con puntos
            beta=10000  #Ponemos a alfa en un numero muy muy grande que sea imposible de llegar con puntos
        estadoPap=papa[0] #Guardamos el estado de papa en estadoPap
        if(prof<profMax): #Definimos cuanta queremos que sea la profundidad
            hijos=self.obtenerHijos(papa,turnOrg) #Obtenemos la lista de posibles hijos del estado actual
            #si el turno de movimiento es el mismo del turno original que llamo a la función min y max hacemos funcion max
            if(estadoPap.turno==turnOrg): #Entramos en max
                minHijos=[0] *len(hijos) #Instanciamos la lista de hijos minimos con tantos espacios como hijos haya
                #Instanciamos el hijo maximo vacio y con contador de puntos muy bajo
                maxHijo=[papa[0],[0,0],[0,0],-100000,[0,0],[0,0]]
                comprobador=True # Comprobador de si hay hijos, si no hay un hijo valido se queda true y devuelve 0       
                for i in range(len(hijos)): #Recorremos la lista de hijos guardando los hijos optimos
                    #LLamamos a la función min y max para buscar el siguiente hijo optimo, y lo guardamos en la posición adecuada
                    minHijos[i],alfabet=self.minMax(hijos[i],prof+1,turnOrg,alfa,beta,profMax) 
                    if(alfa<alfabet): #hacemos los cortes alfa beta, en caso de que el alfa del hijo sea mayor
                        if(alfabet>=beta): #si el alfa es mayor que el beta hacemos corte
                            print("Corte alfa") #Se have corte alfa
                            return 0,alfa #se devuelve 0(el corte)
                        alfa=alfabet #En caso de no hacer el corte el nuevo alfa se guarda
                for temp in minHijos: #recorremos la lista de hijos optimos
                    if(temp!=0): #si el hijo no es 0 osea que hay hijo y no es nulo
                        maxval=maxHijo[3] #guardamos el contador de puntos del hijo maximo actual
                        maxVal2=temp[3] #guardamos el contador de puntos del hijo actual a comparar
                        if(maxval<=maxVal2): #si el contador del actual es mayor que el del hijo maximo
                            maxHijo=copy.deepcopy(temp) #Copiamos el hijo actual en maxHijo
                            tempX=maxHijo[1]            #Guardamos la posición de origen del movimiento del hijo actual
                            tempY=maxHijo[2]            #Guardamos la posición de destino del movimiento del hijo actual
                            if(prof!=0):                #Si no estamos en la profundidad base
                                #Guardamos la posición de origen del hijo actual, en la zona de siguiente movimiento
                                maxHijo[4]=tempX 
                                #Guardamos la posición de destino del hijo actual, en la zona de siguiente movimiento       
                                maxHijo[5]=tempY
                                #Guardamos la posición de origen del padre actual, en la zona de moviemiento actual
                                maxHijo[1]=papa[1] 
                                 #Guardamos la posición de destino del padre actual, en la zona de moviemiento actual
                                maxHijo[2]=papa[2]
                            

                            comprobador=False #Actualizamos el comprobador para decir que hay hijo valido
                if(comprobador): #Si no hay hijo valido
                    print("No tiene hijo maximo") #Imprimios por pantalla que no hay 
                    return 0,alfa #devolvemos 0
                return maxHijo,alfa #si hay hijo valido devolvemos el hijo optimo
            else:# Si no esta en el turno original hacemos min
                maxHijos=[0] *len(hijos) #Instanciamos la lista de hijos maximos con tantos espacios como hijos haya
                #Instanciamos el hijo minimo vacio y con contador de puntos muy alto
                minHijo=[papa[0],[0,0],[0,0],100000,[0,0],[0,0]]
                comprobador=True   # Comprobador de si hay hijos, si no hay un hijo valido se queda true y devuelve 0            
                for i in range(len(hijos)):#Recorremos la lista de hijos guardando los hijos optimos
                     #LLamamos a la función min y max para buscar el siguiente hijo optimo, y lo guardamos en la posición adecuada
                    maxHijos[i],alfabet=self.minMax(hijos[i],prof+1,turnOrg,alfa,beta,profMax)
                    if(beta>alfabet): #hacemos los cortes alfa beta, en caso de que el beta del hijo sea menos
                        if(alfa>=alfabet):  #si el alfa es mayor que el beta hacemos corte
                            print("Corte beta") #Imprimimos que se realiza un corte beta
                            return 0,beta   #Pasamos el corte beta
                        beta=alfabet     #En caso de que no ocurra un corte
                for temp in maxHijos: #recorremos la lista de hijos optimos
                    if(temp!=0): #si el hijo no es 0 osea que hay hijo y no es nulo
                        minval=minHijo[3] #guardamos el contador de puntos del hijo minimo actual
                        minVal2=temp[3] #guardamos el contador de puntos del hijo actual a comparar
                        if(minval>=minVal2): #si el contador del actual es menor que el del hijo minimo
                            minHijo=copy.deepcopy(temp) #Copiamos el hijo actual en minHijo
                            tempX=minHijo[1]        #Guardamos la posición de origen del movimiento del hijo actual
                            tempY=minHijo[2]        #Guardamos la posición de destino del movimiento del hijo actual
                            if(prof!=0):            #Si no estamos en la profundidad base
                                #Guardamos la posición de origen del hijo actual, en la zona de siguiente movimiento
                                minHijo[4]=tempX
                                #Guardamos la posición de destino del hijo actual, en la zona de siguiente movimiento       
                                minHijo[5]=tempY
                                 #Guardamos la posición de origen del padre actual, en la zona de moviemiento actual
                                minHijo[1]=papa[1]
                                #Guardamos la posición de destino del padre actual, en la zona de moviemiento actual
                                minHijo[2]=papa[2]


                            comprobador=False #Actualizamos el comprobador para decir que hay hijo valido
                if(comprobador):    #Si no hay hijo valido
                    print("No tiene hijo minimo")   #Imprimios por pantalla que no hay 
                    return 0,beta   #devolvemos 0
                return minHijo,beta  #si hay hijo valido devolvemos el hijo optimo
            
        else: #Si la profundidad es maxima
            return papa ,papa[3]#devuelve el padre y el valor del mismo
    #############################################################################################################
###############################################################################################################################
   