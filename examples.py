"""
examples.py - Ejemplos Prácticos de Uso del Módulo utils.py
===========================================================

Demostraciones de cómo usar cada función del módulo utils.
Ejecuta los ejemplos que necesites según tu caso de uso.
"""

import logging
import os
from utils import (
    random_int,
    random_float,
    press_key,
    repeat_key,
    press_key_sequence,
    get_random_direction_key,
    wait,
    wait_random,
    load_config_file,
    save_config_file,
    file_exists,
    get_files_in_directory,
    find_window_by_title,
    focus_window,
    get_window_rect,
    setup_logger,
    is_valid_key
)
from pynput.keyboard import Key

# ============================================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================================

# Opción 1: Logger simple (consola)
logger = setup_logger('Examples', logging.INFO)

# Opción 2: Logger con archivo de log
# logger = setup_logger('Examples', logging.DEBUG, 'logs/examples.log')

def get_user_input(prompt, default=None):
    try:
        raw = input(prompt)
    except KeyboardInterrupt:
        print("\nEntrada cancelada por el usuario.")
        return None
    if raw is None:
        return None
    if raw == '' and default is not None:
        return default
    if raw.strip() == '' and raw != '':
        return ' '
    value = raw.strip()
    if not value and default is not None:
        return default
    return value


def prompt_int(prompt, default=None):
    while True:
        value = get_user_input(prompt, default)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            print("Por favor ingresa un número entero válido.")


def prompt_float(prompt, default=None):
    while True:
        value = get_user_input(prompt, default)
        if value is None:
            return None
        try:
            return float(value)
        except ValueError:
            print("Por favor ingresa un número válido.")


def parse_key_input(raw):
    if raw is None:
        return None
    raw = raw.strip().lower()
    if not raw:
        return None

    if '+' in raw:
        parts = [parse_key_input(part.strip()) for part in raw.split('+') if part.strip()]
        return tuple(parts)

    if raw == ' ':
        return Key.space

    arrow_map = {
        'vu': Key.up,
        'vd': Key.down,
        'vl': Key.left,
        'vr': Key.right,
    }
    numpad_map = {
        'nu': Key.up,
        'nd': Key.down,
        'nl': Key.left,
        'nr': Key.right,
    }

    if raw in arrow_map:
        return arrow_map[raw]
    if raw in numpad_map:
        return numpad_map[raw]

    named_keys = {
        'up': Key.up,
        'down': Key.down,
        'left': Key.left,
        'right': Key.right,
        'enter': Key.enter,
        'space': Key.space,
        'tab': Key.tab,
        'esc': Key.esc,
        'escape': Key.esc,
        'backspace': Key.backspace,
        'delete': Key.delete,
        'alt': Key.alt,
        'shift': Key.shift,
        'ctrl': Key.ctrl,
        'control': Key.ctrl,
    }

    if raw in named_keys:
        return named_keys[raw]

    if len(raw) == 1:
        return raw

    return raw


def prompt_key(prompt, default='z'):
    raw = get_user_input(prompt, default)
    if raw is None:
        return None
    key = parse_key_input(raw)
    if key is None:
        print("Tecla no reconocida. Se usará el valor predeterminado.")
        return default
    return key


# ============================================================================
# EJEMPLO 1: NÚMEROS ALEATORIOS
# ============================================================================

def example_random_numbers():
    """Demostración de funciones de números aleatorios"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Números Aleatorios")
    print("="*60)
    
    # Número entero aleatorio
    number = random_int(1, 10)
    logger.info(f"Número entero aleatorio (1-10): {number}")
    
    # Número decimal aleatorio
    float_number = random_float(0.5, 2.5)
    logger.info(f"Número decimal aleatorio (0.5-2.5): {float_number}")
    
    # Usar en un bucle
    logger.info("Generando 5 números aleatorios:")
    for i in range(5):
        num = random_int(1, 100)
        logger.info(f"  [{i+1}] {num}")


# ============================================================================
# EJEMPLO 2: PRESIONAR TECLAS
# ============================================================================

def example_press_keys():
    """Demostración de funciones de teclado"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Presionar Teclas")
    print("="*60)
    
    logger.info("Presionando 'z' por 0.5 segundos (activa la ventana del juego)...")
    # press_key('z', 0.5)
    logger.info("✓ Tecla presionada")
    
    logger.info("\nPresionando flecha arriba...")
    # press_key(Key.up, 0.3)
    logger.info("✓ Flecha presionada")


