
from itertools import product
from time import time

from zip import Zip
from barraProgreso import BarraProgreso

class AtaqueFuerzaBruta(object):

    def __init__(self, rutaArchivo, destino, alfabeto):
        self.__alfabeto = alfabeto
        self.__L = len(self.__alfabeto)

        self.__archivo = Zip(rutaArchivo, destino)
        self.__progreso = BarraProgreso()

    def __coincide(self, clave):
        return self.__archivo.extraer(clave)

    def atacar(self, longitudMaximaClave):

        print("\nAlfabeto:", self.__alfabeto)
        print("Longitud máxima:", longitudMaximaClave,"\n")

        inicio = time()

        for longitudClave in range(1, longitudMaximaClave+1):

            tamaño = self.__L**longitudClave
            n = 1
            for combinacion in product(self.__alfabeto, repeat=longitudClave):

                clave = "".join(combinacion)

                if self.__coincide(clave):
                    print()
                    fin = time()
                    print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")
                    print("Clave:", clave)
                    return clave
                
                self.__progreso.printProgressBar(
                    n,
                    tamaño,
                    prefix = "Longitud "+ str(longitudClave)
                )

                n += 1

        fin = time()
        print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")
        print("Clave no encontrada")
        return ""
