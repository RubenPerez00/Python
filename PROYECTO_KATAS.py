from functools import reduce
from datetime import datetime


#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


def cadena_texto (texto):
    """Calcula la frecuencia de cada letra en una cadena de texto excluyendo espacios.

    Args:
        texto (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario con cada letra como clave y su frecuencia como
        valor.
    """

    frecuencias = {}

    for letra in texto:
# Recorremos la cadena con un bucle.  
     if letra != " ":
        # Ignoramos los espacios.
        if letra not in frecuencias:
         #Si la letra no está dentro del diccionario se añade con un 1.   
            frecuencias [letra] = 1
        else :
          #Si la letra esta dentro, se suma 1 al total.  
            frecuencias [letra] += 1
    return frecuencias


cadena = "buenos dias a tod@s"      

print(cadena_texto(cadena))
#Printamos el resultado que se ha ido guardando en el diccionario.

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def calcular_doble (num):
    """Calcula el doble de un número dado.

    Args:
        num (int | float): Número a multiplicar *2.

    Returns:
        int | float: El resultado de multiplicar *2.

    """
    return num*2
#Creamos una función donde cada número que pongamos se multiplique *2.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
#Creamos una lista con números aleatorios.
print (f"La lista original sin multiplicar *2 es {lista_numeros}")

resultado_map = map (calcular_doble, lista_numeros)
#Ponemos que el resultado map sea la función y se aplique a toda la lista de números.

lista_resultado_map = list(resultado_map)
#Hacemos que el resutlado del map se genere en una lista y al final lo printamos.
print (f"El resultado de la función map después de aplicar la función y convertirlo en lista es {lista_resultado_map}")


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras_objetivo(lista_palabras, palabra_objetivo):
   """Filtra una lista de palabras devolviendo aquellas que contienen la subcadena objetivo.

    Args:
        lista_palabras (list[str]): Lista de palabras donde realizar la
        búsqueda.
        palabra_objetivo (str): Subcadena que deben contener las palabras.

    Returns:
        list[str]: Lista con las palabras que contienen la palabra objetivo.
    """
   #Creamos la función con los requisitos que nos pide y a su vez creamos una lista vacía pra ir guardando el resultado.
   resultado = []

   for p in lista_palabras:
     #Recorremos cada palabra de la lista
    if palabra_objetivo in p:
      #Si se cumple la condición, añadimos la palabra en la lista vacía de 'resultado'.
     resultado.append(p) 

   return resultado

lista_ejemplo = ["caracol", "coliflor", "colonia", "berenjena", "colina", "nubes", "conocido"]
objetivo_ejemplo = "col"
#Creamos una lista con palabras aleatorias y también creamos una variable con lo que queremos buscar.
resultado_final = buscar_palabras_objetivo (lista_ejemplo, objetivo_ejemplo)
#Creamos una variable que sea el resultado final donde usamos la función que hemos creado y como parámetros definimos las variables que hemos creado de ejemplo.
print (resultado_final)




#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_lista (lista1, lista2):
    """Calcula elemento a elemento la diferencia resta entre dos listas de números.

    Args:
        lista1 (list[int | float]): Lista de números minuendos.
        lista2 (list[int | float]): Lista de números substraendos.

    Returns:
        list[int | float]: Lista con los resultados de la resta posición por
        posición.
    """
#Creamos una función para hacer la diferencia
    resultado_map = map(lambda x, y:x - y, lista1, lista2)
    #Usamos el map y lambda, como hay 2 listas usamos 'x' e 'y', y con el map le decimos que corresponden a las listas 1 y 2.

    return list(resultado_map)

lista_a = [40,50,60]
lista_b = [10,20,30]
#Creamos 2 listas como nos pide el ejercicio.
resultado_final = diferencia_lista (lista_a,lista_b)
#Aplicamos la funcion en ambas listas.
print (resultado_final)


