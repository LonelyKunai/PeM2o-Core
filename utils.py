"""
Módulo de Utilidades Comunes - Farming Bot
=========================================

Funciones básicas reutilizables para cualquier programador.
Centraliza operaciones comunes de teclado, ventanas, tiempos y configuración.
"""

import random
import logging
import os
from time import sleep
from pynput.keyboard import Controller, Key

# Configurar logger
logger = logging.getLogger(__name__)
kb = Controller()

# ============================================================================
# FUNCIONES DE NÚMEROS Y ALEATORIOS - OPTIMIZADAS
# ============================================================================

# Cache para evitar recrear objetos Key repetidamente
_DIRECTION_KEYS_CACHE = None

def _get_direction_keys():
    """Obtiene la lista de teclas direccionales (cacheada)."""
    global _DIRECTION_KEYS_CACHE
    if _DIRECTION_KEYS_CACHE is None:
        _DIRECTION_KEYS_CACHE = [Key.up, Key.down, Key.right, Key.left]
    return _DIRECTION_KEYS_CACHE


def random_int(min_value, max_value):
    """
    Genera un número entero aleatorio entre dos valores.
    
    Args:
        min_value (int): Valor mínimo (incluido)
        max_value (int): Valor máximo (incluido)
    
    Returns:
        int: Número entero aleatorio
    
    Ejemplo:
        >>> delay = random_int(1, 5)
    """
    return random.randint(min_value, max_value)


def random_float(min_value, max_value):
    """
    Genera un número decimal aleatorio entre dos valores.
    
    Args:
        min_value (float): Valor mínimo (incluido)
        max_value (float): Valor máximo (incluido)
    
    Returns:
        float: Número decimal aleatorio
    
    Ejemplo:
        >>> delay = random_float(0.1, 0.5)
    """
    return random.uniform(min_value, max_value)


# ============================================================================
# FUNCIONES DE TECLADO
# ============================================================================

def get_random_direction_key():
    """
    Retorna una tecla de dirección aleatoria.
    
    Returns:
        Key: Una de las cuatro teclas direccionales (arriba, abajo, izquierda, derecha)
    
    Ejemplo:
        >>> direction = get_random_direction_key()
        >>> press_key(direction, 0.5)
    """
    return random.choice(_get_direction_keys())


def press_key(key, duration=0.1):
    """
    Presiona una tecla o combinación de teclas por un tiempo específico.
    
    Args:
        key (str, Key, list, tuple): Tecla o combinación a presionar
            (ej: 'z', Key.up, [Key.alt, Key.shift, 'b'])
        duration (float): Segundos que se mantiene presionada. Default: 0.1
    
    Returns:
        bool: True si se ejecutó exitosamente, False si hubo error
    
    Ejemplo:
        >>> press_key('z', 0.5)
        >>> press_key(Key.up, 0.2)
        >>> press_key([Key.alt, Key.shift, 'b'], 0.2)
    """
    try:
        if isinstance(key, (list, tuple)):
            for k in key:
                kb.press(k)
            sleep(duration)
            for k in reversed(key):
                kb.release(k)
        else:
            kb.press(key)
            sleep(duration)
            kb.release(key)
        logger.debug("Tecla presionada: %s (%ss)", key, duration)
        return True
    except Exception as e:
        logger.error("Error presionando tecla %s: %s", key, e)
        return False


def press_key_sequence(keys, press_duration=0.1, interval=0.05):
    """
    Presiona una secuencia de teclas con intervalos.
    
    Args:
        keys (list, tuple, str): Teclas a presionar
        press_duration (float): Segundos que se mantiene cada tecla presionada. Default: 0.1
        interval (float): Segundos entre cada pulsación. Default: 0.05
    
    Returns:
        bool: True si se ejecutó exitosamente, False si hubo error
    
    Ejemplo:
        >>> press_key_sequence(['z', 'x', 'z'], 0.2, 0.1)
        >>> press_key_sequence([Key.ctrl, 'c'], 0.1)
    """
    try:
        if isinstance(keys, str):
            keys = list(keys)
        
        for key in keys:
            if isinstance(key, (list, tuple)):
                for k in key:
                    kb.press(k)
                sleep(press_duration)
                for k in reversed(key):
                    kb.release(k)
            else:
                kb.press(key)
                sleep(press_duration)
                kb.release(key)
            sleep(interval)
        
        logger.debug("Secuencia ejecutada: %s", keys)
        return True
    except Exception as e:
        logger.error("Error ejecutando secuencia: %s", e)
        return False


