## Author: Álvaro Villar Val
## Nombre: Linja
## Version: 1.0
## Fecha: 8/11/2023
#Declaramos los imports
import numpy as np

##########################################################################################################################################
#Definicion de Clase Linja
class Linja():

    #Definimos el constructor de la clase objeto
    ############################################################################################################## 
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)
    ############################################################################################################# 

    #Definimos el constructor de la clase
    ##############################################################################################################                    
    def __init__(self):

        #Inicializamos las Variables
        self.tablero=np.zeros([8,6]) #Tablero del juego
        self.contadorTot1=0             #Contador de los puntos del jugador negro o 1 menos los puntos del jugador rojo
        self.contador1=0                #Contador de los puntos del jugador negro o 1 
        self.contadorTot2=0             #Contador de los puntos del jugador rojo o 2 menos los puntos del jugador negro
        self.contador2=0                #Contador de los puntos del judafor rojo o 2 
        self.contadorFin1=0          #Contador que apunta cuantas fichas extra hay en la fila 7 del tablero
        self.contadorFin2=0          #Contador que apunta cuantas fichas extra hay en la fila 0 del tablero
        self.movimiento=0            #Cuanto se puede mover en el segundo movimiento del Turno
        self.turno=2                 #Guarda el turno en el que estamos
        self.comprobadorTurno=True        #Guardamos un comprobador de cuantos turnos seguidos hemos hecho
    #############################################################################################################  

    #Definimos la función que establece el stado incial del tablero
    #############################################################################################################                    
    def inicio(self): 
        #self.tablero=np.array([(2,2,2,2,2,2),(2,2,2,2,2,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(1,0,0,0,2,1),(1,1,1,1,1,1),(1,1,1,1,0,0)])
        #Inicializamos con un bucle for las posiciones iniciales de las fichas negras y Rojas
        for j in range(8):
            for i in range(6):
                if(j==0): #Colocamos las fichas Negras en la fila 0
                    self.tablero[j][i]=1
                elif(j==7): #Colocamos las fichas Rojas en la fila 7
                    self.tablero[j][i]=2
                elif(i==0): #Colocamos las fichas Negras en la columna 0
                    self.tablero[j][i]=1
                elif(i==5): #Colocamos las fichas rojas en la columna 5
                    self.tablero[j][i]=2
    #############################################################################################################                 
                     
    #Definimos el metodo para hallar los puntos de las fichas negras
    #############################################################################################################                                   
    def valSum1(self,valj):
            
            if valj==4 : #Si esta en la fila 5 la ficha vale 1
                return 1
            elif valj==5 : #Si esta en la fila 5 la ficha vale 2
                return 2
            elif valj==6: #Si esta en la fila 6 la ficha vale 3
                return 3
            elif valj==7: #Si esta en la fila 7 la ficha vale 5
                return 5
            else:
                return 0 #Si no esta en ninguna de las filas de puntuar se devolveria 0
    ############################################################################################################# 
    
    #Definimos un metodo para devolver el tablero       
    #############################################################################################################
    def returnTablero(self):
        return self.tablero
    #############################################################################################################
    
    #Definimos el metodo para hallar los puntos de las fichas negras  
    ##############################################################################################################                             
    def valSum2(self,valj):
           
            if valj==0: #Si esta en la fila 0 la ficha vale 5
                return 5
            elif valj==1: #Si esta en la fila 1 la ficha vale 3
                return 3
            elif valj==2: #Si esta en la fila 2 la ficha vale 2
                return 2
            elif valj==3: #Si esta en la fila 3 la ficha vale 1
                return 1
            else:
                return 0 #Si no esta en ninguna de las filas de puntuar se devolveria 0
    #############################################################################################################  
    
    #Definimos el metodo para hallar los puntos de las fichas rojas para la funcion de coste
    ##############################################################################################################                             
    def valSum2Int(self,valj):
           
            if valj==0: #Si esta en la fila 0 la ficha vale 28
                return 28
            elif valj==1: #Si esta en la fila 1 la ficha vale 21
                return 21
            elif valj==2: #Si esta en la fila 2 la ficha vale 15
                return 15
            elif valj==3: #Si esta en la fila 3 la ficha vale 10
                return 10
            elif valj==4: #Si esta en la fila 4 la ficha vale 6
                return 6
            elif valj==5: #Si esta en la fila 5 la ficha vale 3
                return 3
            elif valj==6: #Si esta en la fila 6 la ficha vale 1
                return 1
            elif valj==7: #Si esta en la fila 7 la ficha vale 0
                return 0
    ############################################################################################################# 
    #         
   #Definimos el metodo para hallar los puntos de las fichas negras para la funcion de coste
    #############################################################################################################                                   
    def valSum1Int(self,valj):
            
            if valj==7 : #Si esta en la fila 5 la ficha vale 28
                return 28
            elif valj==6 : #Si esta en la fila 5 la ficha vale 21
                return 21
            elif valj==5: #Si esta en la fila 6 la ficha vale 15
                return 15
            elif valj==4: #Si esta en la fila 7 la ficha vale 10
                return 10
            elif valj==3: #Si esta en la fila 3 la ficha vale 6
                return 6
            elif valj==2: #Si esta en la fila 2 la ficha vale 3
                return 3
            elif valj==1: #Si esta en la fila 1 la ficha vale 1
                return 1
            elif valj==0: #Si esta en la fila 0 la ficha vale 0
                return 0
    #############################################################################################################
   #Definimos el metodo para hallar los puntos de cada jugador
   #############################################################################################################         
    def count(self):
        for j in range(8):
            for i in range(6):
                if self.tablero[j][i]==1: #Comprobamos si tiene una ficha Negra
                    #Sumamos el valor que tenga la ficha Negra dependiendo de la fila en la que este
                    self.contador1+=self.valSum1(j) 
                elif self.tablero[j][i]==2:
                    #Sumamos el valor que tenga la ficha Roja dependiendo de la fila en la que este
                    self.contador2+=self.valSum2(j)
        self.contador2+=self.contadorFin2*5 #Añadimos las fichas extra del final del tablero
        self.contador1+=self.contadorFin1*5 #Añadimos las fichas extra del final del tablero
    #############################################################################################################  

    #Definimos el metodo para hallar los puntos que tiene cada jugador y restarle al otro los que el otro tiene
    ##############################################################################################################                    
    def countInteligente(self):
        contadorTemp1=0 #Contador de puntos del jugador Negro
        contadorTemp2=0 #Contador de puntos del jugador Rojo
        #Recorremos todo el tablero comprobando donde esta cada una de las fichas
        for j in range(8):
            for i in range(6):
                if self.tablero[j][i]==1: #Comprobamos si tiene una ficha Negra
                    #Sumamos el valor que tenga la ficha Negra dependiendo de la fila en la que este
                    temp1=self.valSum1Int(j)
                    contadorTemp1+=temp1 
                    contadorTemp2-=temp1 
                elif self.tablero[j][i]==2:
                    #Sumamos el valor que tenga la ficha Roja dependiendo de la fila en la que este
                    temp2=self.valSum2Int(j)
                    contadorTemp2+=temp2
                    contadorTemp1-=temp2

        contadorTemp2+=self.contadorFin2*5 #Añadimos las fichas extra del final del tablero
        contadorTemp1-=self.contadorFin2*5 #Restamos las fichas del final del tablero del otro jugador
        contadorTemp2-=self.contadorFin1*5 #Restamos las fichas del final del tablero del otro jugador
        contadorTemp1+=self.contadorFin1*5 #Añadimos las fichas extra del final del tablero
        return [contadorTemp1,contadorTemp2]   
    #############################################################################################################     
        
    #Definimos el metodo para comparar si dos situaciones del tablero son la misma
    #Se pasan al metodo los dos tableros a comparar y sus contadores de fichas extra en la linea final, en forma de vector 
    # de manera que si se accede a la posicion 0 se accede al contador de la linea 7 y si se accede a la posicion 1 se 
    #accede al contador de la linea 0.
    #############################################################################################################
    def compare(self,tablero1,tablero2,contadoresFinal1,contadoresFinal2):
        for j in range(8):
            for i in range(6):
                if tablero1[j][i]!=tablero2[j][i]: #Si alguna de las casillas del tablero no son iguales se devuelve false
                   return False 
        #Si no tienen el mismo numero de fichas extra en la linea 7 devuelve false
        if contadoresFinal1[0]!=contadoresFinal2[0]: 
            return False
        #Si no tienen el mismo numero de fichas extra en la linea 0 devuelve false
        elif contadoresFinal1[1]!=contadoresFinal2[1]:
            return False
        return True
    ############################################################################################################# 

    #Definimo el metodo que cuenta cuantas fichas hay en una linea dada
    #############################################################################################################
    def countline(self,line):
        #Contador de las fichas en la fila
        counter=0
        for i in range(6): #Recorremos la linea
            if self.tablero[line][i]==1 or self.tablero[line][i]==2: #Si en una de las celdas hay una ficha Negra o Roja contamos 1+
                counter+=1
        return counter
    ############################################################################################################# 

    #Definimos el metodo para mover una ficha de una posicion dada en forma de tupla a otra tambien dada en forma de tupla
    ############################################################################################################# 
    def simpleMove(self,origen,destino):
        temp=self.tablero[origen[0]][origen[1]] #Creamos una variable temporal para guardar la ficha a mover
        self.tablero[origen[0]][origen[1]]=0 #Limpiamos la posicion original
        self.tablero[destino[0]][destino[1]]=temp #Colocamos la ficha guardada en la posición destino
    #############################################################################################################

    #Definimos el metodo para mover una ficha y en caso de moverla a la ultima fila guardarla si ya esta llena
    #############################################################################################################
    def move(self,origen,destino):
        if(destino[0] ==0): #Si estamos en la fila 0
                if(self.isEmpty(destino[0],destino[1])): #Si el sitio objetivo esta vacio
                    self.simpleMove(origen,destino)
                else:   #Si no esta vacio la guardamos en el contador de fichas de ultima fila
                    self.contadorFin2+=1
                    self.tablero[origen[0]][origen[1]]=0   
        elif(destino[0] ==7): #Si estamos en la fila 7
                if(self.isEmpty(destino[0],destino[1])): #Si el sitio objetivo esta vacio
                    self.simpleMove(origen,destino)
                else:  #Si no esta vacio la guardamos en el contador de fichas de ultima fila
                    self.contadorFin1+=1
                    self.tablero[origen[0]][origen[1]]=0  
        else: #En caso de no estar en ninguna de las filas del final simplemente movemos la ficha
                self.simpleMove(origen,destino)
    ############################################################################################################# 

    #Definimos el metodo para obterner el turno en el que se ecuentra el juego en el momento
    #############################################################################################################
    def getTurno(self):
        if self.turno==1:
            return "Turno Negro" 
        elif self.turno==2:
            return "Turno Rojo"
        else:
            print("Ha ocurrido un error en get Turno")
            return 0
    ############################################################################################################# 

    #Definimos el metodo para saber si una posicion dada esta vacia o no
    #############################################################################################################
    def isEmpty(self,fil,col):
        if self.tablero[fil][col]==0:
            return True
        else:
            return False
    ############################################################################################################# 

    #Definimos un metodo para saber la distancia entre dos posiciones, solo nos interesa la distancia vertical
    #############################################################################################################
    def getDistance(self,origenX,destinoX):
        if self.turno==1: #Si estamos en el turno Negro ya que van de arriba a abajo se resta el origen al destino
            return destinoX-origenX
        elif self.turno==2: #Si estamos en el turno Rojo ya que van de abajo a arriba se resta el destino al origen
            return origenX-destinoX
        else:
            #Ocurrio un error 
            print("Ha ocurrido un error en getDistance")
            return 0
    ############################################################################################################# 

    #Definimos un metodo para comprobar que la cordenada que se pasa este dentro del rango del tablero
    #############################################################################################################
    def isInBounds(self,fila,columna):
        if fila>=0 and fila<=7 and columna>=0 and columna<=5:
            return True
    ############################################################################################################# 
    
    #Definimos una Funcion para cambiar el turno actual al otro posible
    ############################################################################################################# 
    def changeTurn(self):
        if(self.turno==1): #Si estamos en turno Negro lo Cambiamos a turno Rojo
            self.turno=2
        elif(self.turno==2): #Si estamos en turno Rojo lo cambiamos a turno Negro
            self.turno=1
        else:
            print("Ha ocurrido un error en el cambio de turno")
     ############################################################################################################# 

    #Definimos un metodo para comprobar que las cordenadas que se pasan este dentro del rango del tablero
    #############################################################################################################
    def areInBounds(self,origenX,origenY,destinoX,destinoY):
        if self.isInBounds(origenX,origenY) and self.isInBounds(destinoX,destinoY):
            return True
    ############################################################################################################# 

    #Definimos un metodo para comprobar que el movimiento que se esta realizando es legal
    #############################################################################################################
    def isLegal(self,origenX,origenY,destinoX,destinoY):
        if not self.areInBounds(origenX,origenY,destinoX,destinoY): #Comprobamos que el movimiento esta dentro del rango del tablero
            return False
        if self.turno!=self.tablero[origenX][origenY]: #Comprobamos que estamos moviendo una ficha del turno que toca
            return False
        #Comprobamos que estamos en la segunda parte del turno ya que si esto es cero significaria que es la primera
        if self.movimiento!=0: 
            if self.getDistance(origenX,destinoX)!=self.movimiento: #Comprobamos que no nos movemos más de lo que podemos
                return False
        elif self.movimiento==0: #Comprobamos que estamos en la primera parte del turno
            if self.getDistance(origenX,destinoX)!=1: #Comprobamos que no nos estamos moviendo mas de una unidad
                return False
        else:
            #Si algo va mal salta un error
            print("ha ocurrido un error en Islegal")
            return 0
        #Comprobamos que no se esta moviendo a la ultima linea ya que en esta se puede colocar mas del limite
        if destinoX!=0 and destinoX!=7: 
            if not self.isEmpty(destinoX,destinoY): #Comprobamos si la posición a la que nos queremos mover esta libre
                return False
        else: #En caso de estar en la ultima fila
            if self.countline(destinoX)<6: #Comprobamos que la ultima fila esta completa
                if not self.isEmpty(destinoX,destinoY): #Si no esta completa tendremos que mover la ficha a una posición vacia
                    return False 
        return True #Si ninguna de las condiciones se imcumplen devolvemos que es un movimiento legal
    ############################################################################################################# 
    
    #Definimos un metodo para mover las fichas comprobando que se mueven de manera legal nos pasan dos tuplas con la coordenadas
    #############################################################################################################
    def moveArbitrado(self,origen,destino):
        origenFil=origen[0]
        origenCol=origen[1]
        destinoFil=destino[0]
        destinoCol=destino[1]
        comprobador=False #Comprobador para saber si hay que resetear a 0 el contador de movimiento
        if self.isLegal(origenFil,origenCol,destinoFil,destinoCol): #Comprobamos si es un movimiento legal
            if self.movimiento==0:   #Comprobamos si estamos en el la primera parte del turno 
                if(destinoFil==0 or destinoFil==7): #Si se llega a la ultima fila se obtine 1 movimiento solo
                   self.movimiento=1
                else:
                    if(self.countline(destinoFil)==0):#Si no estamos en la ultima fila pero no hay fichas en la fila destino se cambia el turno
                        self.changeTurn()
                    else:
                        self.movimiento=self.countline(destinoFil)
            else:   #Estamos en la segunda parte del turno por ende tenemos que cambiar de turno si no nos movemos a una fila vacia y poner a 0 el movimiento
                comprobador=True #Cambiamos a True el comprobador de manera que se pondra a 0 el la var movimiento despues de mover
                if(self.countline(destinoFil)==0 and self.comprobadorTurno): #Comprobamos si en la segunda mitad del turno acaba en fila vacia por primera vez
                    self.comprobadorTurno=False #Marcamos que ya hemos conseguido un segundo turno
                else:
                    self.changeTurn() #En caso de que no llegue a una fila vacia o no lo haga por primera vez cambiamos turno
                    self.comprobadorTurno=True #Desmarcamos que hemos comseguido segundo turno
            self.move(origen,destino) #Si es legal movemos las ficha
            if(comprobador): #Cambiamos a 0 el valor de la var movimiento
                self.movimiento=0
        else:
            print("No se puede mover ahi")
            return False
        return True
    #############################################################################################################   
     
    # Definimos una función que compruebe que no hay movimientos posibles para el turno actual
    #############################################################################################################         
    def movimientoPosibleEnTurno(self):
        primeraParteTurno=False     #Declaramos un comprobador para saber en que parte del turno estamos
        if(self.movimiento==0):     #Comprobamos que estamos en la primera parte del turno
            primeraParteTurno=True  #Si lo estamos guardamos que lo estamos
        for j in range (8):         #Recorremos el tablero
            for i in range(6):
                if(self.tablero[j][i]==self.turno): #Si la ficha coincide con el turno en el que nos encontramos
                    if(primeraParteTurno):              #Si estamos en la primera parte del turno
                        for k in range(6):              #Comprobamos todas las casillas en la fila en la que se puede mover
                            #Si estamos en turno uno sumaremos 1 a la fila actual para saber a que casillas se puede mover
                            if(self.turno==1):          
                                if(self.isLegal(j,i,j+1,k)): #Comprobamos si seria un movimiento legal a la casilla
                                    return False             #Si no lo es devolvemos false
                            else:   #En caso de estar en turno dos tendremos que restarle 1 a la fila actual
                                if(self.isLegal(j,i,j-1,k)):  #Comprobamos si seria un movimiento legal a la casilla
                                    return False              #Si no lo es devolvemos false
                    else:    #En caso de estar en la segunda mitad del turno
                        for k in range(6):  #Comprobamos todas las casillas en la fila en la que se puede mover
                            #Si estamos en turno uno sumaremos el movimiento a la fila actual para saber a que casillas se puede mover
                            if(self.turno==1):
                                if(self.isLegal(j,i,j+self.movimiento,k)): #Comprobamos si seria un movimiento legal a la casilla
                                    return False                           #Si no lo es devolvemos false
                            else: #Si estamos en turno uno restaremos el movimiento a la fila actual para saber a que casillas se puede mover
                                if(self.isLegal(j,i,j-self.movimiento,k)): #Comprobamos si seria un movimiento legal a la casilla
                                    return False                           #Si no lo es devolvemos false
        return True
    #############################################################################################################
    def gameOver(self):
        if(self.movimientoPosibleEnTurno()):
            self.changeTurn()
            self.movimiento=0
            if(self.movimientoPosibleEnTurno()):
                return True
        return False
    #Definimos un metodo que comprueba si se ha llegado al estado de fin de juego
    #############################################################################################################
    def comprobarFin(self):
        if(self.gameOver()):
            return True
        comprobatorTemp=False #Comprobador de si nos hemos encontrado alguna ficha Negra
        for j in range(8): #Recorremos el tablero 
            for i in range(6):
                if(comprobatorTemp): #si hemos encontrado almenos una ficha Negra
                    if(self.tablero[j][i]==2): #Comprobamos si hay alguna ficha Roja despues
                            return False #Si la hay no es el final del juego                
                elif(self.tablero[j][i]==1): #Si nos encontramos una ficha Negra
                    comprobatorTemp=True    #Guardamos que nos hemos encontrado la ficha Negra
                    #Comprobamos que no hay una ficha negra en la misma fila antes de donde nos hemos encontrado a la Roja
                    for k in range(i):      
                        if(self.tablero[j][k]==2): #si hay una ficha antes de donde hemos encontrado la negra no es el final del juego
                            return False               
        return True #Si no hemos encontrado fichas Rojas despues de encontrar la Negra es el final del juego
    #############################################################################################################
    