#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#   que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas (lista_notas, nota_aprobado = 5):
    """Calcula la media de una lista de notas y determina si el alumno está aprobado o suspenso.

    Args:
        lista_notas (list[int | float]): Lista con las calificaciones numéricas.
        nota_aprobado (int | float, optional): Nota mínima para aprobar. Por
        defecto es 5.

    Returns:
        tuple[float, str]: Tupla con la nota media redondeada a 2 decimales y el
        estado ("Aprobado" o "Suspenso").
    """
    #Creamos la función y asignamos un valor fijo a nota aprobado.
    media = round (sum(lista_notas) / len(lista_notas),2)
    #Calculamos la media y redondeamos los decimales.(lo había probado sin el round y daban muchos decimales, cosa que no nos interesa)
    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    #Aplicamos una condición entre notas >=5 y notas <5.
    return (media,estado)
Nombre_alumno = "Gon Freecs"
notas_alumno1 = [2,8,9,4,3,10,7]
#Creamos una lista con las notas de un alumno.

resultado_final = evaluar_notas(notas_alumno1)
#Creamos una variable con el resultado final y lo printamos. Para que no salga (6.14, 'Aprobado') he elegido el orden 0 dentro del resultado final para que me saque solo la nota y el orden 1 para que solo me saque el estado y quede más legible.
print (f"El alumno {Nombre_alumno} tiene una nota media de {resultado_final[0]} por lo que está {resultado_final[1]}. ")



#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial (n):
    """Calcula el factorial de un número entero positivo de forma recursiva.

    Args:
        n (int): Número entero sobre el cual calcular el factorial.

    Returns:
        int: El factorial del número n.
    """
    if n==1:
        return 1
    #En cuanto llegue a 1 se detiene la función.
    else:
        return n * factorial (n-1) #La función se llama a si misma y se vuelve a aplicar hasta llegar a 1.

resultado_final = factorial (6)
#Aplicamos la función sobre el nº6 por ejemplo y printamos el resultado.
print (f"El resultado del factorial es {resultado_final}")



#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()


def tuplas_a_strings(lista_tuplas):
    """Convierte una lista de tuplas de dos elementos (nombre, edad) a una lista de textos.

    Args:
        lista_tuplas (list[tuple]): Lista de tuplas con formato (elemento1,
        elemento2).

    Returns:
        list[str]: Lista de cadenas formateadas separadas por espacio.
    """
    # Creamos la función
    resultado = map(lambda t: f"{t[0]} {t[1]}", lista_tuplas)

    #Cojo el f- string para acceder directamente a los valores en orden 0 y 1 (Nombre y edad) y le digo al resultado que lo saque en formato de lista
    return list(resultado)

datos = [("Ana", 25), ("Carlos", 30), ("Elena", 22)]


resultado_final = tuplas_a_strings(datos)

print(resultado_final)



#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir_numeros(num1, num2):
    """Muestra el resultado de dividir dos números o un mensaje de error si el divisor es cero.

    Args:
        num1 (int | float): El dividendo.
        num2 (int | float): El divisor.
    """
    # Validamos la división por 0.
    if num2 == 0:
        print(" Error: No se puede dividir entre cero.")
    else:
    #Si el número por el que se divide no es 0, se muestra el resultado.
        resultado = num1 / num2
        print(f" La división fue exitosa. El resultado es: {resultado}")


try:
    # Convertimos la entrada a float para verificar si es un número válido
    n1 = float(input("Introduce el primer número: "))
    n2 = float(input("Introduce el segundo número: "))
    
    # Llamamos a la función sólo si los datos son numéricos
    dividir_numeros(n1, n2)

except ValueError:
    #Creamos un except ValueError por si en vez de números se pone otro tipo caracter.
    print(" Error: Debes ingresar un valor numérico.")





#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


def mascotas_permitidas (lista_animales):
   """Filtra una lista de animales eliminando aquellos clasificados como mascotas prohibidas.

    Args:
        lista_animales (list[str]): Lista de nombres de mascotas.

    Returns:
        list[str]: Lista con las mascotas permitidas en España.
    """
# Creamos una variable con los animales prohibidos
   animales_prohibidos = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
# Creamos una variable con el filter, donde le decimos que filtre los animales que no están en la lista.
   animales_filtados = filter(lambda x :x not in animales_prohibidos, lista_animales)

 # Convertimos el resultado de filter a una lista normal
   return list(animales_filtados)

