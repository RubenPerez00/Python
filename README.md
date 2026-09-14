# Python
# 🚀 Proyecto Python: Resolución de Katas y Fundamentos de Programación

Este README contiene el desarrollo completo, la metodología, la arquitectura de código y los ejercicios resueltos pertenecientes a la colección de Katas de lógica de programación en Python[cite: 6].

---

## 📊 Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+[cite: 6]
* **Módulos Estándar:** `functools` (`reduce`), `datetime`[cite: 6]
* **Entorno de Desarrollo:** Visual Studio Code

---

## 📋 INFORME EXPLICATIVO DEL PROYECTO

El conjunto de ejercicios está diseñado como un catálogo exhaustivo de prácticas en Python, simulando la resolución de problemas reales divididos en tres pilares fundamentales: la **manipulación de colecciones**, el **procesamiento funcional de datos** y el **diseño orientado a objetos (POO)**[cite: 6].

---

### 📈 1. Paradigma Funcional y Procesamiento de Datos

* **Iteración Eficiente con `map()`:** Transformación masiva de datos sin necesidad de bucles explícitos, aplicando operaciones de duplicado de valores, cálculo de longitudes de palabras y conversiones de listas de tuplas a cadenas formateadas[cite: 6].
* **Filtrado Avanzado con `filter()` e Expresiones `Lambda`:** Selección de subconjuntos de datos según criterios dinámicos (como el filtrado de mascotas prohibidas en España, la extracción de palabras por longitud o la selección de estudiantes con calificaciones sobresalientes `≥ 90`)[cite: 6].
* **Reducción de Colecciones con `reduce()`:** Aplicación de funciones acumulativas para construir números enteros a partir de listas de dígitos, calcular productos totales, restar valores en secuencia y concatenar cadenas de texto[cite: 6].
* **Matemáticas de Fondo:** Cálculo de factoriales mediante funciones recursivas y operaciones estadísticas para evaluar promedios ponderados con redondeo de decimales[cite: 6].

---

### 🛠️ 2. Arquitectura de Código y Control de Excepciones

Para garantizar la robustez, modularidad y mantenibilidad de la aplicación, se implementaron las siguientes soluciones técnicas:

* **Manejo Riguroso de Excepciones (`try-except`, `raise`):** Validación contra la división por cero, captura de datos no numéricos (`ValueError`) e implementación de validaciones de límites en entradas de usuario (como rangos de edad permitidos de 0 a 120 años)[cite: 6].
* **Tratamiento de Cadenas de Texto:** Funciones avanzadas para el conteo e identificación de frecuencias de letras (descartando espacios), verificación de palabras anagramas y enmascaramiento de datos sensibles (ocultando caracteres excepto los últimos 4 dígitos)[cite: 6].
* **Procesamiento Horario con `datetime`:** Validación e interpretación de horas introducidas por el usuario en formato `HH:MM` para clasificarlas automáticamente en franjas de mañana, tarde o noche[cite: 6].

---

### 🏗️ 3. Diseños de Clases en POO (Programación Orientada a Objetos)

El proyecto modela entidades relacionales complejas mediante clases personalizadas que gestionan su propio estado interno[cite: 6]:

* **Clase `Arbol`:** Modelo de estructura mutable que controla la relación entre la longitud del tronco y una colección dinámica de ramas, proporcionando métodos para añadir, hacer crecer o podar elementos específicos[cite: 6].
* **Clase `UsuarioBanco`:** Simulación de un sistema de cuenta bancaria que implementa encapsulamiento para validar saldos y estados de cuenta activas antes de permitir operaciones de ingreso, retiro o transferencia directa entre usuarios[cite: 6].

---

## 🗺️ Esquema de la Estructura de Ejercicios

El script principal organiza la lógica en los siguientes bloques de aprendizaje[cite: 6]:

1. **Transformación e Iteración:** Ejercicios 2, 4, 7, 12, 13, 15, 33 (Operaciones avanzadas con `map` y `lambda`)[cite: 6].
2. **Filtrado y Selección:** Ejercicios 3, 9, 14, 16, 18, 19, 20 (Filtros de listas, tuplas y diccionarios con `filter`)[cite: 6].
3. **Agregación y Reducción:** Ejercicios 17, 22, 23, 24 (Acumulaciones complejas con `reduce`)[cite: 6].
4. **Validación y Excepciones:** Ejercicios 8, 10, 11, 31 (Control de errores y validación de tipos)[cite: 6].
5. **Algoritmos y Lógica General:** Ejercicios 1, 5, 6, 25, 26, 27, 28, 29, 30, 32, 37, 38, 39, 40, 41 (Lógica condicional, recursividad, fechas y enmascarado)[cite: 6].
6. **Programación Orientada a Objetos:** Ejercicios 34 y 36 (Diseño de las clases `Arbol` y `UsuarioBanco`)[cite: 6].

---
