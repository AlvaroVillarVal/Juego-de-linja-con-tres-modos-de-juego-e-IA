## Documentación del Código: Inteligencia

### Autor
- **Nombre:** Álvaro Villar Val

### Detalles del Código
- **Nombre del Módulo:** Inteligencia
- **Versión:** 1.0
- **Fecha:** 08/11/2023

### Descripción General
Este módulo implementa una clase `Inteligente` que utiliza algoritmos de inteligencia artificial, específicamente el algoritmo MinMax, para tomar decisiones en un juego de estrategia. La clase interactúa con el estado del juego y realiza movimientos óptimos basados en la evaluación de posibles escenarios futuros.

### Dependencias
- numpy
- Linja (un módulo personalizado)
- copy

### Clase: Inteligente
#### Métodos Principales
1. **Constructor (`__new__`):**
   - Inicializa una nueva instancia de la clase `Inteligente`.

2. **jugarTurnoOrdenador (`jugarTurnoOrdenador`):**
   - Realiza el turno del ordenador utilizando el algoritmo MinMax para determinar el movimiento óptimo.
   - Parámetros:
     - `juego`: Instancia del juego actual (tipo `Linja`).

3. **moverPrimerSitio (`moverPrimerSitio`):**
   - Mueve una ficha al primer sitio disponible que no esté en la lista de excluidos.
   - Parámetros:
     - `juego`: Instancia del juego actual (tipo `Linja`).
     - `origen`: Coordenadas de origen de la ficha.
     - `excluidos`: Lista de posiciones excluidas.

4. **posPrimFich (`posPrimFich`):**
   - Encuentra la primera posición a la que se pueda mover una ficha.
   - Parámetros:
     - `juego`: Instancia del juego actual (tipo `Linja`).
     - `excluidos`: Lista de posiciones excluidas.

5. **obtenerHijos (`obtenerHijos`):**
   - Genera posibles movimientos (hijos) a partir del estado actual del juego.
   - Parámetros:
     - `pap`: Estado actual del juego.
     - `turnOrg`: Turno original del juego.

6. **minMax (`minMax`):**
   - Implementa el algoritmo MinMax para determinar el mejor movimiento posible.
   - Parámetros:
     - `papa`: Estado actual del juego.
     - `prof`: Profundidad actual en el árbol de juego.
     - `turnOrg`: Turno original del juego.
     - `alfa`: Valor alfa para la poda Alfa-Beta.
     - `beta`: Valor beta para la poda Alfa-Beta.
     - `profMax`: Profundidad máxima del árbol de juego.

### Funcionalidades Adicionales
- El código incluye una serie de comprobaciones y ajustes para optimizar el rendimiento del algoritmo MinMax, como la poda Alfa-Beta.
- Se manejan diferentes escenarios y se toman en cuenta las restricciones del juego para realizar movimientos válidos.

### Observaciones
- Este módulo requiere una comprensión profunda del juego `Linja` y de cómo interactúan las fichas y los movimientos dentro de su tablero.
- La eficiencia del algoritmo depende en gran medida de la implementación del juego `Linja` y de cómo se manejan los estados y movimientos dentro de él.