mascotas = ["Oso", "Perro", "Gato", "Mapache"]

resultado = mascotas_permitidas (mascotas)
print (resultado)



#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


# Definimos la función que usa nuestra excepción
def calcular_promedio(lista):
    """Calcula el promedio de una lista de números.

    Args:
        lista (list[int | float]): Lista de números a promediar.

    Returns:
        float: El resultado del promedio numérico.

    Raises:
        ValueError: Si la lista pasada por parámetro está vacía.
    """
    if len(lista) == 0:
        # Lanzamos nuestro error propio
        raise ValueError("La lista está vacía, no se puede calcular el promedio.")
    
    return sum(lista) / len(lista)


#  Probamos el código, generando una lista de números.
lista_numeros = [1,2,3]

try:
    resultado = calcular_promedio(lista_numeros)
    print(f"El promedio es: {resultado}")
except ValueError as error_lista_vacia:
    print(f"Error personalizado: {error_lista_vacia}")


    
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, 
# menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

#Creamos la función con el if y or.
def calcular_edad (num):
    """Valida si una edad numérica dada está dentro del rango válido de 0 a 120 años.

    Args:
        num (int): La edad a validar.

    Returns:
        int: La edad validada.

    Raises:
        ValueError: Si la edad es menor a 0 o mayor a 120.
    """
    if num <0 or num >120:
        raise ValueError ("Valor fuera del rango esperado, rango entre 0 y 120") 
    
    return num


    #Probamos el código.
try:
    entrada = input ("Introduce tu edad: ")
    edad = int (entrada)
    resultado = calcular_edad(edad)
    print ((f"Tu edad es de {edad} años"))
except ValueError as error_edad :
    print (f"Error: {error_edad}")



#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras (frase):
    """Obtiene la longitud en caracteres de cada palabra en una frase dada.

    Args:
        frase (str): Texto conteniendo palabras separadas por espacios.

    Returns:
        list[int]: Lista con los enteros indicando la longitud de cada palabra.
    """
    #Separamos cada palabra.
    palabras = frase.split()
    #Hacemos el map junto con el list para que nos de ya todo hecho.
    resultado_map = list (map(len,palabras))

    return resultado_map

mi_frase = "A veces Python se complica"

resultado = longitud_palabras (mi_frase)
print (resultado)


    
 

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def convertir (texto):
    """Toma una cadena y devuelve tuplas con la versión en mayúscula y minúscula de cada carácter único.

    Args:
        texto (str): Cadena de texto inicial.

    Returns:
        list[tuple[str, str]]: Lista de tuplas únicas en formato (MAYÚSCULA,
        minúscula).
    """

#Con el set eliminamos los duplicados
    caracteres_unicos = set (texto)
    print (caracteres_unicos)
#Dentro del map usamos el lambda para convertir tanto las mayusculas como minisculas en una tupla, por eso los ()
    resultado_map = list(map(lambda x: (x.upper(), x.lower()), caracteres_unicos))

    return resultado_map


palabra = "Helicoptero"

resultado = convertir (palabra)
print (resultado)

   


#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()


#Creamos la función con 2 parámetros, una la lista de palabras, y otra la letra por la que queramos que empiece.
def filtro_letra (lista, letra):
   """Filtra de una lista las palabras que empiezan por una letra específica.

    Args:
        lista (list[str]): Lista de palabras a evaluar.
        letra (str): Letra inicial por la cual se desea filtrar.

    Returns:
        list[str]: Lista con las palabras que inician con dicha letra.
    """
#Usamos el startswith para ver por que letra empieza la palabra
   palabras_filtradas = list(filter(lambda x: x.startswith(letra), lista))

   return palabras_filtradas

lista_palabras = ["casa", "coche", "erizo", "pc","erupcion"]

resultado = filtro_letra (lista_palabras,"c")
print (resultado)



#15. Crea una función lambda que sume 3 a cada número de una lista dada.

#Al ser solo un lambda no hay que crear una def como tal, se aplica directamente a una lista con el map.
lista_numeros = [ 2, 4 , 6]


resultado = list (map (lambda x : x + 3, lista_numeros))


