<div style="text-align:center"><img src="https://i.imgur.com/J0JGm3I.jpg"/></div>

<div style="text-align:center"> <h1>Instituto Tecnologico de Buenos Aires</h1></div>
<div style="text-align:center"> <h2>Sistemas de Inteligencia Artificial</h2></div>
<div style="text-align:center"> <h2>Trabajo Practico 1</h1></div>

<div style="text-align:center;"><h1>Metodos de busqueda Desinformados e Informados</h1></div>

## Objetivos
Se debera crear un generador de soluciones para el juego Sokoban.
## Descripcion del juego
Se busca minimizar la cantidad de movimientos para resolver los escenarios del Sokoban.
Este juego sucede en un tablero con casilleros (discreto) de dos dimensiones. Se cuenta con un jugador,
paredes, cajas y objetivos. La cantidad de cajas equivale a la cantidad de objetivos. El jugador podra moverse en cualquiera de las 4 direcciones, siempre que no se encuentre una pared. El jugador puede empujar
las cajas, pero no tirar de ellas. Una caja A consecutiva a otra caja B se comporta como una pared si es
empujada en la direccion y sentido A →B . Un escenario se encontrara resuelto cuando todas las cajas se
encuentren en un objetivo.
Ejemplo. URL
## Descripcion del trabajo
Se debera realizar lo siguiente:
- Implementacion de las estrategias de busqueda no informadas: Depth-First Search, Breadth-First
Search e Iterative Deepening Depth-First Search.
- Implementacion de las estrategias de busquedas informadas: Global Greedy Search, A* e Iterative
Deepening A*.
- Desarrollo de al menos 3 heurısticas. Dichas heurısticas deben ser no triviales y al menos dos de ellas
deben ser admisibles. De haber una heurıstica no admisible, se debera contar con una justificacion valida
para su inclusion y los casos de uso. El sistema debe poder ejecutar la busqueda utilizando cualquiera
de ellas.
- Implementacion de una funcion de costo.
- Para configurar los diferentes parametros del problema, deberan contar con la lectura de un archivo
de configuracion.
- El sistema debe exponer como resultado:
  - Parametros con los que se realizo la busqueda.
  - El resultado de la busqueda (exito/fracaso).
  - La profundidad de la solucion.
  - El costo obtenido de la solucion.
  - Cantidad de nodos expandidos (al finalizar).
  - Cantidad de nodos frontera (al finalizar).
  - Solucion (estado inicial + estados intermedios + estado final)
  - Tiempo de procesamiento.

No esta permitido el uso de librerıas externas sin el consentimiento de la catedra.

## Repositorio
Cada grupo contara con un repositorio para la entrega del trabajo, donde debe encontrarse todo el material
entregado. La direccion de acceso tambien se publicara en el campus. Generar una carpeta para el
TP1 dentro del repositorio. De esta forma, podremos ordenadamente agregar carpetas con las entregas
siguientes.
## Forma de entrega
- Crear el tag TP1 (respetar las mayusculas) en el repositorio con el trabajo completo. Los contenidos
deben contar con:
  - Todo lo mencionado en la seccion Descripcion del trabajo.
  - Codigo fuente del trabajo.
  - Binarios ejecutables (incluyendo librerıas, plugins y todo lo necesario para su funcionamiento).
  - Documento de la presentacion oral (ppt, pps, pdf, etc.)
  - Un README con la descripcion detallada de los procedimientos para compilar y ejecutar el
sistema; y al menos dos configuraciones de ejecucion que se crean oportunas.
## Presentacion oral
Cada grupo realizara una presentacion oral de 15 minutos (como maximo), donde resumira el trabajo realizado, detallara los resultados obtenidos y explicara las conclusiones a las que llego. Ademas deberan responder
las preguntas que los docentes formulen. Los docentes podran pedir que se hagan corridas en vivo modificando cualquier parametro del programa. No incluir la descripcion del juego en la presentacion. Todos los
alumnos del grupo deberan participar equitativamente de la presentacion.

## Fecha y horario de entrega
Entrega digital: 7 de Abril del 2020 a las 08:59hs
Presentacion oral: 7 de Abril del 2020 a las 09:00hs