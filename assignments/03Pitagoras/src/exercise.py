import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system('clear')

    catetoA = float(input("Ingrese el valor del cateto A de un Triángulo Rectángulo: "))
    catetoB = float(input("Ingrese el valor del cateto B de un Triángulo Rectángulo: "))

    hipotenusa = math.sqrt(math.pow(catetoA,2)+math.pow(catetoB,2))
    

    print(f"El valor de la hipotenusa con cateto A de {catetoA} y cateto B de {catetoB} es: {hipotenusa} unidades ")

if __name__=='__main__':
    main()
