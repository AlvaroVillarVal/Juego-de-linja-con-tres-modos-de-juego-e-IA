# Practiga-grande-sistemas
## Requirements
Necesario pygames y numpy para funcionar
## Recomendations
### Inteligencia artificial con movimientos muy lentos
En caso de que los movimientos de la IA sean muy lentos, se recomienda cambiar en la clase inteligencia en la función: obtenerHijos (self,pap,turnOrg), en la linea 6 del metodo (Linea 96 del codigo), en "for i in range(3)" cambiar el 3 por un 2 reduciendo el numero de hijos por profundidad de 3 a 2, asi se pasaría de 3^8 comprobaciones de movimientos(6561) a 2^8 comprobaciones de movimientos(256), por movimiento.
### Utilización de un Ordenador no muy potente
En esta practica por cada turno que hace la IA se hace un minimax de Profundidad 8 y 3 hijos(a no ser que se haya reducido), esto significaría que por cada turno de la ia el ordenador tiene que realizar 6561 movimientos y situaciones del tablero, en caso de que este codigo se ejecute en un ordenador no muy potente, se recomienda empezar con 2 hijos en vez de 3 ya que funcionara mucho más rapido.
## BenchMark
### Especificaciones del Equipo
-Nombre del dispositivo	DESKTOP-A8SM0VB
-Procesador	Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz   2.59 GHz
-RAM instalada	16,0 GB (15,8 GB usable)
-Tipo de sistema	Sistema operativo de 64 bits, procesador basado en x64
-NVIDIA Geforce RTX 2060 with Max-Q Design
### Tiempo de ejecución de MinMax
#### Con 2 Hijos(256 movimientos)
-Tiempo de ejecución promedio: 0.115871000289917 
    1. 0.15234899520874023
    2. 0.109527587890625
    3. 0.10141110420227051
    4. 0.10474419593811035
    5. 0.11132311820983887

#### Con 3 Hijos(6561 movimientos)
-Tiempo de ejecución promedio: 0.8661438941955566
    1. 1.3217291831970215
    2. 1.274038314819336
    3. 0.6663672924041748
    4. 0.6165871620178223
    5. 0.4519975185394287
#### Con 4 Hijos(65536 movimientos)
-Tiempo de ejecución promedio: 1.0045984745025636
    1. 1.1756939888000488
    2. 1.2670965194702148
    3. 0.9569261074066162
    4. 1.1165244579315186
    5. 0.506751298904419
#### Con 5 Hijos(390625 movimientos)
-Tiempo de ejecución promedio: 9.452440786361695
    1. 13.147498369216919
    2. 10.030307531356812
    3. 9.989877939224243
    4. 10.149210691452026
    5. 3.9453094005584717
#### Con 6 Hijos(1679616 Movimientos)
-Tiempo de ejecución promedio: 12.413691902160645
    1. 20.155647039413452
    2. 16.790600061416626
    3. 8.656764507293701
    4. 7.022095203399658
    5. 9.443352699279785
### Con 7 Hijos (5764801 Movimientos)
-Tiempo de ejecución promedio: 19.155841684341432
    1. 22.301238775253296
    2. 28.91622805595398
    3. 19.976686239242554
    4. 8.801581859588623
    5. 15.783473491668701
### Con 8 Hijos (16777216 Movimientos)
-Tiempo de ejecución promedio: 18.536736059188843
    1. 23.667473316192627
    2. 27.135742664337158
    3. 18.99834942817688
    4. 12.860623598098755
    5. 10.021491289138794
### Con 9 Hijos (43046721 Movimientos)
-Tiempo de ejecución promedio: 19.78009386062622
    1. 23.205416202545166
    2. 27.856266975402832
    3. 18.007469654083252
    4. 18.161332368850708
    5. 11.669984102249146
### Con 10 Hijos (100000000 Movimientos)
-Tiempo de ejecución promedio: 18.004673290252686
    1. 22.946293592453003
    2. 19.276718139648438
    3. 9.696178197860718
    4. 17.0955491065979
    5. 21.00862741470337

### Analisis
Podemos ver que apartir de los 7 hijos no incrementa el tiempo de ejecución, esto imagino que se debe a que apartir de 7 movimientos no hay movimiento que den costes distintos, por ello hipotizo que hay alrededor de 7 movimientos den distintos costes, por eso no haria falta más de 6 hijos.


