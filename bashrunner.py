# import sys
# print(sys.argv)
from argparse import ArgumentParser # Libreria para tomar argumentos desde la consola para parsear datos por el script

def parseArguments():
    parser = ArgumentParser()
    parser.add_argument('-s', '--saludar', dest='to_', help = 'Imprime un saludo')
    return parser.parse_args()

argu = parseArguments()
print("esto es un saludo", argu.to_)
