# Utils Repository Structure / Estructura del Repositorio Utils

## 📁 Files Overview

### Core Module
- **`utils.py`** (600+ lines)
  - 17 reusable functions
  - Full documentation
  - Error handling included
  - Ready to use

### Documentation
- **`README.md`** (Bilingual: English/Español)
  - Complete API reference
  - Function descriptions
  - Usage examples
  - Common patterns

- **`GETTING_STARTED.md`** (Bilingual)
  - Quick setup guide
  - First steps
  - Common use cases
  - Troubleshooting

### Examples
- **`examples.py`** (12 practical examples)
  - Import demos
  - Keyboard control
  - File management
  - Window management
  - Complete bot example

### Configuration
- **`requirements.txt`**
  - pynput>=1.7.6
  - pywin32>=305

- **`.gitignore`**
  - Python cache files
  - Virtual environments
  - Log files
  - IDE files

### Licensing
- **`LICENSE`**
  - MIT License
  - Free to use and modify

---

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Try examples:**
   ```bash
   python examples.py
   ```

3. **Use in your code:**
   ```python
   from utils import press_key, wait
   press_key('z', 0.5)
   wait(2)
   ```

---

## 📚 Function Categories (17 Total)

### Keyboard (4 functions)
- `press_key()` - Single key press
- `repeat_key()` - Repeat key N times
- `press_key_sequence()` - Execute key sequence
- `get_random_direction_key()` - Random direction

### Numbers (2 functions)
- `random_int()` - Random integer
- `random_float()` - Random decimal

### Time (2 functions)
- `wait()` - Fixed delay
- `wait_random()` - Random delay

### Files (4 functions)
- `load_config_file()` - Read file
- `save_config_file()` - Write file
- `file_exists()` - Check if exists
- `get_files_in_directory()` - List files

### Windows (3 functions)
- `find_window_by_title()` - Find window
- `focus_window()` - Focus window
- `get_window_rect()` - Get window size

### Utilities (2 functions)
- `setup_logger()` - Configure logging
- `is_valid_key()` - Validate key

---

## 💡 Usage Examples

### Example 1: Simple Key Press
```python
from utils import press_key
press_key('z', 0.5)
```

### Example 2: Repeated Action
```python
from utils import repeat_key
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

### Example 3: Load Config
```python
from utils import load_config_file
config = load_config_file('config.txt')
```

### Example 4: Window Management
```python
from utils import find_window_by_title, focus_window
hwnd, title = find_window_by_title("MyApp")
if hwnd:
    focus_window(hwnd)
