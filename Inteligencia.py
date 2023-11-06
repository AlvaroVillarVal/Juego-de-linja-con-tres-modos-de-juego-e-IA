## Author: Álvaro Villar Val
## Nombre: Inteligencia
## Version: 0.6
## Fecha: 30/10/2023
#Declaramos los imports
import numpy as np
from Linja import Linja
import copy
#To do cortes alpha beta
class Inteligente():
    #Definimos el constructor de la clase objeto
    ############################################################################################################## 
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)
    #############################################################################################################              
                     
    #Definimos las función del turno del ordenador
    #############################################################################################################
    def jugarTurnoOrdenador(self,juego:Linja):
        hijoOptimo=self.minMax([juego,0,0,0,0,0],0,juego.turno)
        movimientoOptimo=[hijoOptimo[1],hijoOptimo[2],hijoOptimo[4],hijoOptimo[5]]
        return movimientoOptimo
    #############################################################################################################

    #Definimos una funcion  que mueva la ficha al primer sitio que encuentre que no este en la lista de excluisiones
    #############################################################################################################
    def moverPrimerSitio(self,juego:Linja,origen,excluidos):
        movimientoTemp=juego.movimiento
        if juego.turno==1:    
            if(juego.movimiento==0):
                for i in range (6):
                    if ([origen[0]+1,i] not in excluidos):
                        if(juego.moveArbitrado(origen,[origen[0]+1,i])):
                            return [origen[0]+1,i]
            else:
                for i in range (6):
                    if([origen[0]+juego.movimiento,i] not in excluidos):
                        if(juego.moveArbitrado(origen,[origen[0]+juego.movimiento,i])):
                            return [origen[0]+movimientoTemp,i]
        else:
            if(juego.movimiento==0):
                for i in range (6):
                    if ([origen[0]-1,i] not in excluidos):
                        if(juego.moveArbitrado(origen,[origen[0]-1,i])):
                            return [origen[0]-1,i]
            else:
                for i in range (6):
                    if([origen[0]-juego.movimiento,i] not in excluidos):
                        if(juego.moveArbitrado(origen,[origen[0]-juego.movimiento,i])):
                            return [origen[0]-movimientoTemp,i]
        return False

    def posPrimFich(self,juego:Linja,excluidos):
        for j in range(1,8):
            for i in range(6):
                
                if(juego.turno==2):
                    if [j,i] not in excluidos:
                        if(j):
                            if(juego.tablero[j][i]==2):
                                return [j,i]
                else:
                    if [7-j,5-i] not in excluidos:
                        if(j):
                            if(juego.tablero[7-j][5-i]==1):
                                return [7-j,5-i]
        return False
    #############################################################################################################

    def placeHolder(self,pap,turnOrg):
            estadoPap=pap[0]
            hijos=[]
            origExcluido=[]
            counts=[]
            destExluido=[]
            for i in range(2):
                comprobador=True
                while(comprobador):
                    cordFich=self.posPrimFich(estadoPap,origExcluido)
                    if(cordFich==False):
                        print("Error en Max")
                        comprobador=False
                    else:
                        temp=copy.deepcopy(estadoPap)
                        destino=self.moverPrimerSitio(temp,cordFich,destExluido)
                        if(destino==False):
                            origExcluido.append(cordFich)
                            destExluido=[]
                        else:
                            hijo=[temp,cordFich,destino,temp.countInteligente()[turnOrg-1],[0,0],[0,0]]
                            if(hijo[3] not in counts):
                                hijos.append(hijo)
                                counts.append(hijo[3])
                                comprobador=False
                            destExluido.append(hijo[2])
            return hijos 
    #Definimos la función minMax que hara el algoritmo minMax y devolvera el mejor movimiento posible para el turno 
    # que lo llama
    #############################################################################################################
    def minMax(self, papa,prof,turnOrg):
        estadoPap=papa[0]
        if(prof<5):
            hijos=self.placeHolder(papa,turnOrg)
            if(estadoPap.turno==turnOrg):
                minHijos=[0] *len(hijos)
                maxHijo=[papa[0],[0,0],[0,0],-100000,[0,0],[0,0]]
                comprobador=True           
                for i in range(len(hijos)):
                    minHijos[i]=self.minMax(hijos[i],prof+1,turnOrg)
                for temp in minHijos:
                    if(temp!=0):
                        maxval=maxHijo[3]
                        maxVal2=temp[3]
                        if(maxval<=maxVal2):
                            maxHijo=copy.deepcopy(temp)
                            tempX=maxHijo[1]
                            tempY=maxHijo[2]
                            if(prof!=0):
                                maxHijo[4]=tempX
                                maxHijo[5]=tempY
                                maxHijo[1]=papa[1]
                                maxHijo[2]=papa[2]
                            

                            comprobador=False
                if(comprobador):
                    print("Error en mini en busqueda del min")
                    return 0
                return maxHijo
            else:
                maxHijos=[0] *len(hijos)
                minHijo=[papa[0],[0,0],[0,0],100000,[0,0],[0,0]]
                comprobador=True           
                for i in range(len(hijos)):
                    maxHijos[i]=self.minMax(hijos[i],prof+1,turnOrg)
                for temp in maxHijos:
                    if(temp!=0):
                        minval=minHijo[3]
                        minVal2=temp[3]
                        if(minval>=minVal2):
                            minHijo=copy.deepcopy(temp)
                            tempX=minHijo[1]
                            tempY=minHijo[2]
                            if(prof!=0):
                                minHijo[4]=tempX
                                minHijo[5]=tempY
                                minHijo[1]=papa[1]
                                minHijo[2]=papa[2]
                            comprobador=False
                if(comprobador):
                    print("Error en mini en busqueda del min")
                    return 0
                return minHijo
            
        else:
            return papa
    #############################################################################################################
###############################################################################################################################
#Runer Code
   