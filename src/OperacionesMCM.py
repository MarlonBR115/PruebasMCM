from src.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCM(self):
        if len(self.__numeros) < 2 :
            raise FaltanParametros
        elif len(self.__numeros) > 1 :
            return self.MCMMasDosNumeros()
        else:
            return 0

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCMMasDosNumeros(self):
        for n in (self.__numeros):
            if not isinstance(n, int):
                raise ValueError

        cantidadNumeros = len(self.__numeros)
        mcd = self.MCD(self.__numeros[0], self.__numeros[1])
        i = 0
        while( i < (cantidadNumeros-2)):
            mcd =  self.MCD(mcd, self.__numeros[i+2])
            i = i+1
        dividendo = self.productoNumeros()
        divisor = mcd
        mcm = dividendo / divisor
        return mcm

    def productoNumeros(self):
        producto = 1
        for n in (self.__numeros):
            if not isinstance(n, int):
                raise ValueError
            producto *= n
        return producto


