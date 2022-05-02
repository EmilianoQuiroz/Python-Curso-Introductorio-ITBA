'''
Clase 1 :
    Introducción a la programación en Python.
    Variables.
    Operadores.
    Control de flujo (if, while, for).
    Funciones.
Clase 2 :
    Tipos de datos (int, float, string, boolean).
    Operaciones con tipos de datos.
    Listas.
    Operaciones con listas.
    Manipulación de archivos de texto.
Clase 3 :
    Estructuras de datos (Dictionary, Set, Tuple).
    Operaciones con estructuras de datos.
    Introducción a librerías y ejemplos.
    Casos de aplicación.
'''
'''
Introducción a la programación

La programación es el proceso que se utiliza para diseñar 
e implementar un programa de computadora, valiéndose de 
algún lenguaje que permita comunicar una serie de acciones 
que se requiere que la computadora realice. Podemos pensar 
que es una caja negra que recibe alguna información, la cual 
es llamada input (entrada), realiza alguna acción, y devuelve 
información, la cual es llamada output (salida).

Lenguajes de programación
Un lenguaje de programación es un lenguaje formal que proporciona 
una serie de instrucciones, las cuales permiten a un programador 
escribir secuencias de órdenes para controlar el comportamiento 
físico y lógico de una computadora, con el objetivo de que produzca 
diversas acciones deseadas por el programador (¡y los usuarios!).
Algunos de los lenguajes mas populares en los últimos tiempos 
(lejos de ser los únicos) son Python, Java, C++, JavaScript, PHP, etc.

¿Por qué Python?
Elegimos Python porque es uno de los lenguajes de programación con 
reglas más simples e intuitivas que existen; esto explica la creciente 
popularidad que ha tenido en los ultimos tiempos.
A pesar de su simpleza, es muy utilizado tanto en la industria para 
servidores y servicios web, así como también en el área académica 
para redes neuronales, deep learning, simulación, etc.
La comunidad de Python es una de las más grandes. Por lo tanto 
cualquier duda que tengan, a partir de ahora, Google es su amigo: 
pueden buscar la duda que tengan y seguramente alguien ya haya 
tenido ese problema. Una de los sitios web más conocidos para 
este fin es StackOverflow.
'''

#Input, Output y Variables
'''
Output
El output de un programa es la manera de transmitir información 
hacia el entorno externo. Por ejemplo, puede escribir en la consola 
de la computadora, puede generar una imagen, reproducir un sonido, 
etc. En Google Colaboratory veremos el output del programa debajo 
de la celda donde fue ejecutado.
Para poder mostrar texto, podemos utilizar la instrucción print( ) 
poniendo lo que deseemos mostrar entre los paréntesis. Más adelante 
veremos cómo se pueden generar imágenes, archivos y demás.
Tip: En la esquina superior izquierda del cuadro de texto con 
el código hay un botón para ejecutar el programa.
'''

print(123)
print("Hola, cómo estas?")
print('Buen día')

'''
Noten en el ejemplo que para escribir texto se debe indicar con 
comillas simples o dobles y para escribir números no se usan comillas.
Otra cosa importante para notar es que cada instrucción en Python se 
escribe en un renglón distinto, y se ejecutarán una por una de arriba para abajo.
Cada instrucción print( ) muestra el contenido indicado en un renglón nuevo, 
pero también admite mostrar mensajes en un mismo renglón si se indican 
diferentes parámetros separados con comas:
'''
print(1, 2, 3)
print("Curso", "de", "Python")
print('Uno:', 1, ' Dos:', 2, ' Tres:', 3)
'''
Variables
Para poder realizar tareas es necesario guardar en la memoria de la 
computadora los datos que necesita mi aplicación para funcionar. 
Por ejemplo, en este momento tu navegador web sabe cuántas pestañas 
hay abiertas y qué página se abrió en cada una, sabe en qué posición 
de la página estás y qué usuario utilizaste para entrar a Google Colab. 
Todos estos datos están almacenados en la memoria de la computadora y 
el navegador lee estos datos y los modifica cada vez que lo requiere.
En programación, se le asigna un nombre o apodo a cada pequeño segmento 
de la memoria que almacena un dato o un valor. De esta forma en el 
programa cada vez que se usa este nombre se esta refiriendo al valor 
del dato almacenado en la memoria. Este es el concepto de "variable".
En python esto se logra de la siguiente manera:
'''
x = 5
print(x)

