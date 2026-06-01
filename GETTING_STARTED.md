# Getting Started / Guía de Inicio Rápido

## English

### 1. Setup
```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. First Use
```python
from utils import press_key, wait

# Press 'z' for 0.5 seconds
press_key('z', 0.5)

# Wait 2 seconds
wait(2)
```

### 3. Learn More
- Read `README.md` for full API documentation
- Run `python examples.py` to see all functions in action
- Check function docstrings in `utils.py`

### 4. Common Use Cases

**Press a key multiple times:**
```python
from utils import repeat_key
repeat_key('z', times=5)
```

**Wait a random amount of time:**
```python
from utils import wait_random
wait_random(1, 5)
```

**Load a configuration file:**
```python
from utils import load_config_file
config = load_config_file('config.txt')
```

**Find and focus a window:**
```python
from utils import find_window_by_title, focus_window
hwnd, title = find_window_by_title("MyApp")
if hwnd:
    focus_window(hwnd)
```

---

## Español

### 1. Configuración
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 2. Primer Uso
```python
from utils import press_key, wait

# Presionar 'z' por 0.5 segundos
press_key('z', 0.5)

# Esperar 2 segundos
wait(2)
```

### 3. Aprender Más
- Lee `README.md` para documentación completa de API
- Ejecuta `python examples.py` para ver todas las funciones
- Revisa docstrings en `utils.py`

### 4. Casos de Uso Comunes

**Presionar una tecla múltiples veces:**
```python
from utils import repeat_key
repeat_key('z', times=5)
```

**Esperar un tiempo aleatorio:**
```python
from utils import wait_random
wait_random(1, 5)
```

**Cargar un archivo de configuración:**
```python
from utils import load_config_file
config = load_config_file('config.txt')
```

**Encontrar y enfocar una ventana:**
```python
from utils import find_window_by_title, focus_window
hwnd, title = find_window_by_title("MiApp")
if hwnd:
    focus_window(hwnd)
```

---

## Next Steps / Próximos Pasos

1. **Explore Functions** - Check out all 17 functions in `utils.py`
2. **Run Examples** - Execute `examples.py` to see practical demos
3. **Read API Docs** - Check `README.md` for complete reference
4. **Build Your Script** - Start using utils in your own code

---

1. **Explora Funciones** - Revisa las 17 funciones en `utils.py`
2. **Ejecuta Ejemplos** - Corre `examples.py` para ver demostraciones
3. **Lee Documentación** - Consulta `README.md` para referencia completa
4. **Construye Tu Script** - Comienza a usar utils en tu código

---

## Troubleshooting / Solución de Problemas

### "No module named 'pynput'"
```bash
pip install pynput
```

### "win32gui not found"
```bash
pip install pywin32
```

### Key presses not working?
- Make sure the target window is in focus
- Check your key syntax (use 'z' for characters, Key.up for special keys)
- Add delays with `wait()` if presses happen too fast

### ¿Las pulsaciones de tecla no funcionan?
- Asegúrate de que la ventana objetivo esté enfocada
- Verifica tu sintaxis de tecla (usa 'z' para caracteres, Key.up para teclas especiales)
- Añade retrasos con `wait()` si las pulsaciones ocurren demasiado rápido

---

**Need help?** Check examples.py or README.md for more info!
**¿Necesitas ayuda?** ¡Consulta examples.py o README.md para más información!
