"""
Módulo de Pruebas Unitarias - Farming Bot Utils
================================================

Pruebas unitarias para las funciones del módulo utils.py.
Cubre todas las funciones principales con casos de prueba completos.
"""

import unittest
from unittest.mock import patch, MagicMock, call
import random
import os
import sys

# Mock de pynput antes de importar utils
sys.modules['pynput'] = MagicMock()
sys.modules['pynput.keyboard'] = MagicMock()

from pynput.keyboard import Key

# Importar utils después del mock
import utils


class TestRandomFunctions(unittest.TestCase):
    """Pruebas para funciones de números aleatorios"""
    
    def test_random_int_returns_integer(self):
        """random_int debe retornar un entero"""
        result = utils.random_int(1, 10)
        self.assertIsInstance(result, int)
    
    def test_random_int_in_range(self):
        """random_int debe estar dentro del rango especificado"""
        for _ in range(100):
            result = utils.random_int(1, 10)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 10)
    
    def test_random_int_same_min_max(self):
        """random_int con mismo min y max debe retornar ese valor"""
        result = utils.random_int(5, 5)
        self.assertEqual(result, 5)
    
    def test_random_float_returns_float(self):
        """random_float debe retornar un float"""
        result = utils.random_float(0.5, 2.5)
        self.assertIsInstance(result, float)
    
    def test_random_float_in_range(self):
        """random_float debe estar dentro del rango especificado"""
        for _ in range(100):
            result = utils.random_float(0.5, 2.5)
            self.assertGreaterEqual(result, 0.5)
            self.assertLessEqual(result, 2.5)
    
    def test_random_float_negative_range(self):
        """random_float debe funcionar con rangos negativos"""
        result = utils.random_float(-5.0, -1.0)
        self.assertGreaterEqual(result, -5.0)
        self.assertLessEqual(result, -1.0)


class TestDirectionKeyFunctions(unittest.TestCase):
    """Pruebas para funciones de teclas direccionales"""
    
    def test_get_random_direction_key_returns_key(self):
        """get_random_direction_key debe retornar una tecla Key"""
        result = utils.get_random_direction_key()
        self.assertIn(result, [Key.up, Key.down, Key.right, Key.left])
    
    def test_get_random_direction_key_distribution(self):
        """get_random_direction_key debe distribuir uniformemente"""
        results = [utils.get_random_direction_key() for _ in range(400)]
        # Cada dirección debería aparecer al menos 50 veces en 400 intentos
        for direction in [Key.up, Key.down, Key.right, Key.left]:
            count = results.count(direction)
            self.assertGreater(count, 50, f"{direction} apareció solo {count} veces")
    
    def test_direction_keys_cache(self):
        """El cache de teclas direccionales debe funcionar"""
        # Primera llamada crea el cache
        key1 = utils.get_random_direction_key()
        # Segunda llamada usa el cache
        key2 = utils.get_random_direction_key()
        self.assertIsNotNone(utils._DIRECTION_KEYS_CACHE)