print (resultado)



#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def longitud_palabras (texto,longitud):
    """Filtra palabras de un texto que superan una cantidad determinada de caracteres.

    Args:
        texto (str): Texto de origen.
        longitud (int): Cantidad límite de caracteres.

    Returns:
        list[str]: Lista de palabras cuyo número de letras es mayor a la
        longitud indicada.
    """
#Separamos el texto en una lista de palabras.
    palabras = texto.split()
# Filtramos comprobando si el len es mayor que la longitud indicada mas abajo.
    resultado_filter = list (filter (lambda x : len (x) > longitud, palabras))

    return resultado_filter

frase = "Me gusta comer pizza"

resultado = longitud_palabras (frase,3)

print (resultado)




#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()


def convertir_numeros (lista):
    """Transforma una lista de dígitos individuales en el número entero compuesto equivalente.

    Args:
        lista (list[int]): Lista de dígitos numéricos entre 0 y 9.

    Returns:
        int: El número entero completo resultante.
    """
#Usamos el reduce para sacar un único valor. Cogemos el primer valor y lo acumulamos, cogemos el siguiente, lo multiplicamos por 10 y se lo sumamos y asi con todos
    resultado_reduce= reduce (lambda acc, n : acc * 10 + n, lista)

    return resultado_reduce

lista_numeros = [1,2,3,5,6]

resultado = convertir_numeros(lista_numeros)

print (resultado)




# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()



def calcular_calificacion (lista):
    """Filtra un listado de estudiantes seleccionando a aquellos con calificación mayor o igual a 90.

    Args:
        lista (list[dict]): Lista de diccionarios con datos de los estudiantes.

    Returns:
        list[dict]: Lista con los diccionarios de estudiantes aprobados con
        sobresaliente.
    """
#Dentro del lambda le decimos que uicamente filtre por los que tienen la calificación mayor o igual a 90
    resultado_filter = list( filter (lambda x : x["calificacion"] >= 90, lista))
    return resultado_filter



# Creamos una varible con nuestro diccionario
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 85},
    {"nombre": "Beatriz", "edad": 21, "calificacion": 92},
]

resultado =  calcular_calificacion (estudiantes)

print (f"Estas personas son las que tienen una nota superior o igual a 90: {resultado}")




# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = [1,2,3,4,5]

resultado = list(filter (lambda x: x % 2 != 0,lista_numeros))

print (f"Los numeros impares son {resultado}")




#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista= ["hola", 5, 60, "perro"]
#Usamos el type para decirle el tipo de dato que queremos
resultado_filter = list (filter (lambda x: type (x)== int,lista))

print (f"Los elementos int son {resultado_filter}")



# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo (n):
    """Calcula el cubo de un número entero o decimal utilizando una función lambda interna.

    Args:
        n (int | float): Número a elevar a la tercera potencia.

    Returns:
        int | float: El valor elevado al cubo.
    """

    cubo = lambda x: x**3
    return cubo (n)

numero_a_calcular = 8

resultado =  calcular_cubo(numero_a_calcular)
print (f"El valor al cubo de {numero_a_calcular} es = {resultado}")



#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

#Usamos el acc para acumular los resultados de la lista. 
def calcular_producto_total(lista):
    """Calcula el producto resultante de multiplicar todos los valores numéricos de una lista.

    Args:
        lista (list[int | float]): Lista de números.

    Returns:
        int | float: El resultado final de la multiplicación acumulada.
    """

    producto = reduce (lambda acc , x : acc * x, lista)
    return producto

lista_numeros = [10,5,2]

resultado = calcular_producto_total (lista_numeros)

print (f"El producto total de la lista es = {resultado}")



#23. Concatena una lista de palabras.Usa la función reduce() .

#Igual que el ejercicio anterior pero al ser srt, se pone " " para que deje un espacio entre cada palabra.
def concatenar_palabras (lista):
    """Une una lista de palabras en una sola cadena de texto separada por espacios.

    Args:
        lista (list[str]): Lista con cadenas de texto.

    Returns:
        str: Cadena única con las palabras concatenadas.
    """

    concatenado = reduce (lambda acc, x : acc+ " " + x, lista)
    return concatenado

