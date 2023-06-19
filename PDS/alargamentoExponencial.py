import cv2
import numpy as np

# Carrega a imagem em escala de cinza
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Calcula o alargamento de contraste exponencial
c = 255 / (1 - np.exp(-np.max(img)))
exp_image = c * (1 - np.exp(-img))

# Converte os valores de pixel para o intervalo [0, 255]
exp_image = np.uint8(exp_image)

# Mostra a imagem original e a imagem com alargamento de contraste exponencial
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Alargamento de Contraste Exponencial', exp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
