import cv2

# Carrega a imagem em escala de cinza
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Calcula o histograma da imagem
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Normaliza o histograma
hist_norm = cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

# Aplica a equalização de contraste por histograma
equalized_image = cv2.equalizeHist(img)

# Mostra a imagem original e a imagem com equalização de contraste por histograma
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Equalização de Contraste por Histograma', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