lista_palabras = ["hola", "amigo", "que", "tal"]

resultado = concatenar_palabras (lista_palabras)
print (f"La palabra concatenada es: {resultado}")




#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

# Es lo mismo que el ejercicio 22 pero cambiando la multiplicación por una resta.
def calcular_diferencia_total(lista):
    """Resta secuencialmente todos los elementos de una lista comenzando por el primero.

    Args:
        lista (list[int | float]): Lista de números a restar.

    Returns:
        int | float: El resultado final tras restar cada elemento del acumulado.
    """

    diferencia = reduce (lambda acc , x : acc - x, lista)
    return diferencia

lista_numeros = [10,5,2]

resultado = calcular_diferencia_total (lista_numeros)

print (f"La diferencia total de la lista es = {resultado}")




#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar_caracteres(cadena):
    """Obtiene la cantidad total de caracteres en una cadena de texto.

    Args:
        cadena (str): Texto a medir.

    Returns:
        int: Número total de caracteres.
    """
    #Únicamente cuenta las letras del texto
    return len(cadena)


texto = "Hola mundo"
resultado = contar_caracteres (texto)

print (f"El número total de letras en la lista es = {resultado}")




#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

#Estaba probando con este operador / pero eso me hacía la división tal cual, no sabía que % te daba el resto...
resto =  lambda a, b : a % b


resultado = resto (10,3)


print (f"El resto de ambos números es = {resultado}")





#27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio (lista):
    """Calcula el promedio aritmético de una lista numérica redondeado a dos decimales.

    Args:
        lista (list[int | float]): Lista de valores a promediar.

    Returns:
        float: Promedio numérico redondeado.
    """
#Muy parecido al ejercicio 10, pero sin la excepción. Uso el round para que no saque tantos decimales en caso que haya.
    promedio = round(sum (lista) / len(lista),2)

    return promedio

lista_numeros = [4,2, 5]

resultado =  calcular_promedio (lista_numeros)

print (f"El promedio de la lista es de: {resultado}")





#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


def buscar_duplicado (lista):
    """Identifica y devuelve el primer elemento repetido que aparece al recorrer una lista.

    Args:
        lista (list): Lista de elementos a analizar.

    Returns:
        Any: El primer elemento que se encuentra repetido, o None si no hay
        duplicados.
    """
    duplicados = []
#Recorremos la lista con un bucle y vamos añadiendolas en la lista, en el momento que haya una repetida, salta.
    for p in lista:
        if p in duplicados:
            return p
        else:
             duplicados.append(p)


lista_random = ["Hola", "pan", "pan", "coche", "coche"]

resultado = buscar_duplicado (lista_random)

print (f"La primera palabra repetida en la lista es: {resultado}")

  


#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def convertir_palabra(texto):
    """Oculta todos los caracteres de un texto con '#' exceptuando los últimos cuatro.

    Args:
        texto (str | int): Entrada de texto o número a enmascarar.

    Returns:
        str: Cadena enmascarada con los 4 últimos caracteres visibles.
    """

    visible = str(texto)[-4:] 
    oculto = "#" * len(str(texto)[:-4])

    return  oculto + visible
     


cadena_texto = 630485778

resultado =  convertir_palabra (cadena_texto)

print (resultado)





#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def buscar_anagrama (p1, p2):
    """Comprueba si dos palabras contienen exactamente las mismas letras en distinto orden.

    Args:
        p1 (str): Primera palabra.
        p2 (str): Segunda palabra.

    Returns:
        str: Mensaje afirmando o desmintiendo si las palabras son anagramas.
    """
#Ordenamos la palabra alfabéticamente y si son iguales salta un mensaje y si no, no.
    if sorted(p1) == sorted (p2):

     return ("Estas palabras son anagramas")

    else:
       return ("Estas palabras NO son anagramas")

palabra1 = "perro"
palabra2 = "roma"

resultado = buscar_anagrama(palabra1, palabra2)
print (resultado)





#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#  lanza una excepción.



