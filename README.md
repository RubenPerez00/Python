# Python
# 🚀 Proyecto Python: Resolución de Katas y Fundamentos de Programación

Este repositorio reúne la resolución paso a paso, la metodología y la estructura de código utilizadas para resolver una colección de ejercicios prácticos (Katas) en Python. El objetivo principal ha sido poner en práctica la lógica de programación y dominar los conceptos clave del lenguaje.

---

## 📊 Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Librerías estándar:** `functools` (`reduce`), `datetime`
* **Entorno de trabajo:** Visual Studio Code

---

## 📋 SOBRE EL PROYECTO Y LOS EJERCICIOS

El proyecto está planteado como un recorrido práctico por los pilares fundamentales de Python. A través de diferentes retos, se abordan problemas habituales organizados en tres bloques principales: **procesamiento funcional**, **tratamiento de datos y excepciones**, y **diseño orientado a objetos**.

---

### 📈 1. Programación Funcional y Manejo de Datos

* **Transformación con `map()`:** Procesamiento directo de listas y estructuras para duplicar valores, calcular longitudes de cadenas o formatear tuplas sin necesidad de recurrir a bucles `for` tradicionales.
* **Filtrado con `filter()` y `lambda`:** Selección de datos basada en condiciones específicas, como filtrar especies de mascotas, extraer palabras por su número de letras o seleccionar estudiantes con notas destacadas (`≥ 90`).
* **Acumulación con `reduce()`:** Uso de funciones acumulativas para construir números enteros desde listas de dígitos, calcular productos consecutivos, restar secuencias de valores y combinar textos.
* **Lógica matemática:** Aplicación de funciones recursivas para calcular factoriales y operaciones estadísticas simples para obtener promedios ponderados y redondear resultados.

---

### 🛠️ 2. Control de Errores y Tratamiento de Textos

Para conseguir un código limpio y capaz de gestionar imprevistos, se aplicaron las siguientes soluciones:

* **Gestión de excepciones (`try-except`, `raise`):** Control de errores comunes como divisiones por cero, conversión de tipos con `ValueError` y validación de rangos (por ejemplo, comprobar que una edad esté entre 0 y 120 años).
* **Manipulación de cadenas:** Funciones para contar frecuencia de caracteres (omitendo espacios), detectar si dos palabras son anagramas y enmascarar datos personales dejando visibles solo los últimos 4 dígitos.
* **Uso de `datetime`:** Análisis e interpretación de horas ingresadas por el usuario en formato `HH:MM` para determinar automáticamente la franja horaria (mañana, tarde o noche).

---

### 🏗️ 3. Programación Orientada a Objetos (POO)

Se han diseñado clases personalizadas para representar entidades con su propio estado y reglas de negocio:

* **Clase `Arbol`:** Representa un árbol dinámico que vincula la altura del tronco con una lista de ramas, ofreciendo métodos para hacer crecer el tronco, añadir ramas o podarlas según se necesite.
* **Clase `UsuarioBanco`:** Simula una cuenta bancaria con validación de saldo y estado activo antes de realizar operaciones como ingresos, retiradas o transferencias de dinero entre usuarios.

---

## 🗺️ Organización de los Ejercicios

Los ejercicios del script principal están agrupados según el concepto de programación que trabajan:

1. **Transformación de datos (`map`, `lambda`):** Ejercicios 2, 4, 7, 12, 13, 15, 33
2. **Filtrado de información (`filter`):** Ejercicios 3, 9, 14, 16, 18, 19, 20
3. **Agregación de datos (`reduce`):** Ejercicios 17, 22, 23, 24
4. **Validaciones y excepciones (`try-except`):** Ejercicios 8, 10, 11, 31
5. **Lógica general, fechas y cadenas:** Ejercicios 1, 5, 6, 25, 26, 27, 28, 29, 30, 32, 37, 38, 39, 40, 41
6. **Clases y Objetos (POO):** Ejercicios 34 (`Arbol`) y 36 (`UsuarioBanco`)

---

