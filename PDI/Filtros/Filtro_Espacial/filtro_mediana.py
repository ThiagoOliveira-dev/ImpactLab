import cv2
import numpy as np

# Filtro passa-baixa
# Suaviza o ruído

img = cv2.imread("PDI/Filtros/ruido.jpg")


img_out = cv2.medianBlur(img, 5) # Filtro da mediana

cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()