def encontrar_repetidos ():

    lista_nombres = input("Introduzca lista de nombres: ").split()
    nombre_a_buscar = input ("Nombre a buscar: ")

    if nombre_a_buscar in lista_nombres:
        print (f"{nombre_a_buscar} está en la lista")
    else:
        raise Exception ("no está en la lista")

try:
    encontrar_repetidos()
except Exception as error:
    
    print (f"No se puede encontrar este nombre: {error}")


    


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.


def buscar_nombre_empleado(nombre, lista):
    """Busca a un empleado en el registro de la empresa y devuelve su puesto de trabajo.

    Args:
        nombre (str): Nombre completo del empleado.
        lista (dict[str, str]): Diccionario con los nombres como claves y sus
        puestos como valores.

    Returns:
        str: Puesto del empleado o un mensaje notificando que no trabaja en la
        empresa.
    """

    if nombre in lista:
        return (f" El trabajador {nombre} tiene el puesto de {lista[nombre]}")

    else:
        return (f"{nombre} no trabaja aquí.")

#Creamos un diccionario para asociar el puesto a un nombre, por lo que dentro del if le pedimos que dentro de la lista busque ese nombre y nos saque lo que tiene asociado.
lista_nombres = {"Luis Perez" : "Programador" ,
                 "Ruben Fernandez" : "Diseñador Grafico",
                 "Maria Pina" : "Directora"
                 }


resultado = buscar_nombre_empleado("Luis Perez", lista_nombres)

print (resultado)




# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas

def  sumas_listas (lista1,lista2):
    """Suma los elementos de dos listas posición a posición usando una función lambda y map.

    Args:
        lista1 (list[int | float]): Primera lista de números.
        lista2 (list[int | float]): Segunda lista de números.

    Returns:
        list[int | float]: Lista con el resultado de sumar los pares de valores.
    """

    resultado_lista= list (map (lambda x , y: x + y, lista1, lista2))
   

    return resultado_lista

lista_suma1 = [1, 2, 3]
lista_suma2 = [3, 2, 1]

resultado = sumas_listas (lista_suma1, lista_suma2)


print (f"La suma total de ambas lista es de: {sum(resultado)}")




#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.


class Arbol:
    #Creamos la clase

#Creamos los metodos
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    def __init__(self):
        """Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas."""
        self.tronco = 1
        self.ramas = []

#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.   

    def crecer_tronco(self):
        """Incrementa en 1 unidad la longitud del tronco."""

        self.tronco +=1

#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.

    def nueva_rama (self):
        """Agrega una nueva rama de longitud 1 al árbol."""

        self.ramas.append(1)

#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.

    def crecer_ramas (self):
        """Aumenta en 1 unidad la longitud de cada una de las ramas existentes."""

        for l in range(len(self.ramas)):
            self.ramas[l] +=1

#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.

    def quitar_rama (self,posicion):
        """Elimina una rama en un índice o posición específica.

        Args:
            posicion (int): Índice de la rama a eliminar dentro de la lista.
        """

        self.ramas.pop(posicion)

#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

    def info_arbol (self):
        """Imprime la información actualizada del tronco, número de ramas y la medida de cada una."""

        print (f"Longitud del tronco: {self.tronco} metros, Longitud de ramas: {self.ramas} metros, Total ramas: {len(self.ramas)}")


#Caso de uso:
#1. Crear un árbol.

pino = Arbol ()

#2. Hacer crecer el tronco del árbol una unidad.

pino.crecer_tronco()

#3. Añadir una nueva rama al árbol.

pino.nueva_rama()
#4. Hacer crecer todas las ramas del árbol una unidad.

pino.crecer_ramas()
pino.crecer_ramas()

#5. Añadir dos nuevas ramas al árbol.

pino.nueva_rama()
pino.nueva_rama()

#6. Retirar la rama situada en la posición 2.

pino.quitar_rama(2)

#7. Obtener información sobre el árbol.

pino.info_arbol()




#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
# agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

class UsuarioBanco:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    def __init__(self, nombre, saldo, cuenta):
        """Representa a un cliente de banco con saldo y cuenta corriente activa."""

        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta

