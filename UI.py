# ## Author: Álvaro Villar Val
## Nombre: UI
## Version: 0.9
## Fecha: 22/11/2023
#Declaramos los imports
import pygame 
import sys
import time
from Linja import Linja
from Inteligencia import Inteligente
#TO DO: Comentar


pygame.init()
##########################################################################################################################################
# Definimos las constantes
ANCHO = 800 #Ancho de la pantalla
ALTO = 800 #Alto de la pantalla
LIN_ANCHO = 15 #Ancho de las lineas delimitadoras
FILAS = 8 #Nº de filas en el tablero
COLUMNAS = 6 #Nº de columnas en el tablero
CELDA_SIZ =100 #Tamaño que queremos que tengan las celdas dibujadas
RADIO_CIRC = 35 #Radio de la ficha
ANCHO_CIRC = 15 #Ancho de la linea que dibuja la ficha
# Declaramos aqui los colores que utilizaremos
ROJO = (247, 27, 64)
VERDE = (0,255,0)
AZUL=(0,0,255)
GRIS=(71,75,78)
BACK_COLOR = (28, 170, 156) #Color del fondo
COLOR_LINEA = (23, 145, 135) #Color de la linea delimitadora
JUGADOR1_COLOR = (0, 0, 0) #Color del jugador 1 (negro)
JUGADOR2_COLOR = (175, 2, 2) #Color del jugador 2 (Granate)
##########################################################################################################################################
#Definimos la Clase Ui que sera la interfaz de usuario
class Ui():
    #Definimos el constructor de la clase objeto
    ############################################################################################################## 
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)
    ############################################################################################################# 

    #Definimos el constructor de la clase
    ##############################################################################################################      
    def __init__(self):
        self.pantalla = pygame.display.set_mode( (ANCHO, ALTO) ) #Establecemos la pantalla del juego
        self.pantalla.fill( BACK_COLOR )                         #Pintamos la pantalla del juego del color del fondo
        self.juego=Linja()                                       #Establecemos en juego la clase Linja para poder aplicarle al juego la interfaz
        self.juego.inicio()                                      #Iniciamos Linja
        self.tablero =  self.juego.returnTablero()               #Obtenemos y guardamos el tablero de juego
        #Pintamos el display desde donde nos comunicaremos con el usuario
        pygame.draw.line( self.pantalla, COLOR_LINEA, (600, 785), (800, 785),15)    #Linea de borde Horizotal inferior
        pygame.draw.line( self.pantalla, COLOR_LINEA, (600, 0), (800, 0),30)        #Linea de borde Horizontal superior
        pygame.draw.line( self.pantalla, COLOR_LINEA, (790, 0), (790, 800),20)      #Linea de borde Lateral
        pygame.draw.rect(self.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0)  #Fondo del display
    ##############################################################################################################
    
    #Definimos un metodo que escribira un string que le pasemos en la posicion que le pasemos
    ##############################################################################################################
    def escribir(self,text1,pos,color,tamaño):
        fuente = pygame.font.Font('freesansbold.ttf', tamaño) # Escogemos la fuente y el tamaño en el que escribiremos
        text = fuente.render(text1, True, color)  #Renderizamos el texto en la fuente y tamaño escogido
        textRect = text.get_rect()                      #Guardamos el rectangulo del texto
        textRect.center = (pos[0], pos[1])              #Escogemos donde queremos que aparezca
        self.pantalla.blit(text, textRect)              #Lo enseñamos por pantalla
    ##############################################################################################################
     
    #Definimos un metodo que dibuje las lineas del tablero
    ##############################################################################################################    
    def dibujLineas(self):
        pygame.draw.line( self.pantalla, COLOR_LINEA, (0, 0), (600, 0), LIN_ANCHO )
        pygame.draw.line( self.pantalla, COLOR_LINEA, (0, 0), (0, ALTO), LIN_ANCHO )
        for i in range(FILAS):  #Dibujamos tantas lineas horizontales como filas haya en el tablero
            #Pintamos la linea en la pantalla del color escogido, estableciendo la cordenada de incio y la de final y el ancho de la linea
            pygame.draw.line( self.pantalla, COLOR_LINEA, (0, (i+1)*CELDA_SIZ), (600, (i+1)*CELDA_SIZ), LIN_ANCHO )
        for i in range(COLUMNAS): #Dibujamos tantas lineas verticales como columnas haya en el tablero
            #Pintamos la linea en la pantalla del color escogido, estableciendo la cordenada de incio y la de final y el ancho de la linea
            pygame.draw.line( self.pantalla, COLOR_LINEA, ((i+1)*CELDA_SIZ, 0), ((i+1)*CELDA_SIZ, ALTO), LIN_ANCHO )
    ##############################################################################################################
     
    #Definimos un metodo que dibuje las fichas en el tablero   
    ##############################################################################################################
    def dibujFichas(self):
        for row in range(FILAS): #Recorremos el tablero
            for col in range(COLUMNAS):
                if self.tablero[row][col] == 1: #Si hay un 1 en el tablero dibujamos una ficha negra
                    pygame.draw.circle( self.pantalla, GRIS, (int( (col * CELDA_SIZ + CELDA_SIZ//2)+2 ), int( row * CELDA_SIZ + CELDA_SIZ//2 )), RADIO_CIRC, ANCHO_CIRC )
                    pygame.draw.circle( self.pantalla, JUGADOR1_COLOR, (int( (col * CELDA_SIZ + CELDA_SIZ//2)-5 ), int( row * CELDA_SIZ + CELDA_SIZ//2 )), RADIO_CIRC, ANCHO_CIRC )
                    
                elif self.tablero[row][col] == 2: #Si hay un 2 en el tablero dibujamos una ficha roja
                    pygame.draw.circle( self.pantalla, ROJO, (int( (col * CELDA_SIZ + CELDA_SIZ//2)+2 ), int( row * CELDA_SIZ + CELDA_SIZ//2 )), RADIO_CIRC, ANCHO_CIRC )
                    pygame.draw.circle( self.pantalla, JUGADOR2_COLOR, (int( (col * CELDA_SIZ + CELDA_SIZ//2)-5 ), int( (row * CELDA_SIZ + CELDA_SIZ//2 ))), RADIO_CIRC, ANCHO_CIRC )
                else: #Si no hay ninguno de los dos borramos lo que haya en esa casilla 
                    pygame.draw.circle( self.pantalla, BACK_COLOR, (int( (col * CELDA_SIZ + CELDA_SIZ//2)+2 ), int( row * CELDA_SIZ + CELDA_SIZ//2 )), RADIO_CIRC, ANCHO_CIRC ) 
                    pygame.draw.circle( self.pantalla, BACK_COLOR, (int( (col * CELDA_SIZ + CELDA_SIZ//2)-5 ), int( row * CELDA_SIZ + CELDA_SIZ//2 )), RADIO_CIRC, ANCHO_CIRC )
    ##############################################################################################################

    #Definimos una función para mostrar de manera visual la selcción de la ficha
    ##############################################################################################################
    def fichaSelect(self,fila,col):
        pygame.draw.rect(self.pantalla, pygame.Color('yellow'), (int( (col * CELDA_SIZ+9 ) ), int( fila * CELDA_SIZ+9 ),CELDA_SIZ-18,CELDA_SIZ-18), 0)  #Fondo del display
    ##############################################################################################################
    
    #Deinimos una funcion para deseleccionar la ficha
   ##############################################################################################################
    def unfichaSelect(self,fila,col):
        pygame.draw.rect(self.pantalla, BACK_COLOR, (int( (col * CELDA_SIZ+9 ) ), int( fila * CELDA_SIZ+9 ),CELDA_SIZ-18,CELDA_SIZ-18), 0)  #Fondo del display
    ##############################################################################################################
    
    #Definimos el primer modo de juego jugador contra jugador
    ##############################################################################################################
    def juego1(self):
        cordenadaOrigen=None #Declaramos la variable para guardar la posición de la ficha que querremos mover
        cordenadaFinal=None #Declaramos la variable para gaurdar la posición a la que querremos mover la ficha
        comprobadorFinal=True #Declaramos la variable que parara el juego en caso de que terminemos
        while True:
            for event in pygame.event.get(): #Cada vez que se recoge un evento generado por el usuario hacemos una de 3 cosas
                if event.type == pygame.QUIT: #En caso de que el usuario cierre la ventana finalizamos el programa
                    sys.exit()               

                if event.type == pygame.MOUSEBUTTONDOWN and comprobadorFinal : #Si el usuario ha clicado el raton 

                    mouseX = event.pos[0] #Recogemos la posición X del raton en el momento del Click
                    mouseY = event.pos[1] #Recogemos la posición Y del raton en el momento del click

                    filaClick = int(mouseY // CELDA_SIZ) #Adaptamos la posición Y recogida a la Fila del tablero
                    colClick = int(mouseX // CELDA_SIZ)  #Adaptamos la posición X recogida a la columan del tablero
                    if(cordenadaOrigen==None): #Si no se ha seleccionado una ficha a mover todavia
                        if(self.juego.isInBounds(filaClick,colClick)):    
                            if(self.juego.tablero[filaClick,colClick]==self.juego.turno):
                                cordenadaOrigen=[filaClick,colClick] #Guardamos la casilla seleccionada como casilla del movimiento origen
                                self.fichaSelect(filaClick,colClick)
                                pygame.display.update()
                    else: #En caso de tener una ya seleccionada 
                        cordenadaFinal=[filaClick,colClick] #Guardamos la posicion a la que queremos mover la ficha
                        cond=self.juego.moveArbitrado(cordenadaOrigen,cordenadaFinal) #Movemos la ficha
                        if(not cond): 
                            self.escribir("No puedes mover" ,[697,250],COLOR_LINEA,18)
                            self.escribir("la ficha ahí",[698,269],COLOR_LINEA,18)
                            pygame.display.update()
                            time.sleep(1.2)
                        self.unfichaSelect(cordenadaOrigen[0],cordenadaOrigen[1])
                        cordenadaOrigen=None #Volvemos a vaciar la variable que guarda la ficha a mover
                        
                    
                    print(self.juego.tablero) #Imprimimos por consola el tablero de juego para poder asegurarnos que todo funciona bien
                    self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                    #Actualizamos el display de comunicación con el usuario
                    self.dibujDisplay()
                    if(self.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                        comprobadorFinal=self.rutinaFinJuegos()  

                if event.type == pygame.KEYDOWN: #Si el usuario ha pulsado una tecla
                    if event.key == pygame.K_r: #Si esa tecla es la R reinicia el juego
                        self.juego.inicio()


                pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
    ##############################################################################################################

    #Definimos función para ejecutar el segundo modo de juego
    ##############################################################################################################
    def juego2(self):
        inteligencia=Inteligente()
        cordenadaOrigen=None #Declaramos la variable para guardar la posición de la ficha que querremos mover
        cordenadaFinal=None #Declaramos la variable para gaurdar la posición a la que querremos mover la ficha
        comprobadorFinal=True #Declaramos la variable que parara el juego en caso de que terminemos
        while True:
            if(self.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                comprobadorFinal=self.rutinaFinJuegos()    
            if self.juego.turno==1 and comprobadorFinal:
                turnotemp=self.juego.turno #Guardamos el turno de inicio de la
                start=time.time()    #Guardamos el tiempo de inicio el contador de tiempo
                movientoOrdenador=inteligencia.jugarTurnoOrdenador(self.juego) #Hacemos que la ia haga su turno
                end=time.time()     #Guardamos el tiempo de final el contador de tiempo
                tot=end-start       #Los restamos
                print(tot)          #Imprimimos el tiempo de ejecución
                self.juego.moveArbitrado(movientoOrdenador[0],movientoOrdenador[1]) #Movemos la ficha con los movimientos de la ia
                self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                self.dibujDisplay()
                pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
                time.sleep(2)
                if(turnotemp==self.juego.turno):
                    self.juego.moveArbitrado(movientoOrdenador[2],movientoOrdenador[3])
                    self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                    self.dibujDisplay()
                    pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
                    
                if(self.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                       comprobadorFinal=self.rutinaFinJuegos()  
            for event in pygame.event.get(): #Cada vez que se recoge un evento generado por el usuario hacemos una de 3 cosas
                if event.type == pygame.QUIT: #En caso de que el usuario cierre la ventana finalizamos el programa
                    sys.exit()               
                if self.juego.turno==2:
                    if event.type == pygame.MOUSEBUTTONDOWN and comprobadorFinal : #Si el usuario ha clicado el raton 
                    
                        mouseX = event.pos[0] #Recogemos la posición X del raton en el momento del Click
                        mouseY = event.pos[1] #Recogemos la posición Y del raton en el momento del click

                        filaClick = int(mouseY // CELDA_SIZ) #Adaptamos la posición Y recogida a la Fila del tablero
                        colClick = int(mouseX // CELDA_SIZ)  #Adaptamos la posición X recogida a la columan del tablero
                        if(cordenadaOrigen==None): #Si no se ha seleccionado una ficha a mover todavia
                            if(self.juego.isInBounds(filaClick,colClick)):    
                                if(self.juego.tablero[filaClick,colClick]==self.juego.turno):
                                    cordenadaOrigen=[filaClick,colClick] #Guardamos la casilla seleccionada como casilla del movimiento origen
                                    self.fichaSelect(filaClick,colClick)
                                    pygame.display.update()  
                        else: #En caso de tener una ya seleccionada 
                            cordenadaFinal=[filaClick,colClick] #Guardamos la posicion a la que queremos mover la ficha
                            cond=self.juego.moveArbitrado(cordenadaOrigen,cordenadaFinal) #Movemos la ficha
                            if(not cond): 
                                self.escribir("No puedes mover" ,[697,250],COLOR_LINEA,18)
                                self.escribir("la ficha ahí",[698,269],COLOR_LINEA,18)
                                pygame.display.update()
                                time.sleep(1.2)
                            self.unfichaSelect(cordenadaOrigen[0],cordenadaOrigen[1])
                            cordenadaOrigen=None #Volvemos a vaciar la variable que guarda la ficha a mover
                            
                    
                        self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                        #Actualizamos el display de comunicación con el usuario
                        self.dibujDisplay()
             
                if event.type == pygame.KEYDOWN: #Si el usuario ha pulsado una tecla
                    if event.key == pygame.K_r: #Si esa tecla es la R reinicia el juego
                        self.juego.inicio()
            
                pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
    ##############################################################################################################
    
    #Definimo el metodo del terecer modo de juego
    ##############################################################################################################
    def juego3(self):
        comprobadorFinal=True #Declaramos la variable que parara el juego en caso de que terminemos
        inteligencia=Inteligente()
        self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
        self.dibujDisplay()
        pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
        while True:
            if(comprobadorFinal):    
                turnotemp=self.juego.turno
                movientoOrdenador=inteligencia.jugarTurnoOrdenador(self.juego)
                self.juego.moveArbitrado(movientoOrdenador[0],movientoOrdenador[1])
                self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                self.dibujDisplay()
                pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
                time.sleep(1
                           )
                if(turnotemp==self.juego.turno):
                    self.juego.moveArbitrado(movientoOrdenador[2],movientoOrdenador[3])
                    self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                    self.dibujDisplay()
                    pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
                    
                
                    
                print(self.juego.tablero) #Imprimimos por consola el tablero de juego para poder asegurarnos que todo funciona bien
                self.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                self.dibujDisplay()
                if(self.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                    comprobadorFinal=self.rutinaFinJuegos()  
                             
            for event in pygame.event.get(): #Cada vez que se recoge un evento generado por el usuario hacemos una de 3 cosas
                    if event.type == pygame.QUIT: #En caso de que el usuario cierre la ventana finalizamos el programa
                        sys.exit()              
                    if event.type == pygame.KEYDOWN: #Si el usuario ha pulsado una tecla
                        if event.key == pygame.K_r: #Si esa tecla es la R reinicia el juego
                            self.juego.inicio()


            pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
    ##############################################################################################################
    
    #Definimos la función que ira actualizando el display
    ##############################################################################################################
    def dibujDisplay(self):
        pygame.draw.rect(self.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0)
        if(self.juego.turno==1):
            self.escribir(self.juego.getTurno(),[695,450],JUGADOR1_COLOR,23) #Escribimos el Turno al que le toca jugar
        else:
            self.escribir(self.juego.getTurno(),[693,350],JUGADOR2_COLOR,23) #Escribimos el Turno al que le toca jugar
        
        # Escribimos cuantas casillas se puede mover la siguiente ficha
        self.escribir("Movimientos:{}".format(self.juego.movimiento),[695,400],COLOR_LINEA,20) 
        # Escribimos cuantas fichas Rojas hay en la ultima fila
        self.escribir("Fichas en la ultima fila",[690,100],JUGADOR2_COLOR,15)
        self.escribir("Rojas: {}".format(self.juego.contadorFin2),[700,115],JUGADOR2_COLOR,15)
        # Escribimos cuantas fichas Negras hay en la ultima fila
        self.escribir("Fichas en la ultima fila",[690,700],JUGADOR1_COLOR,15)
        self.escribir("Negras: {}".format(self.juego.contadorFin1),[700,715],JUGADOR1_COLOR,15)
        self.juego.countInteligente() #Contamos los puntos de los dos jugadores
        #Imprimimos por pantalla los puntos de ambos jugadores
        self.escribir("Puntos Fichas ",[690,655],JUGADOR1_COLOR,15)
        puntos=self.juego.countInteligente()
        self.escribir("Negras: {}".format(puntos[0]),[690,670],JUGADOR1_COLOR,15)
        self.escribir("Puntos Fichas ",[690,145],JUGADOR2_COLOR,15)
        self.escribir("Rojas: {}".format(puntos[1]),[690,160],JUGADOR2_COLOR,15)
    ##############################################################################################################

    #Definimos la función que ejecutará la rutina de fin de juego
    ##############################################################################################################
    def rutinaFinJuegos(self):
        pygame.draw.rect(self.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0) 
        self.escribir("Fin del juego",[697,400],COLOR_LINEA,25)
        self.juego.count() #Contamos cuantos puntos tiene cada jugador
        #Imprimimos por pantalla los puntos de ambos jugadores
        self.escribir("Puntos Fichas ",[690,655],JUGADOR1_COLOR,15)
        self.escribir("Negras: {}".format(self.juego.contador1),[690,670],JUGADOR1_COLOR,15)
        self.escribir("Puntos Fichas ",[690,145],JUGADOR2_COLOR,15)
        self.escribir("Rojas: {}".format(self.juego.contador2),[690,160],JUGADOR2_COLOR,15)
        #Comprobamos ganador para enseñarlo por pantalla
        if(self.juego.contador2>self.juego.contador1): #Si el jugador Rojo tiene mas puntos
            self.escribir("GANADOR:",[700,450],JUGADOR2_COLOR,25)
            self.escribir("ROJO",[700,480],JUGADOR2_COLOR,25)
        elif(self.juego.contador2<self.juego.contador1): #Si el jugador Negro tiene mas puntos
            self.escribir("GANADOR:",[700,450],JUGADOR1_COLOR,25)
            self.escribir("NEGRO",[700,480],JUGADOR1_COLOR,25)
        else:
        #Si tienen los mismos puntos
            self.escribir("Empate entre los ",[700,450],COLOR_LINEA,15)
            self.escribir("dos jugadores",[700,465],COLOR_LINEA,15)
        return False
    ##############################################################################################################

    #Definimos el metodo de la rutina, de inicio
    ##############################################################################################################
    def rutinaInicio(self):
        self.pantalla.fill(pygame.Color('LightBlue'))
        self.escribir("Escoge el Modo de juego",[400,50],COLOR_LINEA,15) 
        pygame.draw.rect(self.pantalla, pygame.Color('Grey'), (90, 90, 620, 120), 0)  
        pygame.draw.rect(self.pantalla, pygame.Color('white'), (100, 100, 600, 100), 0) 
        self.escribir("Jugador Contra Jugador",[400,150],COLOR_LINEA,15) 
        pygame.draw.rect(self.pantalla, pygame.Color('Grey'), (90, 290, 620, 120), 0)  
        pygame.draw.rect(self.pantalla, pygame.Color('white'), (100, 300, 600, 100), 0) 
        self.escribir("Jugador Contra IA",[400,350],COLOR_LINEA,15) 
        pygame.draw.rect(self.pantalla, pygame.Color('Grey'), (90, 490, 620, 120), 0)  
        pygame.draw.rect(self.pantalla, pygame.Color('white'), (100, 500, 600, 100), 0) 
        self.escribir("IA VS IA",[400,550],COLOR_LINEA,15) 
        pygame.display.update()
        comprobadorInicio=True
        modoDeJuego=None
        while(comprobadorInicio):
            for event in pygame.event.get(): #Cada vez que se recoge un evento generado por el usuario hacemos una de 3 cosas
                if event.type == pygame.QUIT: #En caso de que el usuario cierre la ventana finalizamos el programa
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN and comprobadorFinal : #Si el usuario ha clicado el raton 
                    mouseX = event.pos[0] #Recogemos la posición X del raton en el momento del Click
                    mouseY = event.pos[1] #Recogemos la posición Y del raton en el momento del click
                    if mouseX>90 and mouseX<620:
                        if mouseY>90 and mouseY<210:
                            modoDeJuego=1 #Jugador contra Jugador
                            comprobadorInicio=False
                        elif mouseY>290 and mouseY<410:
                            modoDeJuego=2 #Jugador contra IA
                            comprobadorInicio=False
                        elif mouseY>490 and mouseY<610:
                            modoDeJuego=3 #IA contra IA
                            comprobadorInicio=False
        return modoDeJuego

###########################################################################################################################################
#Runer Code    
#Declaramos las variables que utilizaremos
cordenadaOrigen=None #Declaramos la variable para guardar la posición de la ficha que querremos mover
cordenadaFinal=None #Declaramos la variable para gaurdar la posición a la que querremos mover la ficha
comprobadorFinal=True #Declaramos la variable que parara el juego en caso de que terminemos
interfaz=Ui()   #Declaramos e inicializamos la interfaz que usaremos
modoDeJuego=interfaz.rutinaInicio()          
interfaz=Ui()   #Reiniciamos las UI
interfaz.dibujLineas() #Dibujamos las lineas en el tablero
interfaz.dibujFichas() #Dibujamos las fichas en el tablero
interfaz.dibujDisplay()
if(modoDeJuego==1):#Modo jugador contra jugador
    interfaz.juego1()
elif(modoDeJuego==2): #Modo de juego de jugador contra IA
    interfaz.juego2()
elif(modoDeJuego==3): #Modo de juego de IA contra IA
    interfaz.juego3()
else:
    print("Error en la selcción de juego")