def repeat_key(key, times=1, press_duration=0.1, interval=0.05, final_wait=0.0):
    """
    Repite la presión de una tecla o combinación de teclas múltiples veces.
    
    Args:
        key (str, Key, list, tuple): Tecla o combinación a presionar repetidamente
        times (int): Número de veces a presionar. Default: 1
        press_duration (float): Segundos que se mantiene presionada. Default: 0.1
        interval (float): Segundos entre pulsaciones. Default: 0.05
        final_wait (float): Segundos de espera al final. Default: 0.0
    
    Returns:
        bool: True si se ejecutó exitosamente, False si hubo error
    
    Ejemplo:
        >>> repeat_key('z', 5, 0.2, 0.1)
        >>> repeat_key([Key.alt, Key.shift, 'b'], 3, 0.1, 0.05, 1.0)
    """
    try:
        for _ in range(times):
            if isinstance(key, (list, tuple)):
                for k in key:
                    kb.press(k)
                sleep(press_duration)
                for k in reversed(key):
                    kb.release(k)
            else:
                kb.press(key)
                sleep(press_duration)
                kb.release(key)
            sleep(interval)
        
        sleep(final_wait)
        logger.debug("Tecla repetida: %s (%s veces)", key, times)
        return True
    except Exception as e:
        logger.error("Error repitiendo tecla %s: %s", key, e)
        return False


# ============================================================================
# FUNCIONES DE VENTANAS (Windows)
# ============================================================================

def find_window_by_title(window_title_keywords):
    """
    Busca una ventana por palabras clave en su título.
    
    Args:
        window_title_keywords (str or list): Palabras clave a buscar en el título
    
    Returns:
        tuple: (hwnd, window_title) si se encuentra, (None, None) si no
    
    Ejemplo:
        >>> hwnd, title = find_window_by_title("PokeMMO")
        >>> hwnd, title = find_window_by_title(["Pokemon", "MMO"])
    """
    try:
        import win32gui
        import win32con
        
        if isinstance(window_title_keywords, str):
            keywords = [window_title_keywords]
        else:
            keywords = window_title_keywords
        
        def enum_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if any(kw.lower() in title.lower() for kw in keywords):
                    windows.append((hwnd, title))
            return True
        
        windows = []
        win32gui.EnumWindows(enum_callback, windows)
        
        if windows:
            logger.info("Ventana encontrada: %s", windows[0][1])
            return windows[0]
        
        logger.warning("No se encontró ventana con keywords: %s", keywords)
        return None, None
        
    except ImportError:
        logger.warning("win32gui no disponible. Instala: pip install pywin32")
        return None, None
    except Exception as e:
        logger.error("Error buscando ventana: %s", e)
        return None, None


def focus_window(hwnd):
    """
    Enfoca una ventana y la trae al frente.
    
    Args:
        hwnd (int): Manejador de ventana (window handle)
    
    Returns:
        bool: True si se ejecutó exitosamente, False si hubo error
    
    Ejemplo:
        >>> hwnd, title = find_window_by_title("PokeMMO")
        >>> focus_window(hwnd)
    """
    try:
        import win32gui
        import win32con
        
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        logger.info("Ventana enfocada")
        return True
    except ImportError:
        logger.warning("win32gui no disponible")
        return False
    except Exception as e:
        logger.error("Error enfocando ventana: %s", e)
        return False


def get_window_rect(hwnd):
    """
    Obtiene las coordenadas y dimensiones de una ventana.
    
    Args:
        hwnd (int): Manejador de ventana (window handle)
    
    Returns:
        tuple: (x, y, width, height) de la ventana, o None si hay error
    
    Ejemplo:
        >>> hwnd, _ = find_window_by_title("PokeMMO")
        >>> x, y, w, h = get_window_rect(hwnd)
    """
    try:
        import win32gui
        
        rect = win32gui.GetWindowRect(hwnd)
        x, y, right, bottom = rect
        width = right - x
        height = bottom - y
        
        logger.debug("Ventana rect: x=%s, y=%s, w=%s, h=%s", x, y, width, height)
        return (x, y, width, height)
        
    except ImportError:
        logger.warning("win32gui no disponible")
        return None
    except Exception as e:
        logger.error("Error obteniendo rect de ventana: %s", e)
        return None


# ============================================================================
# FUNCIONES DE CONFIGURACIÓN Y ARCHIVOS
# ============================================================================

def load_config_file(filepath, encoding='utf-8'):
    """
    Lee un archivo de configuración (texto simple).
    
    Args:
        filepath (str): Ruta del archivo
        encoding (str): Codificación del archivo. Default: 'utf-8'
    
    Returns:
        list: Lista de líneas del archivo, o lista vacía si hay error
    
    Ejemplo:
        >>> lines = load_config_file('config.txt')
        >>> value = lines[0] if lines else ""
    """
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            lines = f.readlines()
        logger.info("Archivo cargado: %s (%s líneas)", filepath, len(lines))
        return lines
    except FileNotFoundError:
        logger.warning("Archivo no encontrado: %s", filepath)
        return []
    except Exception as e:
        logger.error("Error cargando archivo %s: %s", filepath, e)
        return []


