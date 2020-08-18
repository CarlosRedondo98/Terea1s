#Carlos Redondo Hurtado
#carlos.redondo@javeriana.edu.co
#Tarea 1

# importar clases
from colorImage import *

# Main

if __name__ == "__main__":

    rutaImagen = input("Ingrese la ruta de la imagen: ")      # link de la imagen por consola
    imagen = colorImage(rutaImagen)                           # ejecución del constructor de la clase ColorImage
    imagen.displayProperties()                                # ejecución de displayProperties
    imagen.makeGray()                                         # ejecución de makeGray
    canalColor = input("Ingrese el canal de color deseado ( red, green , blue): ")  # color deseado
    imagen.colorizeRGB(canalColor)                            # ejecución de colorizeRGB
    imagen.makeHue()                                          # ejecución de makeHue
