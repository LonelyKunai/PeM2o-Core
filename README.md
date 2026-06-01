---
<a name="English"></a>
# PokéM2O Core
## A simple way to automate mechanics of PokéMMO (MuHelper console style)

[English](#english) | [Español](#español)

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Functions](#functions)
- [Examples](#examples)
- [Requirements](#requirements)
- [License](#license)

---
<a name="Overview"></a>
## 🎯 Overview

**PokéM2O Core** is a lightweight, well-documented Python module that provides 17 reusable functions for common automation tasks. Perfect for building bots, automation scripts, and game control applications.

### Key Benefits

✅ **Simple & Clean** - Easy-to-understand function names  
✅ **Well Documented** - Every function has docstrings and examples  
✅ **Error Handling** - Built-in exception management  
✅ **Flexible** - Works with both string and Key objects  
✅ **Modular** - Import only what you need  

---
<a name="Features"></a>
## 🌟 Features

### Keyboard Control
- Press individual keys
- Repeat keys multiple times
- Execute key sequences
- Random directional input

### File Management
- Load and save configuration files
- List files in directories
- Check file existence
- Multiple encoding support

### Window Management (Windows)
- Find windows by title
- Focus windows
- Get window dimensions

### Utilities
- Random number generation (int & float)
- Time delays (fixed & random)
- Logger configuration
- Key validation

---
<a name="Installation"></a>
## 📥 Installation

### 1. Download the module
Copy `utils.py` to your project directory

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

For Windows window management:
```bash
pip install pywin32
```

### 3. Basic usage
```python
from utils import press_key, wait, random_int

# Your code here
```

---
<a name="quick-start"></a>
## 🚀 Quick Start

### Example 1: Press a Key
```python
from utils import press_key

# Press 'z' for 0.5 seconds
press_key('z', 0.5)
```

### Example 2: Repeat a Key
```python
from utils import repeat_key

# Press 'z' 5 times with 0.2s duration and 0.1s interval
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

### Example 3: Wait with Randomization
```python
from utils import wait_random

# Wait 1-5 seconds randomly
wait_random(1, 5)
```

### Example 4: Load Configuration
```python
from utils import load_config_file

config = load_config_file('config.txt')
if config:
    print(f"Loaded {len(config)} lines")
```

---
<a name="Functions"></a>
## 📚 Functions Reference

### Keyboard Functions

#### `press_key(key, duration=0.1)`
Press a key for a specified duration.

**Parameters:**
- `key` (str or Key): Key to press
- `duration` (float): How long to press (seconds)

**Returns:** bool

**Example:**
```python
press_key('z', 0.5)
press_key(Key.up, 0.2)
```

---

#### `repeat_key(key, times=1, press_duration=0.1, interval=0.05, final_wait=0.0)`
Repeat key presses multiple times.

**Parameters:**
- `key`: Key to press repeatedly
- `times`: Number of presses
- `press_duration`: How long each press lasts
- `interval`: Delay between presses
- `final_wait`: Delay after all presses

**Returns:** bool

**Example:**
```python
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

---

#### `press_key_sequence(keys, press_duration=0.1, interval=0.05)`
Execute a sequence of key presses.

**Parameters:**
- `keys`: List, tuple, or string of keys
- `press_duration`: How long each key is pressed
- `interval`: Delay between keys

**Returns:** bool

**Example:**
```python
press_key_sequence(['z', 'x', 'z'], 0.2, 0.1)
```

---

#### `get_random_direction_key()`
Get a random directional key (up, down, left, right).

**Returns:** Key

**Example:**
```python
direction = get_random_direction_key()
press_key(direction, 0.3)
```

---

### Number Functions

#### `random_int(min_value, max_value)`
Generate a random integer.

**Example:**
```python
number = random_int(1, 10)
```

---

#### `random_float(min_value, max_value)`
Generate a random decimal number.

**Example:**
```python
value = random_float(0.5, 2.5)
```

---

### Time Functions

#### `wait(seconds)`
Wait for a specified number of seconds.

**Example:**
```python
wait(2.5)
```

---

#### `wait_random(min_seconds, max_seconds)`
Wait a random amount of time.

**Example:**
```python
wait_random(1, 5)  # Wait 1-5 seconds randomly
```

---

### File Functions

#### `load_config_file(filepath, encoding='utf-8')`
Load a text configuration file.

**Returns:** list of lines

**Example:**
```python
lines = load_config_file('config.txt')
```

---

#### `save_config_file(filepath, content, encoding='utf-8')`
Save content to a file.

**Returns:** bool

**Example:**
```python
save_config_file('output.txt', ['line1', 'line2'])
```

---

#### `file_exists(filepath)`
Check if a file exists.

**Returns:** bool

**Example:**
```python
if file_exists('config.txt'):
    data = load_config_file('config.txt')
```

---

#### `get_files_in_directory(directory, extensions=None)`
List files in a directory.

**Returns:** list of file paths

**Example:**
```python
# Get all Python files
py_files = get_files_in_directory('.', ['.py'])

# Get all files
all_files = get_files_in_directory('data/')
```

---

### Window Functions

#### `find_window_by_title(keywords)`
Find a window by title keywords.

**Returns:** tuple (hwnd, title) or (None, None)

**Example:**
```python
hwnd, title = find_window_by_title("PokeMMO")
```

---

#### `focus_window(hwnd)`
Focus a window and bring it to front.

**Returns:** bool

**Example:**
```python
hwnd, title = find_window_by_title("MyApp")
if hwnd:
    focus_window(hwnd)
```

---

#### `get_window_rect(hwnd)`
Get window position and dimensions.

**Returns:** tuple (x, y, width, height) or None

**Example:**
```python
x, y, w, h = get_window_rect(hwnd)
```

---

### Utility Functions

#### `setup_logger(name, level=logging.INFO, log_file=None)`
Configure a custom logger.

**Returns:** logging.Logger

**Example:**
```python
logger = setup_logger('MyBot', logging.DEBUG)
logger.info("Bot started")
```

---

#### `is_valid_key(key)`
Validate if a value is a valid key.

**Returns:** bool

**Example:**
```python
if is_valid_key('z'):
    press_key('z', 0.5)
```

---
<a name="Examples"></a>
## 💡 Complete Examples

See `examples.py` for comprehensive demonstrations of all functions.

### Running Examples
```bash
python examples.py
```

---
<a name="Requirements"></a>
## 📋 Requirements

- Python 3.8 or higher
- pynput (for keyboard control)
- pywin32 (for Windows window management - optional)

### Install Requirements
```bash
pip install -r requirements.txt
```

---

## 🛠️ Common Patterns

### Retry Pattern
```python
def retry_action(key, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}/{max_attempts}")
        press_key(key, 0.3)
        if attempt < max_attempts:
            wait_random(0.5, 1.5)

retry_action('z', max_attempts=3)
```

### Timed Loop
```python
import time

start = time.time()
duration = 60  # 60 seconds

while time.time() - start < duration:
    press_key('z', 0.3)
    wait_random(1, 2)
```

### Smart Sequence
```python
def smart_action(attack=True, move=False):
    if attack:
        repeat_key('z', times=3, press_duration=0.2)
    if move:
        press_key(get_random_direction_key(), 0.3)
    wait_random(1, 2)

smart_action(attack=True, move=True)
```

---
<a name="License"></a>
## 📝 License

MIT License - Feel free to use in your projects

---

## 🤝 Contributing

Have suggestions? Found a bug? Feel free to open an issue or contribute!

---

## 📞 Support

For more information:
- Check `examples.py` for practical demonstrations
- Review function docstrings in `utils.py`
- Read this README for API reference

---

<a name="español"></a>

# PokéM2O Core
## Una manera simple de automatizar mecanicas de PokéMMO (Estilo MuHelper)

[English](#english) | [Español](#español)

---

## 📖 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Inicio Rápido](#inicio-rápido)
- [Funciones](#funciones)
- [Ejemplos](#ejemplos)
- [Requisitos](#requisitos)
- [Licencia](#licencia)

---
<a name="Descripción"></a>
## 🎯 Descripción

**Utils** es un módulo Python ligero y bien documentado que proporciona 17 funciones reutilizables para tareas comunes de automatización. Perfecto para construir bots, scripts de automatización y aplicaciones de control de juegos.

### Ventajas Principales

✅ **Simple y Limpio** - Nombres de función fáciles de entender  
✅ **Bien Documentado** - Cada función tiene docstrings y ejemplos  
✅ **Manejo de Errores** - Gestión integrada de excepciones  
✅ **Flexible** - Funciona con strings y objetos Key  
✅ **Modular** - Importa solo lo que necesites  

---
<a name="Características"></a>
## 🌟 Características

### Control de Teclado
- Presionar teclas individuales
- Repetir teclas múltiples veces
- Ejecutar secuencias de teclas
- Entrada direccional aleatoria

### Gestión de Archivos
- Cargar y guardar archivos de configuración
- Listar archivos en directorios
- Verificar existencia de archivos
- Soporte para múltiples codificaciones

### Gestión de Ventanas (Windows)
- Encontrar ventanas por título
- Enfocar ventanas
- Obtener dimensiones de ventana

### Utilidades
- Generación de números aleatorios (int y float)
- Retrasos de tiempo (fijos y aleatorios)
- Configuración de logging
- Validación de teclas

---
<a name="Instalación"></a>
## 📥 Instalación

### 1. Descargar el módulo
Copia `utils.py` a tu directorio del proyecto

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

Para gestión de ventanas en Windows:
```bash
pip install pywin32
```

### 3. Uso básico
```python
from utils import press_key, wait, random_int

# Tu código aquí
```

---
<a name="Inicio-Rápido"></a>
## 🚀 Inicio Rápido

### Ejemplo 1: Presionar una Tecla
```python
from utils import press_key

# Presionar 'z' por 0.5 segundos
press_key('z', 0.5)
```

### Ejemplo 2: Repetir una Tecla
```python
from utils import repeat_key

# Presionar 'z' 5 veces con 0.2s de duración y 0.1s de intervalo
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

### Ejemplo 3: Esperar con Aleatorización
```python
from utils import wait_random

# Esperar 1-5 segundos aleatoriamente
wait_random(1, 5)
```

### Ejemplo 4: Cargar Configuración
```python
from utils import load_config_file

config = load_config_file('config.txt')
if config:
    print(f"Se cargaron {len(config)} líneas")
```

---

## 📚 Referencia de Funciones

### Funciones de Teclado

#### `press_key(key, duration=0.1)`
Presiona una tecla durante una duración específica.

**Parámetros:**
- `key` (str o Key): Tecla a presionar
- `duration` (float): Cuánto presionar (segundos)

**Retorna:** bool

**Ejemplo:**
```python
press_key('z', 0.5)
press_key(Key.up, 0.2)
```

---

#### `repeat_key(key, times=1, press_duration=0.1, interval=0.05, final_wait=0.0)`
Repite la presión de una tecla múltiples veces.

**Parámetros:**
- `key`: Tecla a presionar repetidamente
- `times`: Número de pulsaciones
- `press_duration`: Cuánto dura cada pulsación
- `interval`: Retraso entre pulsaciones
- `final_wait`: Retraso después de todas las pulsaciones

**Retorna:** bool

**Ejemplo:**
```python
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

---

#### `press_key_sequence(keys, press_duration=0.1, interval=0.05)`
Ejecuta una secuencia de pulsaciones de tecla.

**Parámetros:**
- `keys`: Lista, tupla o string de teclas
- `press_duration`: Cuánto se presiona cada tecla
- `interval`: Retraso entre teclas

**Retorna:** bool

**Ejemplo:**
```python
press_key_sequence(['z', 'x', 'z'], 0.2, 0.1)
```

---

#### `get_random_direction_key()`
Obtiene una tecla direccional aleatoria (arriba, abajo, izquierda, derecha).

**Retorna:** Key

**Ejemplo:**
```python
direction = get_random_direction_key()
press_key(direction, 0.3)
```

---

### Funciones de Números

#### `random_int(min_value, max_value)`
Genera un número entero aleatorio.

**Ejemplo:**
```python
number = random_int(1, 10)
```

---

#### `random_float(min_value, max_value)`
Genera un número decimal aleatorio.

**Ejemplo:**
```python
value = random_float(0.5, 2.5)
```

---

### Funciones de Tiempo

#### `wait(seconds)`
Espera un número específico de segundos.

**Ejemplo:**
```python
wait(2.5)
```

---

#### `wait_random(min_seconds, max_seconds)`
Espera un tiempo aleatorio.

**Ejemplo:**
```python
wait_random(1, 5)  # Espera 1-5 segundos aleatoriamente
```

---

### Funciones de Archivo

#### `load_config_file(filepath, encoding='utf-8')`
Carga un archivo de configuración de texto.

**Retorna:** lista de líneas

**Ejemplo:**
```python
lines = load_config_file('config.txt')
```

---

#### `save_config_file(filepath, content, encoding='utf-8')`
Guarda contenido en un archivo.

**Retorna:** bool

**Ejemplo:**
```python
save_config_file('output.txt', ['línea1', 'línea2'])
```

---

#### `file_exists(filepath)`
Verifica si un archivo existe.

**Retorna:** bool

**Ejemplo:**
```python
if file_exists('config.txt'):
    data = load_config_file('config.txt')
```

---

#### `get_files_in_directory(directory, extensions=None)`
Lista archivos en un directorio.

**Retorna:** lista de rutas de archivo

**Ejemplo:**
```python
# Obtener todos los archivos Python
py_files = get_files_in_directory('.', ['.py'])

# Obtener todos los archivos
all_files = get_files_in_directory('data/')
```

---

### Funciones de Ventana

#### `find_window_by_title(keywords)`
Encuentra una ventana por palabras clave en su título.

**Retorna:** tupla (hwnd, title) o (None, None)

**Ejemplo:**
```python
hwnd, title = find_window_by_title("PokeMMO")
```

---

#### `focus_window(hwnd)`
Enfoca una ventana y la trae al frente.

**Retorna:** bool

**Ejemplo:**
```python
hwnd, title = find_window_by_title("MiApp")
if hwnd:
    focus_window(hwnd)
```

---

#### `get_window_rect(hwnd)`
Obtiene la posición y dimensiones de una ventana.

**Retorna:** tupla (x, y, width, height) o None

**Ejemplo:**
```python
x, y, w, h = get_window_rect(hwnd)
```

---

### Funciones de Utilidad

#### `setup_logger(name, level=logging.INFO, log_file=None)`
Configura un logger personalizado.

**Retorna:** logging.Logger

**Ejemplo:**
```python
logger = setup_logger('MiBot', logging.DEBUG)
logger.info("Bot iniciado")
```

---

#### `is_valid_key(key)`
Valida si un valor es una tecla válida.

**Retorna:** bool

**Ejemplo:**
```python
if is_valid_key('z'):
    press_key('z', 0.5)
```

---
<a name="Ejemplos"></a>
## 💡 Ejemplos Completos

Consulta `examples.py` para demostraciones exhaustivas de todas las funciones.

### Ejecutar Ejemplos
```bash
python examples.py
```

---
<a name="Requisitos"></a>
## 📋 Requisitos

- Python 3.8 o superior
- pynput (para control de teclado)
- pywin32 (para gestión de ventanas - opcional)

### Instalar Requisitos
```bash
pip install -r requirements.txt
```

---

## 🛠️ Patrones Comunes

### Patrón de Reintentos
```python
def retry_action(key, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        print(f"Intento {attempt}/{max_attempts}")
        press_key(key, 0.3)
        if attempt < max_attempts:
            wait_random(0.5, 1.5)

retry_action('z', max_attempts=3)
```

### Bucle Controlado por Tiempo
```python
import time

start = time.time()
duration = 60  # 60 segundos

while time.time() - start < duration:
    press_key('z', 0.3)
    wait_random(1, 2)
```

### Acción Inteligente
```python
def smart_action(attack=True, move=False):
    if attack:
        repeat_key('z', times=3, press_duration=0.2)
    if move:
        press_key(get_random_direction_key(), 0.3)
    wait_random(1, 2)

smart_action(attack=True, move=True)
```

---
<a name="Licencia"></a>
## 📝 Licencia

Licencia MIT - Siéntete libre de usar en tus proyectos

---

## 🤝 Contribuir

¿Tienes sugerencias? ¿Encontraste un bug? ¡Abre un issue o contribuye!

---

## 📞 Soporte

Para más información:
- Revisa `examples.py` para demostraciones prácticas
- Lee docstrings en `utils.py`
- Consulta este README para referencia de API

---

**Last Update:** 2026-06-01  
**Version:** 1.0
