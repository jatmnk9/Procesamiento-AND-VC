import cv2
import numpy as np

# Procesar imagen

# Carga la imagen
img = cv2.imread('prueba.jpg', cv2.IMREAD_GRAYSCALE)

# Define un umbral para convertir la imagen a blanco y negro
threshold_value = 128
(threshold, img_bw) = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Guarda la imagen en blanco y negro
cv2.imwrite('black_and_white_image.jpg', img_bw)

# Realizar operación AND bit a bit
result = cv2.bitwise_and(img, img_bw)

# Guardar resultado
cv2.imwrite("resultado.jpg", result)

# Mostrar resultado
cv2.imshow("Resultado", result)
cv2.waitKey(0)
cv2.destroyAllWindows()