def save_config_file(filepath, content, encoding='utf-8'):
    """
    Guarda contenido en un archivo.
    
    Args:
        filepath (str): Ruta del archivo
        content (str or list): Contenido a guardar (string o lista de líneas)
        encoding (str): Codificación del archivo. Default: 'utf-8'
    
    Returns:
        bool: True si se ejecutó exitosamente, False si hubo error
    
    Ejemplo:
        >>> save_config_file('output.txt', 'Contenido de ejemplo')
        >>> save_config_file('lines.txt', ['línea1', 'línea2'])
    """
    try:
        if isinstance(content, list):
            content = '\n'.join(content)
        
        dirname = os.path.dirname(filepath)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(filepath, 'w', encoding=encoding) as f:
            f.write(content)
        logger.info("Archivo guardado: %s", filepath)
        return True
    except Exception as e:
        logger.error("Error guardando archivo %s: %s", filepath, e)
        return False


def file_exists(filepath):
    """
    Verifica si un archivo existe.
    
    Args:
        filepath (str): Ruta del archivo
    
    Returns:
        bool: True si el archivo existe, False si no
    
    Ejemplo:
        >>> if file_exists('config.txt'):
        ...     data = load_config_file('config.txt')
    """
    return os.path.exists(filepath)


def get_files_in_directory(directory, extensions=None):
    """
    Obtiene lista de archivos en un directorio.
    
    Args:
        directory (str): Ruta del directorio
        extensions (list): Lista de extensiones a filtrar (ej: ['.png', '.jpg']). 
                          Si es None, retorna todos los archivos.
    
    Returns:
        list: Lista de rutas completas de archivos
    
    Ejemplo:
        >>> images = get_files_in_directory('mons/', ['.png', '.jpg'])
        >>> all_files = get_files_in_directory('data/')
    """
    try:
        if not os.path.exists(directory):
            logger.warning("Directorio no encontrado: %s", directory)
            return []
        
        files = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                if extensions is None:
                    files.append(filepath)
                else:
                    _, ext = os.path.splitext(filename)
                    if ext.lower() in extensions:
                        files.append(filepath)
        
        logger.debug("Encontrados %s archivos en %s", len(files), directory)
        return files
    except Exception as e:
        logger.error("Error listando directorio %s: %s", directory, e)
        return []


# ============================================================================
# FUNCIONES DE TIEMPO Y ESPERA
# ============================================================================

def wait(seconds):
    """
    Espera un número específico de segundos.
    
    Args:
        seconds (float): Segundos a esperar
    
    Ejemplo:
        >>> wait(2.5)
    """
    sleep(seconds)


def wait_random(min_seconds, max_seconds):
    """
    Espera un tiempo aleatorio entre dos valores.
    
    Args:
        min_seconds (float): Mínimo de segundos a esperar
        max_seconds (float): Máximo de segundos a esperar
    
    Ejemplo:
        >>> wait_random(1, 5)  # Espera entre 1 y 5 segundos aleatoriamente
    """
    delay = random.uniform(min_seconds, max_seconds)
    sleep(delay)


# ============================================================================
# FUNCIONES DE LOGGING
# ============================================================================

def setup_logger(name, level=logging.INFO, log_file=None):
    """
    Configura un logger personalizado.
    
    Args:
        name (str): Nombre del logger
        level (int): Nivel de logging. Default: logging.INFO
        log_file (str): Ruta del archivo de log (opcional)
    
    Returns:
        logging.Logger: Logger configurado
    
    Ejemplo:
        >>> my_logger = setup_logger('MyBot', logging.DEBUG)
        >>> my_logger.info("Iniciando...")
    """
    logger_obj = logging.getLogger(name)
    logger_obj.setLevel(level)
    
    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger_obj.addHandler(console_handler)
    
    # Handler para archivo (si se especifica)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger_obj.addHandler(file_handler)
    
    return logger_obj


# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def is_valid_key(key):
    """
    Valida si un valor es una tecla válida.
    
    Args:
        key: Tecla a validar
    
    Returns:
        bool: True si es una tecla válida
    
    Ejemplo:
        >>> is_valid_key('z')
        >>> is_valid_key(Key.up)
    """
    try:
        if isinstance(key, (str, int)):
            return True
        if hasattr(key, '__class__') and 'Key' in str(key.__class__):
            return True
        return False
    except:
        return False


# ============================================================================
# EXPORTAR TODAS LAS FUNCIONES
# ============================================================================

__all__ = [
    'random_int',
    'random_float',
    'get_random_direction_key',
    'press_key',
    'press_key_sequence',
    'repeat_key',
    'find_window_by_title',
    'focus_window',
    'get_window_rect',
    'load_config_file',
    'save_config_file',
    'file_exists',
    'get_files_in_directory',
    'wait',
    'wait_random',
    'setup_logger',
    'is_valid_key',
]
