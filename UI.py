# ## Author: Álvaro Villar Val
## Nombre: UI
## Version: 0.7
## Fecha: 11/10/2023
#Declaramos los imports
import pygame 
import sys
from Linja import Linja
from Inteligencia import Inteligente
#TO DO: Hacer que cuando se selccione una ficha esta se resalte(Dibujando una circulito blanco fino por encima),
#  hacer que salga por pantalla el hecho de que no se puede mover una ficha, No seleccionar una coordenada cuando 
# esta este vacia en la matriz,hacer pagina de inicio para seleccionar que modo jugar, hacer pantalla de final

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
    def escribir(self,text1,pos):
        fuente = pygame.font.Font('freesansbold.ttf', 15) # Escogemos la fuente y el tamaño en el que escribiremos
        text = fuente.render(text1, True, COLOR_LINEA)  #Renderizamos el texto en la fuente y tamaño escogido
        textRect = text.get_rect()                      #Guardamos el rectangulo del texto
        textRect.center = (pos[0], pos[1])              #Escogemos donde queremos que aparezca
        self.pantalla.blit(text, textRect)              #Lo enseñamos por pantalla
    ##############################################################################################################
     
    #Definimos un metodo que dibuje las lineas del tablero
    ##############################################################################################################    
    def dibujLineas(self):
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

###########################################################################################################################################
#Runer Code    
#Declaramos las variables que utilizaremos
cordenadaOrigen=None #Declaramos la variable para guardar la posición de la ficha que querremos mover
cordenadaFinal=None #Declaramos la variable para gaurdar la posición a la que querremos mover la ficha
comprobadorFinal=True #Declaramos la variable que parara el juego en caso de que terminemos
interfaz=Ui()   #Declaramos e inicializamos la interfaz que usaremos
interfaz.pantalla.fill(pygame.Color('LightBlue'))
interfaz.escribir("Escoge el Modo de juego",[400,50]) 
pygame.draw.rect(interfaz.pantalla, pygame.Color('Grey'), (90, 90, 620, 120), 0)  
pygame.draw.rect(interfaz.pantalla, pygame.Color('white'), (100, 100, 600, 100), 0) 
interfaz.escribir("Jugador Contra Jugador",[400,150]) 
pygame.draw.rect(interfaz.pantalla, pygame.Color('Grey'), (90, 290, 620, 120), 0)  
pygame.draw.rect(interfaz.pantalla, pygame.Color('white'), (100, 300, 600, 100), 0) 
interfaz.escribir("Jugador Contra IA",[400,350]) 
pygame.draw.rect(interfaz.pantalla, pygame.Color('Grey'), (90, 490, 620, 120), 0)  
pygame.draw.rect(interfaz.pantalla, pygame.Color('white'), (100, 500, 600, 100), 0) 
interfaz.escribir("IA VS IA",[400,550]) 
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
            

