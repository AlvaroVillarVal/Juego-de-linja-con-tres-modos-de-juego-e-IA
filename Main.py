# ## Author: Álvaro Villar Val
## Nombre: Main
## Version: 1.0
## Fecha: 29/11/2023
#Declaramos los imports
from UI import Ui
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