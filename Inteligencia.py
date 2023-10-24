## Author: Álvaro Villar Val
## Nombre: Inteligencia
## Version: 0.4
## Fecha: 18/10/2023
#Declaramos los imports
import numpy as np
from Linja import Linja


class Inteligente():
    #Definimos el constructor de la clase objeto
    ############################################################################################################## 
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)
    #############################################################################################################              
                     
    #Definimos las función del turno del ordenador
    #############################################################################################################
    def jugarTurnoOrdenador(self,juego:Linja):
        hijoOptimo=self.minMax(juego,0,juego.turno)
        movimientoOptimo=[hijoOptimo[1],hijoOptimo[2]]
        return movimientoOptimo
    #############################################################################################################

    #Definimos una funcion  que mueva la ficha al primer sitio que encuentre que no este en la lista de excluisiones
    #############################################################################################################
    def moverPrimerSitio(self,juego:Linja,origen,excluidos):
        if(juego.movimiento==0):
            for i in range (6):
                if ([origen[0]+1,i] not in excluidos):
                    if(juego.moveArbitrado(origen,[origen[0]+1,i])):
                        return [origen[0]+1,i]
        else:
            for i in range (6):
                if([origen[0]+juego.movimiento,i] not in excluidos):
                    if(juego.moveArbitrado(origen,[origen[0]+juego.movimiento,i])):
                        return [origen[0]+juego.movimiento,i]
        return False

    def posPrimFich(self,juego:Linja,excluidos):
        for j in range(1,8):
            for i in range(6):
                if [j,i] not in excluidos:
                    if(juego.turno==2):
                        if(j):
                            if(juego.tablero[j][i]==2):
                                return [j,i]
                    else:
                        if(j):
                            if(juego.tablero[7-j][5-i]==1):
                                return [j,i]
        return False
    #############################################################################################################

    #Definimos la función minMax que hara el algoritmo minMax y devolvera el mejor movimiento posible para el turno 
    # que lo llama
    #############################################################################################################
    def minMax(self, estadoPap:Linja,prof,turnOrg):
        if(prof<2):
            hijos=[]
            for i in range(6):
                comprobador=True
                origExcluido=[]
                destExluido=[]
                counts=[]
                while(comprobador):
                    cordFich=self.posPrimFich(self,estadoPap,origExcluido)
                    if(cordFich==False):
                        print("Error en Max")
                    temp=estadoPap
                    destino=self.moverPrimerSitio(temp,cordFich,destExluido)
                    if(destino==False):
                        origExcluido.append(cordFich)
                    hijo=[temp,cordFich,destino,temp.countInteligente()[turnOrg-1]]
                    if(hijo[3] not in counts):
                        hijos.append(hijo)
                        comprobador=False
                    destExluido.append(hijo[2]) 
            if(estadoPap.turno==turnOrg):
                minHijos=[]
                maxHijo=[temp,cordFich,destino,-100000]
                comprobador=True           
                for i in range(len(hijos)):
                    hijos[i].changeTurn()
                    minHijos[i]=self.minMax(hijos[i],prof+1,turnOrg)
                    for temp in minHijos:
                        if(maxHijo[3]<=temp[3]):
                            maxHijo=temp
                            comprobador=False
                if(comprobador):
                    print("Error en mini en busqueda del min")
                    return 0
                return maxHijo
            else:
                maxHijos=[]
                minHijo=[temp,cordFich,destino,100000]
                comprobador=True           
                for i in range(len(hijos)):
                    hijos[i].changeTurn()
                    maxHijos[i]=self.minMax(hijos[i],prof+1,turnOrg)
                    for temp in maxHijos:
                        if(minHijo[3]>=temp[3]):
                            minHijo=temp
                            comprobador=False
                if(comprobador):
                    print("Error en mini en busqueda del min")
                    return 0
                return minHijo
            
        else:
            return estadoPap
    #############################################################################################################
###############################################################################################################################
#Runer Code
   