###########################################################################################################################################
#Runer Code
# prueba= Linja()
# prueba.inicio()
# prueba.count()
# print(prueba.tablero)
# comprobadorFinal=True
# prueba= Linja()
# prueba.inicio()
# # prueba.count()
# # prueba.countInteligente()
# # print(prueba.contadorTot1,prueba.contadorTot2)
# # print(prueba.contador1,prueba.contador2)
# print("\nBienvenido al inicio del juego, usted esta jugando a Linja\n")
# while comprobadorFinal:
#     print(prueba.tablero)
#     if(prueba.movimiento==0):
#         print("\n Empezamos la 1º parte del ",prueba.getTurno(), " puedes moverte 1 casilla")
#     else:
#         print("\n Empezamos la 2º parte del ",prueba.getTurno()," puedes mover ",prueba.movimiento," casillas")
    
#     cordenadaOrigentemp=[int(x) for x in input("\nDame la coordenada origen en este formato: Fila Columna ").split()]
#     cordenadaFinaltemp=[int(x) for x in input("\nDame la coordenada final en este formato: Fila Columna ").split()]
#     cordenadaOrigen=[cordenadaOrigentemp[0]-1, cordenadaOrigentemp[1]-1]
#     cordenadaFinal=[cordenadaFinaltemp[0]-1, cordenadaFinaltemp[1]-1]
#     prueba.moveArbitrado(cordenadaOrigen,cordenadaFinal)
#     if(prueba.comprobarFin()):
#         comprobadorFinal=False
#         prueba.count()
#         print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡FIN DEL JUEGO!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         print("La puntuación del jugador Negro es: ",prueba.contador1)
#         print("La puntuación del jugador Rojo es: ",prueba.contador2)
#         if(prueba.contador2>prueba.contador1):
#             print("El ganador es el jugador Rojo")
#         elif(prueba.contador2<prueba.contador1):
#             print("El ganador es el jugador Negro")
#         else:
#             print("Empate entre los dos jugadores")