#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    def retirar_dinero (self,cantidad):
        """Resta una suma de dinero del saldo del usuario si dispone de fondos y cuenta activa.

        Args:
            cantidad (int | float): Importe a retirar.

        Raises:
            ValueError: Si la cuenta no está activa o no hay suficiente saldo.
        """

        if self.cuenta == False:
            raise ValueError (f"{self.nombre} no tiene cuenta activa")

    
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print (f"Aún quedan {self.saldo} euros en la cuenta")

        else:
            raise ValueError (f"No puede retirarse {cantidad} euros, cantidad actual: {self.saldo}")

#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.

    def transferir_dinero (self,usuario, cantidad):
        """Transfiere dinero desde la cuenta de otro usuario a la cuenta actual.

        Args:
            usuario (UsuarioBanco): El objeto UsuarioBanco desde el cual se
            extraen los fondos.
            cantidad (int | float): Importe a transferir.
        """

        usuario.retirar_dinero(cantidad)
        self.agregar_dinero (cantidad)


         

         
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
    def agregar_dinero (self,cantidad):
        """Suma una cantidad de dinero al saldo actual de la cuenta activa.

        Args:
            cantidad (int | float): Importe a ingresar.

        Raises:
            ValueError: Si la cuenta corriente no está activa.
        """

        if self.cuenta == False:
            raise ValueError (f"{self.nombre} no tiene cuenta activa")

        self.saldo += cantidad
        
        print (f"Se han añadido {cantidad} en la cuenta. Hay un total de : {self.saldo} euros en su cuenta")

#Caso de uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. PROYECTO LÓGICA: Katas de Python 3

Alicia = UsuarioBanco ("Alicia", 100, True)
Bob = UsuarioBanco ("Bob", 50, True)


#2. Agregar 20 unidades de saldo de "Bob".

Bob.agregar_dinero (20) 

#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

Alicia.transferir_dinero(Bob,80)

#4. Retirar 50 unidades de saldo a "Alicia".

Alicia.retirar_dinero (50)






#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#Código a seguir:
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.

def contar_palabra(texto):
    """Cuenta las apariciones de cada palabra en una cadena de texto.

    Args:
        texto (str): Cadena de texto a analizar.

    Returns:
        dict[str, int]: Diccionario indicando cuántas veces aparece cada
        palabra.
    """
#Creamos la funcion, primero convertimos todo a minúsuclas por si hubiera caractéres en mayúsuclas, y separamos cada palabra con un split.
    palabras = texto.lower().split()
#Creamos un diccionario vacío que nos servirá de acumulador
    resultado_conteo = {}

    for p in palabras:
#Si al hacer el bucel la palabra está dentro del diccionario, se pone esa palabra con +1
        if p in resultado_conteo:
            resultado_conteo[p] += 1
#Si no está la palabra, se pone 1
        else:
            resultado_conteo[p] = 1

    return resultado_conteo