# ============================================================================
# EJEMPLO 3: REPETIR TECLA
# ============================================================================

def example_repeat_key():
    """Demostración de repetición de teclas"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Repetir Tecla")
    print("="*60)
    
    logger.info("Presionando 'z' 5 veces (puede usarse para ataques)...")
    # repeat_key('z', times=5, press_duration=0.2, interval=0.1)
    logger.info("✓ Repetición completada")
    
    logger.info("\nPresionando flecha derecha 3 veces...")
    # repeat_key(Key.right, times=3, press_duration=0.1, interval=0.05)
    logger.info("✓ Movimiento completado")


# ============================================================================
# EJEMPLO 4: SECUENCIA DE TECLAS
# ============================================================================

def example_key_sequence():
    """Demostración de secuencias de teclas"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Secuencia de Teclas")
    print("="*60)
    
    logger.info("Ejecutando secuencia: z, x, z")
    # press_key_sequence(['z', 'x', 'z'], 0.2, 0.1)
    logger.info("✓ Secuencia ejecutada")
    
    logger.info("\nEjecutando movimiento: arriba, arriba, derecha, abajo")
    movements = [Key.up, Key.up, Key.right, Key.down]
    # press_key_sequence(movements, 0.15, 0.05)
    logger.info("✓ Movimiento ejecutado")


# ============================================================================
# EJEMPLO 5: DIRECCIÓN ALEATORIA
# ============================================================================

def example_random_direction():
    """Demostración de dirección aleatoria"""
    print("\n" + "="*60)
    print("EJEMPLO 5: Dirección Aleatoria")
    print("="*60)
    
    logger.info("Generando 5 direcciones aleatorias:")
    for i in range(5):
        direction = get_random_direction_key()
        logger.info(f"  [{i+1}] Dirección: {direction}")


# ============================================================================
# EJEMPLO 6: TIEMPO Y ESPERA
# ============================================================================

def example_wait():
    """Demostración de funciones de espera"""
    print("\n" + "="*60)
    print("EJEMPLO 6: Tiempo y Espera")
    print("="*60)
    
    logger.info("Esperando 1 segundo...")
    wait(1)
    logger.info("✓ Espera completada")
    
    logger.info("\nEsperando tiempo aleatorio (1-3 segundos)...")
    # wait_random(1, 3)  # Descomentar para esperar realmente
    logger.info("✓ Espera aleatoria completada")


# ============================================================================
# EJEMPLO 7: ARCHIVOS DE CONFIGURACIÓN
# ============================================================================

def example_config_files():
    """Demostración de manejo de archivos"""
    print("\n" + "="*60)
    print("EJEMPLO 7: Archivos de Configuración")
    print("="*60)
    
    # Guardar configuración
    config_data = [
        "# Mi Configuración",
        "nombre=MiBot",
        "velocidad=5",
        "modo=farming"
    ]
    
    logger.info("Guardando configuración...")
    if save_config_file('example_config.txt', config_data):
        logger.info("✓ Configuración guardada")
    
    # Cargar configuración
    logger.info("Cargando configuración...")
    lines = load_config_file('example_config.txt')
    if lines:
        logger.info(f"✓ Configuración cargada ({len(lines)} líneas):")
        for line in lines:
            logger.info(f"    {line.strip()}")
    
    # Verificar existencia
    if file_exists('example_config.txt'):
        logger.info("✓ Archivo existe")
    else:
        logger.warning("✗ Archivo no existe")