```

---

## 📖 File Descriptions

| File | Size | Purpose |
|------|------|---------|
| utils.py | 600+ lines | Main module with all functions |
| examples.py | 400+ lines | 12 practical examples |
| README.md | 800+ lines | Full API documentation (bilingual) |
| GETTING_STARTED.md | 150+ lines | Quick start guide (bilingual) |
| requirements.txt | 2 lines | Dependencies |
| .gitignore | 40+ lines | Git ignore rules |
| LICENSE | 20 lines | MIT License |

---

## ✨ Key Features

✅ **Well-Documented** - Every function has docstrings and examples
✅ **Error Handling** - Built-in exception management
✅ **Flexible** - Works with strings and Key objects
✅ **Modular** - Import only what you need
✅ **Tested** - Examples demonstrate all functions
✅ **Licensed** - MIT - Free to use and modify

---

## 🔧 System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows (for window management)
- **Dependencies:** pynput, pywin32 (optional)

---

## 🎯 Use Cases

- **Game Bots** - Automated gameplay
- **GUI Automation** - Control applications
- **Testing** - Automated testing of keyboard input
- **Scripts** - Automate repetitive tasks

---

## 📞 Support

**Documentation:**
- Complete API docs in `README.md`
- Examples in `examples.py`
- Quick start in `GETTING_STARTED.md`

**Learning:**
1. Read `GETTING_STARTED.md`
2. Run `python examples.py`
3. Check function docstrings
4. Review `README.md` for details

---

## 📝 License

MIT License - See `LICENSE` file for details.

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to improve!

---

## 📊 Statistics

- **17 Functions** total
- **600+ Lines** of code
- **12 Examples** included
- **2 Languages** (English & Spanish)
- **100% Documented** - Every function

---

**Last Updated:** 2026-06-01  
**Version:** 1.0  
**Status:** ✅ Production Ready

---

---

# Estructura del Repositorio Utils

## 📁 Descripción de Archivos

### Módulo Principal
- **`utils.py`** (600+ líneas)
  - 17 funciones reutilizables
  - Documentación completa
  - Manejo de errores incluido
  - Listo para usar

### Documentación
- **`README.md`** (Bilingüe: English/Español)
  - Referencia completa de API
  - Descripciones de funciones
  - Ejemplos de uso
  - Patrones comunes

- **`GETTING_STARTED.md`** (Bilingüe)
  - Guía de configuración rápida
  - Primeros pasos
  - Casos de uso comunes
  - Solución de problemas

### Ejemplos
- **`examples.py`** (12 ejemplos prácticos)
  - Demostraciones de importación
  - Control de teclado
  - Gestión de archivos
  - Gestión de ventanas
  - Ejemplo de bot completo

### Configuración
- **`requirements.txt`**
  - pynput>=1.7.6
  - pywin32>=305

- **`.gitignore`**
  - Archivos de caché de Python
  - Entornos virtuales
  - Archivos de registro
  - Archivos del IDE

### Licencia
- **`LICENSE`**
  - Licencia MIT
  - Libre de usar y modificar

---

## 🚀 Inicio Rápido

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Probar ejemplos:**
   ```bash
   python examples.py
   ```

3. **Usar en tu código:**
   ```python
   from utils import press_key, wait
   press_key('z', 0.5)
   wait(2)
   ```

---

## 📚 Categorías de Funciones (17 Total)

### Teclado (4 funciones)
- `press_key()` - Pulsación de tecla única
- `repeat_key()` - Repetir tecla N veces
- `press_key_sequence()` - Ejecutar secuencia de teclas
- `get_random_direction_key()` - Dirección aleatoria

### Números (2 funciones)
- `random_int()` - Entero aleatorio
- `random_float()` - Decimal aleatorio

### Tiempo (2 funciones)
- `wait()` - Retraso fijo
- `wait_random()` - Retraso aleatorio

### Archivos (4 funciones)
- `load_config_file()` - Leer archivo
- `save_config_file()` - Escribir archivo
- `file_exists()` - Verificar si existe
- `get_files_in_directory()` - Listar archivos

### Ventanas (3 funciones)
- `find_window_by_title()` - Encontrar ventana
- `focus_window()` - Enfocar ventana
- `get_window_rect()` - Obtener tamaño de ventana

### Utilidades (2 funciones)
- `setup_logger()` - Configurar logging
- `is_valid_key()` - Validar tecla

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Pulsación de Tecla Simple
```python
from utils import press_key
press_key('z', 0.5)
```

### Ejemplo 2: Acción Repetida
```python
from utils import repeat_key
repeat_key('z', times=5, press_duration=0.2, interval=0.1)
```

### Ejemplo 3: Cargar Configuración
```python
from utils import load_config_file
config = load_config_file('config.txt')
```

### Ejemplo 4: Gestión de Ventanas
```python
from utils import find_window_by_title, focus_window
hwnd, title = find_window_by_title("MiApp")
if hwnd:
    focus_window(hwnd)
```

---

## 📖 Descripciones de Archivos

| Archivo | Tamaño | Propósito |
|---------|--------|-----------|
| utils.py | 600+ líneas | Módulo principal con todas las funciones |
| examples.py | 400+ líneas | 12 ejemplos prácticos |
| README.md | 800+ líneas | Documentación completa de API (bilingüe) |
| GETTING_STARTED.md | 150+ líneas | Guía de inicio rápido (bilingüe) |
| requirements.txt | 2 líneas | Dependencias |
| .gitignore | 40+ líneas | Reglas de ignoro de Git |
| LICENSE | 20 líneas | Licencia MIT |

---

## ✨ Características Principales

✅ **Bien Documentado** - Cada función tiene docstrings y ejemplos
✅ **Manejo de Errores** - Gestión integrada de excepciones
✅ **Flexible** - Funciona con strings y objetos Key
✅ **Modular** - Importa solo lo que necesites
✅ **Probado** - Los ejemplos demuestran todas las funciones
✅ **Con Licencia** - MIT - Libre de usar y modificar

---

## 🔧 Requisitos del Sistema

- **Python:** 3.8 o superior
- **SO:** Windows (para gestión de ventanas)
- **Dependencias:** pynput, pywin32 (opcional)

---

## 🎯 Casos de Uso

- **Bots de Juegos** - Juego automático
- **Automatización de GUI** - Controlar aplicaciones
- **Pruebas** - Pruebas automatizadas de entrada de teclado
- **Scripts** - Automatizar tareas repetitivas

---

## 📞 Soporte

**Documentación:**
- Documentación API completa en `README.md`
- Ejemplos en `examples.py`
- Inicio rápido en `GETTING_STARTED.md`

**Aprendizaje:**
1. Lee `GETTING_STARTED.md`
2. Ejecuta `python examples.py`
3. Revisa docstrings de funciones
4. Consulta `README.md` para detalles

---

## 📝 Licencia

Licencia MIT - Ver archivo `LICENSE` para detalles.

---

## 🤝 Contribuir

¿Encontraste un bug? ¿Tienes una sugerencia? ¡Siéntete libre de mejorar!

---

## 📊 Estadísticas

- **17 Funciones** en total
- **600+ Líneas** de código
- **12 Ejemplos** incluidos
- **2 Idiomas** (English & Spanish)
- **100% Documentado** - Cada función

---

**Última Actualización:** 2026-06-01  
**Versión:** 1.0  
**Estado:** ✅ Listo para Producción
