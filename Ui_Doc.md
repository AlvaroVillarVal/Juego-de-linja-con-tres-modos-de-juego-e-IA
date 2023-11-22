## Documentación del Código

### Autor: Álvaro Villar Val
- **Nombre:** UI
- **Versión:** 1.0
- **Fecha:** 22/11/2023

### Descripción General
El código proporcionado es una implementación de una interfaz de usuario (UI) para un juego, utilizando la biblioteca Pygame. Incluye la definición de constantes, la creación de una clase `Ui`, y la implementación de varios métodos para manejar la lógica del juego y la interacción con el usuario.

### Importaciones
- `pygame`: Utilizada para la creación de interfaces gráficas y manejo de eventos.
- `sys`: Usado para operaciones relacionadas con el sistema, como salir del programa.
- `time`: Para manejar tiempos y retrasos en el juego.
- `Linja`: Clase que representa la lógica del juego (no se proporciona el código de esta clase).
- `Inteligente`: Clase que representa la inteligencia artificial del juego (no se proporciona el código de esta clase).

### Constantes
- Dimensiones de la pantalla, líneas delimitadoras, filas, columnas, tamaño de celdas y fichas.
- Colores utilizados en la interfaz.

### Clase `Ui`
#### Métodos
- `__new__`: Constructor de la clase objeto.
- `__init__`: Inicializa la pantalla del juego, el tablero y otros elementos visuales.
- `escribir`: Escribe texto en una posición específica de la pantalla.
- `dibujLineas`: Dibuja las líneas del tablero.
- `dibujFichas`: Dibuja las fichas en el tablero según su estado actual.
- `fichaSelect` y `unfichaSelect`: Métodos para seleccionar y deseleccionar fichas.
- `juego1`, `juego2`, `juego3`: Métodos que definen diferentes modos de juego (jugador vs jugador, jugador vs IA, IA vs IA).
- `dibujDisplay`: Actualiza el display con información relevante del juego.
- `rutinaFinJuegos`: Maneja la lógica de finalización del juego y muestra el ganador.
- `rutinaInicio`: Muestra la pantalla de inicio y permite la selección del modo de juego.

### Lógica del Juego
- El juego se maneja a través de eventos de Pygame, como clics del ratón y pulsaciones de teclas.
- Se implementan diferentes modos de juego, incluyendo interacción con una IA.
- Se actualiza constantemente el estado del juego y la interfaz gráfica para reflejar los movimientos de los jugadores y la IA.

### Observaciones
- El código es una implementación detallada de una interfaz gráfica para un juego de tablero, con soporte para diferentes modos de juego y una IA.
- Se hace uso intensivo de las capacidades gráficas de Pygame para dibujar elementos en la pantalla y manejar la interacción del usuario.

