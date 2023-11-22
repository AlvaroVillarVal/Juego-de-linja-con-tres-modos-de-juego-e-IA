## Documentación del Código: Linja

### Autor: Álvaro Villar Val
- **Nombre del Proyecto:** Linja
- **Versión:** 1.0
- **Fecha:** 8/11/2023

### Descripción General
El código implementa una clase llamada `Linja` que simula el juego de mesa del mismo nombre. La clase gestiona el estado del juego, incluyendo el tablero, el turno de los jugadores, y las reglas para mover las fichas.

### Importaciones
- `numpy` para manejar el tablero de juego como un array.

### Clase: Linja
#### Atributos
- `tablero`: Array de 8x6 representando el tablero del juego.
- `contadorTot1`, `contadorTot2`: Contadores de puntos para los jugadores negro y rojo.
- `contador1`, `contador2`: Contadores de puntos individuales para cada jugador.
- `contadorFin1`, `contadorFin2`: Contadores de fichas extras en las filas finales del tablero.
- `movimiento`: Indica la cantidad de movimiento permitido en el segundo turno.
- `turno`: Indica el turno actual (negro o rojo).
- `comprobadorTurno`: Verifica cuántos turnos consecutivos se han realizado.

#### Métodos
- `__new__`, `__init__`: Constructores de la clase.
- `inicio`: Establece el estado inicial del tablero.
- `valSum1`, `valSum2`: Calculan los puntos de las fichas negras y rojas.
- `valSum1Int`, `valSum2Int`: Calculan los puntos de las fichas para la función de coste.
- `returnTablero`: Devuelve el estado actual del tablero.
- `count`: Calcula los puntos totales de cada jugador.
- `countInteligente`: Calcula los puntos de manera inteligente, restando los puntos del oponente.
- `compare`: Compara dos estados del tablero.
- `countline`: Cuenta las fichas en una línea específica.
- `simpleMove`: Mueve una ficha de una posición a otra.
- `move`: Mueve una ficha y gestiona las fichas en las filas finales.
- `getTurno`: Devuelve el turno actual.
- `isEmpty`: Verifica si una posición está vacía.
- `getDistance`: Calcula la distancia entre dos posiciones.
- `isInBounds`, `areInBounds`: Verifican si las coordenadas están dentro del tablero.
- `changeTurn`: Cambia el turno actual.
- `isLegal`: Verifica si un movimiento es legal.
- `moveArbitrado`: Realiza un movimiento verificando su legalidad.
- `movimientoPosibleEnTurno`: Verifica si hay movimientos posibles en el turno actual.
- `gameOver`: Comprueba si el juego ha terminado.
- `comprobarFin`: Verifica si se ha alcanzado el estado final del juego.

### Detalles Adicionales
- El juego alterna entre dos jugadores, negro y rojo.
- Cada jugador mueve sus fichas según las reglas establecidas, buscando alcanzar la fila opuesta o capturar las fichas del oponente.
- El juego termina cuando un jugador no puede realizar más movimientos legales o se alcanza una configuración final específica en el tablero.