'''
Este ejemplo utilizará un bloque de la memoria para almacenar el número 5, 
luego le asigna a este bloque el nombre x y por lo tanto a partir de entonces 
cada vez que se utiliza la palabra x en realidad nos referimos al valor 
almacenado dentro del bloque de memoria, al cual apodamos x.

¿Cómo se interpreta una expresión de asignación?
Es muy importante entender cómo leer una expresión de asignación. 
Cuando recorras y analices tu código, es preferible que entiendas 
el significado de la operación:

nombre = expresión

Como:
Se asigna el valor de expresión a nombre.
Y no como:
variable es igual a expresión.
Ejemplos
En estas variables podemos guardar lo que sea necesario para 
ejecutar el programa, por ejemplo si necesitamos guardar texto 
se indica con: "(texto)" o '(texto)'.

'''
x = 'Hola'
y = "Adios"
z = 123
print(x)
print(y)
print(z)

'''
Noten que la instrucción print( ) permite mostrar el contenido de una variable. 
Cuando ponemos print(x) no imprime la letra x sino que imprime el contenido de x. 
Es por esto que para eliminar la confusión se usan comillas cuando queremos mostrar 
texto y no el contenido de una variable.
Es importante tener en cuenta que no es necesario aclarar de antemano si las variables 
son textos (Strings) o números, el lenguaje lo puede identificar automáticamente

Reglas para el nombre de una variable:
Debe empezar con una letra (a-z, A-Z) o un guión bajo (_).
Los otros caracteres pueden ser letras, numeros o guión bajo.
Distingue mayúsculas de minúsculas.
Existen palabras reservadas que no se pueden usar como nombre de variable porque 
Python las usa para otras cosas. Por ejemplo el nombre de una variable no puede ser print.

Prolijidad y buenas prácticas.
Cuando se escribe código, no solamente se está utilizando un lenguaje de programación 
para poder aprovechar los recursos de una computadora. Al igual que cualquier otra 
actividad humana, la tarea de programar se vuelve más interesante cuando se realiza 
junto a otras personas.
De hecho, para realizar ciertos trabajos de mucha complejidad, no es posible que un 
único individuo se encargue de escribir todo el código. Por eso, es importante ser 
prolijos y utilizar buenas prácticas de programación, para que otras personas puedan 
entender nuestro código (incluído nuestro yo del futuro) y de esa forma corregirlo o 
agregarle funcionalidad.

Unos tips que ya pueden a empezar a usar son:
Separar el nombre de la variable, el operador de asignación y la expresión a evaluar con espacios.
Es decir, en lugar de escribir:

x="Hola mundo!"

Es mejor escribir:

x = "Hola mundo!"

Elegir nombres de variables descriptivos, aunque nos de pereza escribirlos.
radio = 5
pi = 3.14
perimetro = 2 * pi * radio
areaEsfera = 4 * pi * radio**2
volumenEsfera = 4 / 3 * pi * radio**3

Mini-desafío: Output y variables

Diseñar un programa en el cual se definan exactamente 2 variables.
La primera se debe llamar nombre y debe contener tu nombre (entre comillas).
La segunda se debe llamar edad y debe contener tu edad (como un número simple, sin comillas).
Por último el programa debe mostrar en pantalla la siguiente frase en una sóla línea:

(nombre) tiene (edad) años

Por ejemplo:

Mati tiene 5 años

Tip: La instrucción print() admite mostrar mensajes en un mismo renglón si se indican diferentes parámetros separados con comas.
'''

nombre = "Santiago"

edad = 23

print( nombre, " tiene ", edad, " años.")

'''
Input
El input de un programa es la manera de recibir información del entorno externo al programa. 
Esto puede ser un usuario, un archivo, otro programa, un sensor, etc.
Para ingresar una variable podemos usar input( "Texto a mostrar:" ). Corran este código 
ustedes para que les de una pequeña casilla donde escribir, y luego el programa escribirá 
lo que ustedes ingresaron.
'''
# Esto es un comentario!
# Los comentarios no son ejecutados por Python
# De esta forma el programador puede hacer una nota para humanos

nombre = input("Ingrese su nombre: ")
edad = int( input("Ingrese su edad: ") )

print("nombre:", nombre)
print("edad:", edad)

'''

Un detalle a tener en cuenta es que la información ingresada por el usuario usando input( ) 
será interpretada como texto, no como un número. Por eso cuando queremos ingresar un número 
usaremos int( ) para convertir ese texto al número correspondiente. En la próxima clase quedará 
claro por qué debemos hacer esto y qué es el tipo de una variable.

'''
#Operaciones básicas con variables Seguir



