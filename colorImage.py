
# imports
import numpy as np
import cv2
import os

class colorImage:

    # Constructor
    def __init__(self, rutaImagen):
        self.imagen1 = cv2.imread(rutaImagen, 1)        # imagen importada
        self.imagen2 = cv2.imread(rutaImagen, 1)        # copoa imagen importada

# Métodos

    # método displayProperties
    def displayProperties(self):
        alto, ancho, canales = self.imagen1.shape          # parametros de la imagen
        print(f"El ancho de la imagen es: {ancho} \nEl alto de la imagen es: {alto}") # imprimir parametros deseados

    # método makeGray
    def makeGray(self):
        self.grises = cv2.cvtColor(self.imagen1, cv2.COLOR_BGR2GRAY)    # BGR a Grises
        cv2.imshow("Version en grises de la imagen", self.grises)       # mostrar versión en grises
        cv2.waitKey(1000)                                               # delay de 1 seundo

    # método colorizeRGB
    def colorizeRGB(self, canalColor):

        # caso rojo
        if canalColor == "red":
            self.imagen1[:, :, 0] = 0                             # eliminar componentes azules
            self.imagen1[:, :, 1] = 0                             # eliminar componentes verdes
            self.imagen1[:, :, 2] = self.grises                   # componentes rojas en la imagen en grises
            cv2.imshow("Imagen colorizada rojiza", self.imagen1)  # imprimir imagen
            cv2.waitKey(1000)                                     # delay de 1 seundo

        # caso verde
        elif canalColor == 'green':
            self.imagen1[:, :, 0] = 0                              # eliminar componentes azules
            self.imagen1[:, :, 2] = 0                              # eliminar componentes rojas
            self.imagen1[:, :, 1] = self.grises                    # componentes verdes en la imagen en grises
            cv2.imshow("Imagen colorizada verdosa", self.imagen1)  # imprimir imagen
            cv2.waitKey(1000)                                      # delay de 1 seundo

        # caso azul
        else:
            self.imagen1[:, :, 1] = 0                               # eliminar componentes verdes
            self.imagen1[:, :, 2] = 0                               # eliminar componentes rojas
            self.imagen1[:, :, 0] = self.grises                     # omponentes azules en la imagen en grises
            cv2.imshow("Imagen colorizada azuloza", self.imagen1)   # imprimir imagen
            cv2.waitKey(1000)                                       # delay de 1 seundo

    # Método makeHue
    def makeHue(self):
        self.hsv = cv2.cvtColor(self.imagen2, cv2.COLOR_BGR2HSV)   # BGR a HSV
        self.hsv[:, :, 1] = 255                                    # componente H constante de 255
        self.hsv[:, :, 2] = 255                                    # componente V constante de 255
        self.hsv = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)       # HSV a BGR
        cv2.imshow("Imagen con tonos Hue resaltados", self.hsv)                                # imprimir HSV convertida
        cv2.waitKey(0)                                             # delay


