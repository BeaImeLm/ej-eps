import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system('clear')

    """radio = float(input("Ingrese el valor del radio de la esfera: "))
    volumen = 4 / 3 * math.pi * radio ** 3
    print(f"El volumen de la esfera con radio {radio} es: {volumen} unidades cúbicas")"""

    radio = float(input("Ingrese el valor del radio de la esfera: "))

    volumen = 4 / 3 * math.pi * math.pow(radio,3)
    area = 4 * math.pi * math.pow(radio,2)

    print(f"El volumen de la esfera con radio {radio} es: {volumen} unidades cúbicas")
    print(f"El área de la esfera con radio {radio} es: {area} unidades cuadradas")



if __name__=='__main__':
    main()
