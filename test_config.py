import os
import unittest
from unittest.mock import patch

from config import CONFIG, cargar_config


class TestConfig(unittest.TestCase):
    def test_ambiente_por_defecto(self):
        with patch.dict(os.environ):
            os.environ.pop("APP_ENV", None)
            self.assertEqual(cargar_config()[0], "desarrollo")

    def test_ambiente_desconocido(self):
        with patch.dict(os.environ, {"APP_ENV": "desconocido"}):
            with self.assertRaises(ValueError):
                cargar_config()

    def test_bases_de_datos_indepednientes(self):
        bases = [c["base_datos"] for c in CONFIG.values()]
        self.assertEqual(len(bases), len(set(bases)))

    def test_produccion_sin_depuracion(self):
        self.assertIs(CONFIG["produccion"]["depuracion"], False)