interfaz=Ui()   #Reiniciamos las UI
interfaz.dibujLineas() #Dibujamos las lineas en el tablero
interfaz.dibujFichas() #Dibujamos las fichas en el tablero
interfaz.escribir(interfaz.juego.getTurno(),[700,200]) #Escribimos el Turno al que le toca jugar
# Escribimos cuantas casillas se puede mover la siguiente ficha
interfaz.escribir("Movimientos:{}".format(interfaz.juego.movimiento),[700,400]) 
# Escribimos cuantas fichas Rojas hay en la ultima fila
interfaz.escribir("Fichas en la ultima fila",[690,100])
interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorFin2),[700,115])
# Escribimos cuantas fichas Negras hay en la ultima fila
interfaz.escribir("Fichas en la ultima fila",[690,700])
interfaz.escribir("Negras: {}".format(interfaz.juego.contadorFin1),[700,715])
interfaz.escribir("Puntos Fichas ",[690,655])
interfaz.escribir("Negras: {}".format(interfaz.juego.contadorTot1),[690,670])
interfaz.escribir("Puntos Fichas ",[690,145])
interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorTot2),[690,160])
#Empezamos el bucle de juego
if(modoDeJuego==1):
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
                    cordenadaOrigen=[filaClick,colClick] #Guardamos la casilla seleccionada como casilla del movimiento origen
                else: #En caso de tener una ya seleccionada 
                    cordenadaFinal=[filaClick,colClick] #Guardamos la posicion a la que queremos mover la ficha
                    interfaz.juego.moveArbitrado(cordenadaOrigen,cordenadaFinal) #Movemos la ficha
                    cordenadaOrigen=None #Volvemos a vaciar la variable que guarda la ficha a mover
                
                print(interfaz.juego.tablero) #Imprimimos por consola el tablero de juego para poder asegurarnos que todo funciona bien
                interfaz.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                #Actualizamos el display de comunicación con el usuario
                pygame.draw.rect(interfaz.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0) 
                interfaz.escribir(interfaz.juego.getTurno(),[700,200]) #Escribimos el Turno al que le toca jugar
                # Escribimos cuantas casillas se puede mover la siguiente ficha
                interfaz.escribir("Movimientos:{}".format(interfaz.juego.movimiento),[700,400]) 
                # Escribimos cuantas fichas Rojas hay en la ultima fila
                interfaz.escribir("Fichas en la ultima fila",[690,100])
                interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorFin2),[700,115])
                # Escribimos cuantas fichas Negras hay en la ultima fila
                interfaz.escribir("Fichas en la ultima fila",[690,700])
                interfaz.escribir("Negras: {}".format(interfaz.juego.contadorFin1),[700,715])
                interfaz.juego.countInteligente() #Contamos los puntos de los dos jugadores
                #Imprimimos por pantalla los puntos de ambos jugadores
                interfaz.escribir("Puntos Fichas ",[690,655])
                interfaz.escribir("Negras: {}".format(interfaz.juego.contadorTot1),[690,670])
                interfaz.escribir("Puntos Fichas ",[690,145])
                interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorTot2),[690,160])
                if(interfaz.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                    pygame.draw.rect(interfaz.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0) 
                    interfaz.escribir("Fin del juego",[700,400])
                    comprobadorFinal=False #Ponemos en False el comprobador por que se ha llegado a la situación final para que no recoja mas clicks
                    interfaz.juego.count() #Contamos cuantos puntos tiene cada jugador
                    #Imprimimos por pantalla los puntos de ambos jugadores
                    interfaz.escribir("Puntos Fichas ",[690,655])
                    interfaz.escribir("Negras: {}".format(interfaz.juego.contador1),[690,670])
                    interfaz.escribir("Puntos Fichas ",[690,145])
                    interfaz.escribir("Rojas: {}".format(interfaz.juego.contador2),[690,160])
                    #Comprobamos ganador para enseñarlo por pantalla
                    if(interfaz.juego.contador2>interfaz.juego.contador1): #Si el jugador Rojo tiene mas puntos
                        interfaz.escribir("El ganador es ",[700,450])
                        interfaz.escribir("el jugador Rojo",[700,465])
                    elif(interfaz.juego.contador2<interfaz.juego.contador1): #Si el jugador Negro tiene mas puntos
                        interfaz.escribir("El ganador es ",[700,450])
                        interfaz.escribir("el jugador Negro",[700,465])
                    else:
                    #Si tienen los mismos puntos
                        interfaz.escribir("Empate entre los ",[700,450])
                        interfaz.escribir("dos jugadores",[700,465])

            if event.type == pygame.KEYDOWN: #Si el usuario ha pulsado una tecla
                if event.key == pygame.K_r: #Si esa tecla es la R reinicia el juego
                    interfaz.juego.inicio()


            pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
elif(modoDeJuego==2): #Modo de juego de jugador contra IA
    contadorParte=0
    inteligencia=Inteligente()
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
                    cordenadaOrigen=[filaClick,colClick] #Guardamos la casilla seleccionada como casilla del movimiento origen
                else: #En caso de tener una ya seleccionada 
                    cordenadaFinal=[filaClick,colClick] #Guardamos la posicion a la que queremos mover la ficha
                    interfaz.juego.moveArbitrado(cordenadaOrigen,cordenadaFinal) #Movemos la ficha
                    cordenadaOrigen=None #Volvemos a vaciar la variable que guarda la ficha a mover
                    if contadorParte==0:
                        contadorParte+=1
                    elif contadorParte==1:
                        pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
                        movientoOrdenador=inteligencia.jugarTurnoOrdenador(interfaz.juego)
                        interfaz.juego.moveArbitrado(movientoOrdenador[0],movientoOrdenador[1])
                        interfaz.juego.moveArbitrado(movientoOrdenador[2],movientoOrdenador[3])
                        contadorParte=0
                
                print(interfaz.juego.tablero) #Imprimimos por consola el tablero de juego para poder asegurarnos que todo funciona bien
                interfaz.dibujFichas() #Dibujamos todas las fichas de nuevo para actualizar el momento de juego
                #Actualizamos el display de comunicación con el usuario
                pygame.draw.rect(interfaz.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0) 
                interfaz.escribir(interfaz.juego.getTurno(),[700,200]) #Escribimos el Turno al que le toca jugar
                # Escribimos cuantas casillas se puede mover la siguiente ficha
                interfaz.escribir("Movimientos:{}".format(interfaz.juego.movimiento),[700,400]) 
                # Escribimos cuantas fichas Rojas hay en la ultima fila
                interfaz.escribir("Fichas en la ultima fila",[690,100])
                interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorFin2),[700,115])
                # Escribimos cuantas fichas Negras hay en la ultima fila
                interfaz.escribir("Fichas en la ultima fila",[690,700])
                interfaz.escribir("Negras: {}".format(interfaz.juego.contadorFin1),[700,715])
                interfaz.juego.countInteligente() #Contamos los puntos de los dos jugadores
                #Imprimimos por pantalla los puntos de ambos jugadores
                interfaz.escribir("Puntos Fichas ",[690,655])
                interfaz.escribir("Negras: {}".format(interfaz.juego.contadorTot1),[690,670])
                interfaz.escribir("Puntos Fichas ",[690,145])
                interfaz.escribir("Rojas: {}".format(interfaz.juego.contadorTot2),[690,160])
                if(interfaz.juego.comprobarFin()): #Comprobamos si se ha llegado a la situación de final de juego
                    pygame.draw.rect(interfaz.pantalla, pygame.Color('White'), (607, 15, 173, 763), 0) 
                    interfaz.escribir("Fin del juego",[700,400])
                    comprobadorFinal=False #Ponemos en False el comprobador por que se ha llegado a la situación final para que no recoja mas clicks
                    interfaz.juego.count() #Contamos cuantos puntos tiene cada jugador
                    #Imprimimos por pantalla los puntos de ambos jugadores
                    interfaz.escribir("Puntos Fichas ",[690,655])
                    interfaz.escribir("Negras: {}".format(interfaz.juego.contador1),[690,670])
                    interfaz.escribir("Puntos Fichas ",[690,145])
                    interfaz.escribir("Rojas: {}".format(interfaz.juego.contador2),[690,160])
                    #Comprobamos ganador para enseñarlo por pantalla
                    if(interfaz.juego.contador2>interfaz.juego.contador1): #Si el jugador Rojo tiene mas puntos
                        interfaz.escribir("El ganador es ",[700,450])
                        interfaz.escribir("el jugador Rojo",[700,465])
                    elif(interfaz.juego.contador2<interfaz.juego.contador1): #Si el jugador Negro tiene mas puntos
                        interfaz.escribir("El ganador es ",[700,450])
                        interfaz.escribir("el jugador Negro",[700,465])
                    else:
                    #Si tienen los mismos puntos
                        interfaz.escribir("Empate entre los ",[700,450])
                        interfaz.escribir("dos jugadores",[700,465])

            if event.type == pygame.KEYDOWN: #Si el usuario ha pulsado una tecla
                if event.key == pygame.K_r: #Si esa tecla es la R reinicia el juego
                    interfaz.juego.inicio()


            pygame.display.update() #Actualizamos el display del juego para que el jugador vea su moviemiento
elif(modoDeJuego==3):
     print("Modo de juego 3")
else:
    print("Error en la selcción de juego")