#2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Sustituye todas las repeticiones de una palabra en un texto por otra nueva.

    Args:
        texto (str): Texto de origen.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Palabra sustituta.

    Returns:
        str: El texto modificado tras el reemplazo.
    """
#Creamos la función y añadimos el replace.
    return texto.replace(palabra_original, palabra_nueva)

#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.

def eliminar_palabra(texto, palabra_eliminada):
    """Elimina las repeticiones de una palabra concreta dentro de un texto.

    Args:
        texto (str): Texto de origen.
        palabra_eliminada (str): Palabra que se desea borrar.

    Returns:
        str: El texto con la palabra removida.
    """
#Creamos la función igual que antes, pero esta vez con un carácter vacío como ""
    return texto.replace(palabra_eliminada,"")

#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

def procesar_texto(texto, opcion,*args):
    """Procesa un texto según la opción seleccionada ("contar", "reemplazar" o "eliminar").

    Args:
        texto (str): El texto a procesar.
        opcion (str): Acción a ejecutar ("contar", "reemplazar", "eliminar").
        *args: Argumentos variables requeridos según la opción seleccionada.

    Returns:
        dict | str: Un diccionario con los conteos o el texto modificado.

    Raises:
        ValueError: Si se indica una opción diferente a las tres permitidas.
    """
#Creamos la función y usamos los args para tener mayor flexibilidad a la hora de usar cada opción
    if opcion == "contar":
     return contar_palabra(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args [1])

    elif opcion =="eliminar":
        return eliminar_palabra(texto, args[0])
#Si se pone una opción que no esté en la función, forzamos este fallo
    else:
        raise ValueError (f"Opción {opcion} no válida")

#Caso de uso:
#Comprueba el funcionamiento completo de la función procesar_texto

texto_ejemplo = "el perro corre rapido por el parque el perro"

print (procesar_texto(texto_ejemplo, "eliminar", "el perro"))





#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
 

def momento_dia(hora):
    """Evalúa una hora en formato HH:MM e indica el tramo del día correspondiente.

    Args:
        hora (str): Texto con la hora introducida por el usuario (ej: "14:30").

    Returns:
        str: Cadena indicando si es por la mañana, por la tarde o por la noche.
    """
#Importamos arriba del todo de la librería datetime y convertimos el texto recibido a un objeto de tipo hora
    hora = datetime.strptime(hora, "%H:%M").time()
#Asociamos un rango horario  y las horas límite
    mañana = datetime.strptime("06:00","%H:%M").time()
    tarde = datetime.strptime("12:00","%H:%M").time()
    noche = datetime.strptime("20:00","%H:%M").time()

    if mañana <= hora <tarde:
        tiempo = "la mañana"

    elif tarde <=hora < noche:
        tiempo = "la tarde"

    else:
        tiempo = "la noche"

    #.strftime("%H:%M") eliminamos los segundos y nos quedamos solo con hora y minuto. Si no lo ponía me sacaba tambien los segundos y siempre daban 00
    hora_limpia = hora.strftime("%H:%M")
    return f"La hora es: {hora_limpia} y es por {tiempo}"


hora_usuario = input("Introduce la hora (formato HH:MM, ej: 14:30): ")


resultado = momento_dia(hora_usuario)
print(resultado)




#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

def calcular_calificacion (nota):
    """_Determina la calificación en texto de un alumno según su nota numérica.

    Args:
        nota (int | float): La nota numérica del alumno entre 0 y 100.

    Returns:
        str: La calificación correspondiente ("insuficiente", "bien", "muy bien", "excelente").
 
    """
    if nota < 0 or nota > 100:
        return "Nota no válida. Debe estar entre 0 y 100."

    if nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"

nota_alumno = float(input("Introduce la nota numérica del alumno (0-100): "))
resultado = calcular_calificacion(nota_alumno)
print(f"La calificación es: {resultado}")




#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area (figura,datos):
    """Calcula el área de una figura geométrica (rectángulo, círculo o triángulo).

    Args:
        figura (str): El nombre de la figura ("rectangulo", "circulo" o "triangulo").
        datos (tuple): Tupla con las medidas necesarias:
                       - Para "rectangulo": (base, altura)
                       - Para "circulo": (radio,)
                       - Para "triangulo": (base, altura)

    Returns:
        float | str: El área calculada de la figura o un mensaje de error si la figura no es válida.
    """

    if figura == "rectangulo":
        area_rectangulo = datos[0] * datos[1]
        return area_rectangulo
    

    elif figura == "circulo":
        area_circulo = 3.14* (datos[0]**2)
        return area_circulo

    elif figura == "triangulo":
        area_triangulo = (datos[0] * datos[1]) /2
        return area_triangulo

    else:
        return ("Figura no válida")

    
print (calcular_area("circulo",(5,)))



# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en
#  línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones.


precio_original = float(input("Introduzca importe del artículo: "))


respuesta_cupon = input("¿Tiene código de descuento? (si/no): ").strip().lower()


if respuesta_cupon in ["si", "sí"]:
    cupon = float(input("Introduzca valor del descuento (€): "))

    if cupon > 0:
     precio_final = max(0.0, precio_original - cupon)
     print (f"Descuento de {cupon}€ aplicado. Precio final: {precio_final}€")

    else:
       print (f"El valor del cupón no es válido. Precio final: {precio_original}€")

else:
    print(f"No se puede aplicar ningún descuento a este artículo. Precio final: {precio_original}€")