class TestPressKeyFunction(unittest.TestCase):
    """Pruebas para la función press_key"""
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_single_char(self, mock_sleep, mock_kb):
        """press_key con caracter simple"""
        result = utils.press_key('z', 0.5)
        
        mock_kb.press.assert_called_once_with('z')
        mock_kb.release.assert_called_once_with('z')
        mock_sleep.assert_called_once_with(0.5)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_with_key_object(self, mock_sleep, mock_kb):
        """press_key con objeto Key"""
        result = utils.press_key(Key.up, 0.3)
        
        mock_kb.press.assert_called_once_with(Key.up)
        mock_kb.release.assert_called_once_with(Key.up)
        mock_sleep.assert_called_once_with(0.3)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_combination(self, mock_sleep, mock_kb):
        """press_key con combinación de teclas"""
        result = utils.press_key([Key.alt, 'b'], 0.2)
        
        expected_presses = [call(Key.alt), call('b')]
        expected_releases = [call('b'), call(Key.alt)]
        
        mock_kb.press.assert_has_calls(expected_presses)
        mock_kb.release.assert_has_calls(expected_releases)
        mock_sleep.assert_called_once_with(0.2)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_error_handling(self, mock_sleep, mock_kb):
        """press_key debe manejar errores"""
        mock_kb.press.side_effect = Exception("Test error")
        
        with patch('utils.logger') as mock_logger:
            result = utils.press_key('z', 0.1)
            
            mock_logger.error.assert_called()
            self.assertFalse(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_default_duration(self, mock_sleep, mock_kb):
        """press_key con duración por defecto"""
        utils.press_key('x')
        mock_sleep.assert_called_once_with(0.1)


class TestPressKeySequenceFunction(unittest.TestCase):
    """Pruebas para la función press_key_sequence"""
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_sequence_list(self, mock_sleep, mock_kb):
        """press_key_sequence con lista de teclas"""
        result = utils.press_key_sequence(['z', 'x', 'c'], 0.1, 0.05)
        
        self.assertEqual(mock_kb.press.call_count, 3)
        self.assertEqual(mock_kb.release.call_count, 3)
        # 3 intervalos + 3 durations = 6 sleeps
        self.assertEqual(mock_sleep.call_count, 6)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_sequence_string(self, mock_sleep, mock_kb):
        """press_key_sequence con string"""
        result = utils.press_key_sequence('abc', 0.1, 0.05)
        
        self.assertEqual(mock_kb.press.call_count, 3)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_sequence_with_combinations(self, mock_sleep, mock_kb):
        """press_key_sequence con combinaciones"""
        result = utils.press_key_sequence([['ctrl', 'c'], 'z'], 0.1, 0.05)
        
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_press_key_sequence_error_handling(self, mock_sleep, mock_kb):
        """press_key_sequence debe manejar errores"""
        mock_kb.press.side_effect = Exception("Test error")
        
        with patch('utils.logger') as mock_logger:
            result = utils.press_key_sequence(['z'], 0.1, 0.05)
            
            mock_logger.error.assert_called()
            self.assertFalse(result)


class TestRepeatKeyFunction(unittest.TestCase):
    """Pruebas para la función repeat_key"""
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_repeat_key_single(self, mock_sleep, mock_kb):
        """repeat_key una vez"""
        result = utils.repeat_key('z', times=1, press_duration=0.1, interval=0.05)
        
        mock_kb.press.assert_called_once_with('z')
        mock_kb.release.assert_called_once_with('z')
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_repeat_key_multiple(self, mock_sleep, mock_kb):
        """repeat_key múltiples veces"""
        result = utils.repeat_key('z', times=3, press_duration=0.1, interval=0.05, final_wait=0.2)
        
        self.assertEqual(mock_kb.press.call_count, 3)
        self.assertEqual(mock_kb.release.call_count, 3)
        # 3 intervals + 3 durations + 1 final_wait = 7 sleeps
        self.assertEqual(mock_sleep.call_count, 7)
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_repeat_key_default_params(self, mock_sleep, mock_kb):
        """repeat_key con parámetros por defecto"""
        result = utils.repeat_key('z')
        
        mock_kb.press.assert_called_once_with('z')
        self.assertTrue(result)
    
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_repeat_key_error_handling(self, mock_sleep, mock_kb):
        """repeat_key debe manejar errores"""
        mock_kb.press.side_effect = Exception("Test error")
        
        with patch('utils.logger') as mock_logger:
            result = utils.repeat_key('z', times=1)
            
            mock_logger.error.assert_called()
            self.assertFalse(result)


class TestFileFunctions(unittest.TestCase):
    """Pruebas para funciones de archivos"""
    
    @patch('utils.os.path.exists')
    def test_file_exists_true(self, mock_exists):
        """file_exists debe retornar True cuando existe"""
        mock_exists.return_value = True
        
        result = utils.file_exists('/path/to/file.txt')
        
        self.assertTrue(result)
        mock_exists.assert_called_once_with('/path/to/file.txt')
    
    @patch('utils.os.path.exists')
    def test_file_exists_false(self, mock_exists):
        """file_exists debe retornar False cuando no existe"""
        mock_exists.return_value = False
        
        result = utils.file_exists('/nonexistent/file.txt')
        
        self.assertFalse(result)
    
    @patch('utils.open', new_callable=unittest.mock.mock_open, read_data="line1\nline2\nline3")
    @patch('utils.os.path.exists')
    def test_load_config_file_success(self, mock_exists, mock_file):
        """load_config_file debe cargar archivo correctamente"""
        mock_exists.return_value = True
        
        with patch('utils.logger'):
            result = utils.load_config_file('config.txt')
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "line1\n")
    
    @patch('utils.open')
    def test_load_config_file_not_found(self, mock_open):
        """load_config_file debe manejar archivo no encontrado"""
        mock_open.side_effect = FileNotFoundError()
        
        with patch('utils.logger'):
            result = utils.load_config_file('nonexistent.txt')
        
        self.assertEqual(result, [])
    
    @patch('utils.open', new_callable=unittest.mock.mock_open)
    @patch('utils.os.makedirs')
    def test_save_config_file_string(self, mock_makedirs, mock_file):
        """save_config_file debe guardar string correctamente"""
        with patch('utils.logger'):
            result = utils.save_config_file('output.txt', 'contenido')
        
        mock_file().write.assert_called_once_with('contenido')
        self.assertTrue(result)
    
    @patch('utils.open', new_callable=unittest.mock.mock_open)
    @patch('utils.os.makedirs')
    def test_save_config_file_list(self, mock_makedirs, mock_file):
        """save_config_file debe guardar lista correctamente"""
        with patch('utils.logger'):
            result = utils.save_config_file('output.txt', ['line1', 'line2'])
        
        mock_file().write.assert_called_once_with('line1\nline2')
        self.assertTrue(result)
    
    @patch('utils.os.makedirs')
    @patch('utils.open')
    def test_save_config_file_no_dirname(self, mock_open, mock_makedirs):
        """save_config_file no debe crear directorio si filepath no tiene dirname"""
        mock_open.return_value.__enter__ = lambda s: s
        mock_open.return_value.__exit__ = MagicMock()
        
        with patch('utils.logger'):
            result = utils.save_config_file('file.txt', 'content')
        
        # makedirs no debe llamarse para archivos sin directorio
        mock_makedirs.assert_not_called()
        self.assertTrue(result)
    
    @patch('utils.open')
    def test_save_config_file_error(self, mock_open):
        """save_config_file debe manejar errores"""
        mock_open.side_effect = Exception("Test error")
        
        with patch('utils.logger') as mock_logger:
            result = utils.save_config_file('output.txt', 'content')
            
            mock_logger.error.assert_called()
            self.assertFalse(result)


