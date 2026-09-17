# 🐍 Python: Katas y Fundamentos

¡Hola! 👋 Este repositorio es el espacio donde voy guardando los ejercicios, katas y retos de código que voy resolviendo para dominar las bases de Python y mejorar mi lógica de programación día a día.

La idea no es solo que el código funcione, sino aprender a escribir un Python más limpio, eficiente y legible en el proceso.

---

## 📊 Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Herramientas de la librería estándar:** `functools` (`reduce`), `datetime`, `collections`
* **Editor:** Visual Studio Code

---

## 📋 SOBRE EL PROYECTO Y LOS EJERCICIOS

He ido organizando los retos por bloques conceptuales según los temas que he ido trabajando:

### 🧠 1. Programación Funcional y Manipulación de Datos

Aquí el objetivo fue dejar a un lado los bucles `for` tradicionales cuando no hacían falta y apoyarme en herramientas más *pythonicas*:

* **`map()`**: Transformación rápida de listas (calcular longitudes de texto, duplicar números, formatear tuplas).
* **`filter()` + `lambda`**: Filtrado de colecciones según reglas específicas (extraer ciertas palabras, filtrar notas superiores a 90, clasificar elementos).
* **`reduce()`**: Acumulación de datos para construir números a partir de listas de dígitos, productos acumulados o combinación de textos.
* **Lógica y matemáticas**: Uso de recursividad (como el cálculo de factoriales) y operaciones estadísticas como promedios ponderados.

---

### 🛡️ 2. Control de Errores y Manejo de Textos

Escribir código que no rompa a la primera oportunidad:

* **Excepciones con `try-except` y `raise`**: Manejo de fallos típicos como divisiones entre cero, validación de tipos (`ValueError`) o comprobación de rangos (por ejemplo, validar que una edad sea real).
* **Cadenas de texto**: Contar frecuencia de caracteres, detectar anagramas o enmascarar datos sensibles (mostrar solo los últimos 4 dígitos).
* **Fechas y horas con `datetime`**: Parseo de horas en formato `HH:MM` para clasificar franjas horarias (mañana, tarde, noche).

---

### 🏗️ 3. Programación Orientada a Objetos (POO)

Modelado de problemas usando clases, atributos y métodos con reglas de negocio claras:

* **Clase `Arbol`**: Un modelo dinámico donde la altura del tronco está ligada a sus ramas, permitiendo hacer crecer la planta, añadir ramas o podarla.
* **Clase `UsuarioBanco`**: Simulación de una cuenta bancaria con controles de saldo y estado activo para permitir ingresos, retiros y transferencias entre usuarios.

---

💡 *Este repositorio se va actualizando a medida que voy resolviendo nuevos ejercicios.*