# ============================================================================
# EJEMPLO 8: LISTAR ARCHIVOS
# ============================================================================

def example_list_files():
    """Demostración de listado de archivos"""
    print("\n" + "="*60)
    print("EJEMPLO 8: Listar Archivos")
    print("="*60)
    
    # Listar archivos Python
    logger.info("Buscando archivos Python en directorio actual:")
    py_files = get_files_in_directory('.', ['.py'])
    logger.info(f"Encontrados {len(py_files)} archivos:")
    for file in py_files[:5]:  # Mostrar primeros 5
        logger.info(f"  - {file}")
    
    if len(py_files) > 5:
        logger.info(f"  ... y {len(py_files) - 5} más")


# ============================================================================
# EJEMPLO 9: VALIDACIÓN DE TECLAS
# ============================================================================

def example_validate_keys():
    """Demostración de validación de teclas"""
    print("\n" + "="*60)
    print("EJEMPLO 9: Validación de Teclas")
    print("="*60)
    
    test_keys = ['z', 'x', 123, Key.up, None, 'hello']
    
    for key in test_keys:
        valid = is_valid_key(key)
        status = "✓ Válida" if valid else "✗ Inválida"
        logger.info(f"Tecla '{key}': {status}")


# ============================================================================
# EJEMPLO 10: BOT COMPLETO SIMPLIFICADO
# ============================================================================

def example_simple_bot():
    """Bot simplificado demostrando uso integrado"""
    print("\n" + "="*60)
    print("EJEMPLO 10: Bot Simplificado")
    print("="*60)
    
    logger.info("Iniciando bot simplificado...")
    
    # Cargar configuración
    config = load_config_file('example_config.txt')
    if config:
        logger.info(f"Configuración cargada: {len(config)} líneas")
    
    # Simular bucle principal
    logger.info("Ejecutando 3 iteraciones:")
    for iteration in range(1, 4):
        logger.info(f"\n  [Iteración {iteration}]")
        
        # Acción aleatoria
        action = random_int(1, 3)
        if action == 1:
            logger.info("    → Presionando ataque")
            # repeat_key('z', times=3, press_duration=0.1)
        elif action == 2:
            logger.info("    → Moviendo en dirección aleatoria")
            # direction = get_random_direction_key()
            # press_key(direction, 0.2)
        else:
            logger.info("    → Esperando")
            # wait_random(1, 2)
    
    logger.info("\n✓ Bot completado")


# ============================================================================
# EJEMPLO 11: PATRÓN DE REINTENTOS
# ============================================================================

def example_retry_pattern():
    """Patrón de reintentos automáticos"""
    print("\n" + "="*60)
    print("EJEMPLO 11: Patrón de Reintentos")
    print("="*60)
    
    def attempt_action(key, max_attempts=3):
        """Intenta una acción múltiples veces"""
        for attempt in range(1, max_attempts + 1):
            logger.info(f"  Intento {attempt}/{max_attempts}...")
            # press_key(key, 0.3)
            
            if attempt < max_attempts:
                wait_random(0.5, 1.5)
        
        logger.info("  ✓ Acción completada después de múltiples intentos")
    
    logger.info("Intentando presionar 'z' 3 veces:")
    attempt_action('z', max_attempts=3)


# ============================================================================
# EJEMPLO 12: BUCLE CONTROLADO POR TIEMPO
# ============================================================================

def example_timed_loop():
    """Bucle que se ejecuta durante un tiempo específico"""
    print("\n" + "="*60)
    print("EJEMPLO 12: Bucle Controlado por Tiempo")
    print("="*60)
    
    import time
    
    logger.info("Ejecutando bucle durante 5 segundos (simulado)...")
    
    # Simular bucle
    start = time.time()
    iterations = 0
    
    while time.time() - start < 5:
        iterations += 1
        
        # Simular una acción
        if iterations % 2 == 0:
            logger.info(f"  Iteración {iterations}")
        
        if iterations >= 5:  # Para demo, solo 5 iteraciones
            break
        
        wait_random(0.5, 1)
    
    logger.info(f"✓ Bucle completado ({iterations} iteraciones)")


