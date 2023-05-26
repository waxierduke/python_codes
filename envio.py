import cv2
image = cv2.imread("1.jpg",0)
import serial
import keyboard  # Módulo para detectar la tecla presionada
ser = serial.Serial(port='COM6', baudrate=9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS)
count = 0
"""
##print(image[0])
##cv2.imshow("image",image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
"""
"""
# Crear y abrir el archivo de texto para escritura
with open("output.txt", "w") as file:
    # Recorrer la matriz de la imagen
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            # Obtener el valor del píxel
            pixel_value = image[row, col]

            # Imprimir el valor en la consola
            print(pixel_value)

            # Escribir el valor en el archivo de texto, seguido de un salto de línea
            file.write(str(pixel_value) + "\n")
"""
while not keyboard.is_pressed('esc'):
    if keyboard.is_pressed('g'):
    # Recorrer la matriz de la imagen
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
            # Obtener el valor del píxel
                pixel_value = image[row, col]
                numero_binario = bin(pixel_value)[2:]
                bytes_a_enviar = int(numero_binario, 2).to_bytes((len(numero_binario) + 7) // 8, byteorder='big')
                ser.write(bytes_a_enviar)
                count = count + 1
            # Imprimir el valor en la consola
                print("va por:", count)
                print(pixel_value)
                