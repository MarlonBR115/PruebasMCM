import unittest
from src.OperacionesMCM import OperacionesEnteros
from src.FaltanParametros import FaltanParametros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCM_dosNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 72
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_tresNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        resultadoEsperado = 2160
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_cuatroNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 25920
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numero1 = 18
        operacion = OperacionesEnteros([numero1])

        # Assert
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCM()

    def test_MCM_unaCadena_lanzaExcepcion(self):
        # Arrange
        numero1 = "18a"
        numero2 = 13
        operacion = OperacionesEnteros([numero1, numero2])

        # Assert
        with self.assertRaises(ValueError):
            operacion.calcularMCM()

# Si se ejecuta este archivo directamente, se correrán las pruebas
if __name__ == '__main__':
    unittest.main()
