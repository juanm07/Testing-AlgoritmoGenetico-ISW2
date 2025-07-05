#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode


class TestCgiDecode(unittest.TestCase):
    def test_mas_espacio(self):
        self.assertEqual(cgi_decode("Hola+mundo"),"Hola mundo")
        #self.assertEqual(cgi_decode("oracion+mas+larga+para+probar"), "oracion mas larga para probar")
    
    def test_porcentaje(self):
        self.assertEqual(cgi_decode("hola%2cinge2%2ctesteo+comas"), "hola,inge2,testeo comas")
        self.assertEqual(cgi_decode("%6F%74%72%6F%73+%63%61%72%61%63%74%65%72%65%73"), "otros caracteres")
    
    def test_texto_sin_codificar(self):
        self.assertEqual(cgi_decode("SinNada"),"SinNada")

    def test_invalid_high_digit(self):
        with self.assertRaises(ValueError):
            cgi_decode("primeroInvalido%H2")
    
    def test_invalid_low_digit(self):
        with self.assertRaises(ValueError): 
            cgi_decode("segundoInvalido%2P")