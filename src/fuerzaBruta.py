
import argparse
import os.path

from ataque import AtaqueFuerzaBruta
from config import ALFABETO

def archivoValido(parser, arg):
    if not os.path.exists(arg):
        parser.error("El archivo %s no existe" % arg)
    else:
        return arg

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--comprimido", required=True,
                        help="Archivo comprimido de entrada", type=lambda x: archivoValido(parser, x))
    parser.add_argument("-l", "--longitud", help="Longitud máxima de clave", type=int, default=5)
    parser.add_argument("-d", "--destino", help="Directorio del archivo extraído", default=".")

    args = parser.parse_args()

    fuerzaBruta = AtaqueFuerzaBruta(args.comprimido, args.destino, ALFABETO["español"])
    fuerzaBruta.atacar(args.longitud)

if __name__ == "__main__":
    main()