# ============================================================================
# INTERACTIVE EXAMPLES
# ============================================================================

def confirm_action(prompt, default='n'):
    answer = get_user_input(f"{prompt} [{default}] ", default)
    if answer is None:
        return False
    return answer.strip().lower().startswith('y')


def prompt_key_sequence(prompt="Enter key sequence separated by commas (use v* for arrows, n* for numpad) [z,x,z]: ", default='z,x,z'):
    raw = get_user_input(prompt, default)
    if raw is None:
        return None
    tokens = [token.strip() for token in raw.replace(',', ' ').split() if token.strip()]
    return [parse_key_input(token) for token in tokens]


def run_random_numbers():
    print("\n" + "="*60)
    print("RUNNING: Random Numbers Example")
    print("="*60)
    example_random_numbers()


def run_press_key_interactive():
    print("\n" + "="*60)
    print("RUNNING: Press Key Example")
    print("="*60)
    key = prompt_key("Enter key to press (single char or v{u,d,l,r}, n{u,d,l,r}) [z]: ", 'z')
    if key is None:
        return
    duration = prompt_float("Enter duration in seconds [0.5]: ", 0.5)
    if duration is None:
        return
    if confirm_action("Execute real key press? y/n", 'n'):
        press_key(key, duration)
        logger.info(f"✓ press_key executed: {key} for {duration}s")
    else:
        logger.info(f"Simulated press_key({key}, {duration})")


def run_repeat_key_interactive():
    print("\n" + "="*60)
    print("RUNNING: Repeat Key Example")
    print("="*60)
    key = prompt_key("Enter key to repeat (single char or v{u,d,l,r}, n{u,d,l,r}) [z]: ", 'z')
    if key is None:
        return
    times = prompt_int("Enter times to repeat [5]: ", 5)
    if times is None:
        return
    press_duration = prompt_float("Enter press duration [0.2]: ", 0.2)
    if press_duration is None:
        return
    interval = prompt_float("Enter interval between presses [0.1]: ", 0.1)
    if interval is None:
        return
    final_wait = prompt_float("Enter final wait after presses [0.0]: ", 0.0)
    if final_wait is None:
        return
    if confirm_action("Execute real repeat_key? y/n", 'n'):
        repeat_key(key, times=times, press_duration=press_duration, interval=interval, final_wait=final_wait)
        logger.info(f"✓ repeat_key executed: {key}, times={times}")
    else:
        logger.info(f"Simulated repeat_key({key}, times={times}, press_duration={press_duration}, interval={interval}, final_wait={final_wait})")


def run_key_sequence_interactive():
    print("\n" + "="*60)
    print("RUNNING: Key Sequence Example")
    print("="*60)
    sequence = prompt_key_sequence()
    if sequence is None or not sequence:
        return
    press_duration = prompt_float("Enter press duration [0.2]: ", 0.2)
    if press_duration is None:
        return
    interval = prompt_float("Enter interval between keys [0.1]: ", 0.1)
    if interval is None:
        return
    if confirm_action("Execute real key sequence? y/n", 'n'):
        press_key_sequence(sequence, press_duration=press_duration, interval=interval)
        logger.info("✓ press_key_sequence executed")
    else:
        logger.info(f"Simulated press_key_sequence({sequence}, press_duration={press_duration}, interval={interval})")


def run_random_direction_interactive():
    print("\n" + "="*60)
    print("RUNNING: Random Direction Example")
    print("="*60)
    count = prompt_int("How many directions to generate? [5]: ", 5)
    if count is None:
        return
    logger.info(f"Generating {count} random directions:")
    for i in range(count):
        direction = get_random_direction_key()
        logger.info(f"  [{i+1}] Direction: {direction}")


