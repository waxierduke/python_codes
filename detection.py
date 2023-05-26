import cv2
import os

folder_path = "C:/Users/aulasingenieria/Desktop/Base de datos/train/no_yawn/"  # Ruta de la carpeta con las imágenes
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

total_images = 0
total_detected_faces = 0
total_detected_eyes = 0

# Iterar sobre los archivos en la carpeta
for filename in os.listdir(folder_path):
    # Comprobar si el archivo es una imagen
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(folder_path, filename)

        # Cargar la imagen
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Aplicar la detección de rostros
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Obtener el número de rostros detectados en la imagen actual
        num_faces = len(faces)
        total_detected_faces += num_faces

        # Dibujar un rectángulo alrededor de cada rostro detectado y detectar ojos en cada rostro
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Obtener la región de interés (ROI) correspondiente al rostro
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]

            # Aplicar la detección de ojos en la ROI del rostro
            eyes = eye_cascade.detectMultiScale(roi_gray)

            # Obtener el número de ojos detectados en el rostro actual
            num_eyes = len(eyes)
            total_detected_eyes += num_eyes

            # Dibujar un rectángulo alrededor de cada ojo detectado
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        # Mostrar la imagen con los rostros y los ojos detectados
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        total_images += 1

# Calcular el porcentaje de detección en todas las imágenes procesadas
total_possible_faces = total_images  # Cada imagen debería tener solo un rostro esperado
total_possible_eyes = total_images  # Cada imagen debería tener solo dos ojos esperados
detection_percentage_faces = (total_detected_faces / total_possible_faces) * 100
detection_percentage_eyes = (total_detected_eyes / (total_possible_eyes * 2)) * 100

print("Porcentaje de detección de rostros en las imágenes: {:.2f}%".format(detection_percentage_faces