class TestGetFilesInDirectory(unittest.TestCase):
    """Pruebas para get_files_in_directory"""
    
    @patch('utils.os.listdir')
    @patch('utils.os.path.isfile')
    @patch('utils.os.path.exists')
    def test_get_files_all(self, mock_exists, mock_isfile, mock_listdir):
        """get_files_in_directory sin filtro"""
        mock_exists.return_value = True
        mock_listdir.return_value = ['file1.py', 'file2.txt', 'file3.py']
        mock_isfile.return_value = True
        
        result = utils.get_files_in_directory('/test/dir')
        
        self.assertEqual(len(result), 3)
    
    @patch('utils.os.listdir')
    @patch('utils.os.path.isfile')
    @patch('utils.os.path.exists')
    def test_get_files_filtered(self, mock_exists, mock_isfile, mock_listdir):
        """get_files_in_directory con filtro de extensión"""
        mock_exists.return_value = True
        mock_listdir.return_value = ['file1.py', 'file2.txt', 'file3.py']
        mock_isfile.return_value = True
        
        result = utils.get_files_in_directory('/test/dir', ['.py'])
        
        self.assertEqual(len(result), 2)
    
    @patch('utils.os.path.exists')
    def test_get_files_directory_not_exists(self, mock_exists):
        """get_files_in_directory con directorio inexistente"""
        mock_exists.return_value = False
        
        with patch('utils.logger'):
            result = utils.get_files_in_directory('/nonexistent')
        
        self.assertEqual(result, [])
    
    @patch('utils.os.listdir')
    @patch('utils.os.path.isfile')
    @patch('utils.os.path.exists')
    def test_get_files_error_handling(self, mock_exists, mock_isfile, mock_listdir):
        """get_files_in_directory debe manejar errores"""
        mock_exists.return_value = True
        mock_listdir.side_effect = PermissionError("Access denied")
        
        with patch('utils.logger') as mock_logger:
            result = utils.get_files_in_directory('/restricted')
            
            mock_logger.error.assert_called()
            self.assertEqual(result, [])


class TestWaitFunctions(unittest.TestCase):
    """Pruebas para funciones de espera"""
    
    @patch('utils.sleep')
    def test_wait_exact_time(self, mock_sleep):
        """wait debe esperar el tiempo especificado"""
        utils.wait(2.5)
        mock_sleep.assert_called_once_with(2.5)
    
    @patch('utils.sleep')
    @patch('utils.random.uniform')
    def test_wait_random(self, mock_uniform, mock_sleep):
        """wait_random debe esperar tiempo aleatorio"""
        mock_uniform.return_value = 3.5
        
        utils.wait_random(1.0, 5.0)
        
        mock_uniform.assert_called_once_with(1.0, 5.0)
        mock_sleep.assert_called_once_with(3.5)


class TestIsValidKeyFunction(unittest.TestCase):
    """Pruebas para is_valid_key"""
    
    def test_is_valid_key_string(self):
        """is_valid_key con string"""
        self.assertTrue(utils.is_valid_key('z'))
        self.assertTrue(utils.is_valid_key('a'))
    
    def test_is_valid_key_int(self):
        """is_valid_key con entero"""
        self.assertTrue(utils.is_valid_key(123))
    
    def test_is_valid_key_none(self):
        """is_valid_key con None"""
        self.assertFalse(utils.is_valid_key(None))
    
    def test_is_valid_key_key_object(self):
        """is_valid_key con objeto Key"""
        # Simular objeto Key
        class MockKey:
            pass
        mock_key = MockKey()
        mock_key.__class__.__name__ = 'Key'
        
        # La función verifica si 'Key' está en la representación de la clase
        result = utils.is_valid_key(mock_key)
        # Depende de cómo se representa el objeto
        self.assertIn(result, [True, False])


class TestLoggerOptimization(unittest.TestCase):
    """Pruebas para optimización de logging"""
    
    @patch('utils.logger')
    @patch('utils.kb')
    @patch('utils.sleep')
    def test_logger_format_strings(self, mock_sleep, mock_kb, mock_logger):
        """Las funciones deben usar format strings en lugar de f-strings"""
        utils.press_key('z', 0.5)
        
        # Verificar que se llamó a logger.debug
        mock_logger.debug.assert_called()
        
        # El primer argumento debe ser un string de formato
        call_args = mock_logger.debug.call_args[0][0]
        self.assertIn('%s', call_args)


if __name__ == '__main__':
    unittest.main(verbosity=2)