def run_wait_interactive():
    print("\n" + "="*60)
    print("RUNNING: Wait Example")
    print("="*60)
    seconds = prompt_float("Enter seconds to wait [1.0]: ", 1.0)
    if seconds is None:
        return
    logger.info(f"Waiting {seconds} seconds...")
    wait(seconds)
    logger.info("✓ Wait completed")


def run_wait_random_interactive():
    print("\n" + "="*60)
    print("RUNNING: Wait Random Example")
    print("="*60)
    min_seconds = prompt_float("Enter minimum seconds [1.0]: ", 1.0)
    if min_seconds is None:
        return
    max_seconds = prompt_float("Enter maximum seconds [3.0]: ", 3.0)
    if max_seconds is None:
        return
    if max_seconds < min_seconds:
        min_seconds, max_seconds = max_seconds, min_seconds
    logger.info(f"Waiting random time between {min_seconds} and {max_seconds} seconds...")
    wait_random(min_seconds, max_seconds)
    logger.info("✓ Random wait completed")


def run_config_files_interactive():
    print("\n" + "="*60)
    print("RUNNING: Config Files Example")
    print("="*60)
    save_path = get_user_input("Enter save file path [example_config.txt]: ", 'example_config.txt')
    if save_path is None:
        return
    config_data = [
        "# Mi Configuración",
        "nombre=MiBot",
        "velocidad=5",
        "modo=farming"
    ]
    logger.info(f"Saving configuration to {save_path}...")
    if save_config_file(save_path, config_data):
        logger.info("✓ Configuration saved")
    logger.info(f"Loading configuration from {save_path}...")
    lines = load_config_file(save_path)
    if lines:
        logger.info(f"✓ Loaded {len(lines)} lines:")
        for line in lines:
            logger.info(f"    {line.strip()}")
    if file_exists(save_path):
        logger.info("✓ File exists")
    else:
        logger.warning("✗ File does not exist")


def run_list_files_interactive():
    print("\n" + "="*60)
    print("RUNNING: List Files Example")
    print("="*60)
    directory = get_user_input("Enter directory to search [.]: ", '.')
    if directory is None:
        return
    extensions_raw = get_user_input("Enter extensions separated by commas [.py]: ", '.py')
    if extensions_raw is None:
        return
    extensions = [ext.strip() for ext in extensions_raw.split(',') if ext.strip()]
    logger.info(f"Searching in {directory} for extensions {extensions}")
    files = get_files_in_directory(directory, extensions or None)
    logger.info(f"Found {len(files)} files:")
    for file in files[:10]:
        logger.info(f"  - {file}")
    if len(files) > 10:
        logger.info(f"  ... and {len(files) - 10} more")


def run_validate_keys_interactive():
    print("\n" + "="*60)
    print("RUNNING: Validate Keys Example")
    print("="*60)
    raw = get_user_input("Enter keys separated by commas to validate [z,x,vu,hello]: ", 'z,x,vu,hello')
    if raw is None:
        return
    keys = [parse_key_input(token) for token in raw.replace(',', ' ').split() if token.strip()]
    for key in keys:
        valid = is_valid_key(key)
        status = "✓ Valid" if valid else "✗ Invalid"
        logger.info(f"Key '{key}': {status}")


def run_simple_bot_interactive():
    print("\n" + "="*60)
    print("RUNNING: Simple Bot Example")
    print("="*60)
    iterations = prompt_int("Enter number of iterations [3]: ", 3)
    if iterations is None:
        return
    logger.info("Starting simplified bot simulation...")
    config = load_config_file('example_config.txt')
    if config:
        logger.info(f"Loaded configuration: {len(config)} lines")
    logger.info(f"Executing {iterations} iterations:")
    for iteration in range(1, iterations + 1):
        logger.info(f"  [Iteration {iteration}]")
        action = random_int(1, 3)
        if action == 1:
            logger.info("    → Attack press simulated")
        elif action == 2:
            logger.info("    → Moving in random direction simulated")
        else:
            logger.info("    → Waiting simulated")
            wait_random(1, 2)
    logger.info("\n✓ Simple bot simulation completed")


