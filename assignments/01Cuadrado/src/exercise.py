import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system('clear')
    lado = float(input("Ingrese el valor del lado del cuadrado: "))
    

    perimetro = 4 * lado
    area1 = lado * lado
    area2 = lado ** 2
    area3 = math.pow(lado,2)

    print(f"El perimetro del cuadrado es: {perimetro}")
    print(f"El area del cuadrado con forma 1 es: {area1}")
    print(f"El area del cuadrado con forma 2 es: {area2}")
    print(f"El area del cuadrado con forma 3 es: {area3}")
    
if __name__=='__main__':
    main()