def run_retry_pattern_interactive():
    print("\n" + "="*60)
    print("RUNNING: Retry Pattern Example")
    print("="*60)
    key = prompt_key("Enter key to retry (single char or v{u,d,l,r}, n{u,d,l,r}) [z]: ", 'z')
    if key is None:
        return
    max_attempts = prompt_int("Enter max attempts [3]: ", 3)
    if max_attempts is None:
        return
    def attempt_action(action_key, attempts):
        for attempt in range(1, attempts + 1):
            logger.info(f"  Attempt {attempt}/{attempts}...")
            if confirm_action("  Execute real key press? y/n", 'n'):
                press_key(action_key, 0.3)
            if attempt < attempts:
                wait_random(0.5, 1.5)
        logger.info("  ✓ Action completed")
    logger.info(f"Retrying key {key} up to {max_attempts} times")
    attempt_action(key, max_attempts)


def run_timed_loop_interactive():
    print("\n" + "="*60)
    print("RUNNING: Timed Loop Example")
    print("="*60)
    seconds = prompt_int("Enter total duration in seconds [5]: ", 5)
    if seconds is None:
        return
    import time
    logger.info(f"Running loop for {seconds} seconds...")
    start = time.time()
    iterations = 0
    while time.time() - start < seconds:
        iterations += 1
        logger.info(f"  Iteration {iterations}")
        wait_random(0.5, 1)
        if iterations >= 100:
            logger.warning("Reached 100 iterations limit, stopping for safety")
            break
    logger.info(f"✓ Timed loop completed ({iterations} iterations)")


def run_all_examples():
    run_random_numbers()
    run_press_key_interactive()
    run_repeat_key_interactive()
    run_key_sequence_interactive()
    run_random_direction_interactive()
    run_wait_interactive()
    run_wait_random_interactive()
    run_config_files_interactive()
    run_list_files_interactive()
    run_validate_keys_interactive()
    run_simple_bot_interactive()
    run_retry_pattern_interactive()
    run_timed_loop_interactive()


def main():
    """Muestra un menú interactivo para seleccionar el ejemplo a ejecutar"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  EJEMPLOS DE USO - MÓDULO utils.py".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    options = [
        ("Random numbers", run_random_numbers),
        ("Press key", run_press_key_interactive),
        ("Repeat key", run_repeat_key_interactive),
        ("Key sequence", run_key_sequence_interactive),
        ("Random direction", run_random_direction_interactive),
        ("Wait", run_wait_interactive),
        ("Wait random", run_wait_random_interactive),
        ("Config files", run_config_files_interactive),
        ("List files", run_list_files_interactive),
        ("Validate keys", run_validate_keys_interactive),
        ("Simple bot", run_simple_bot_interactive),
        ("Retry pattern", run_retry_pattern_interactive),
        ("Timed loop", run_timed_loop_interactive),
    ]
    while True:
        print("\nAvailable examples:")
        for index, (label, _) in enumerate(options, start=1):
            print(f"  {index}. {label}")
        print(f"  {len(options) + 1}. Run all examples")
        print("  0. Exit")
        selection = prompt_int("Select example number: ", 0)
        if selection is None or selection == 0:
            print("Exiting examples.")
            break
        if selection == len(options) + 1:
            run_all_examples()
            continue
        if 1 <= selection <= len(options):
            _, action = options[selection - 1]
            action()
            continue
        print("Invalid selection. Please enter a valid number.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nPrograma interrumpido por el usuario")
    except Exception as e:
        logger.error(f"Error: {e}")
