import cv2
import numpy as np

img = cv2.imread('lena.jpg',0)

min_val = np.min(img[100:200, 100:200])
max_val = np.max(img[100:200, 100:200])

out = ((img - min_val) / (max_val - min_val)) * 255

cv2.imwrite('outputPorParte.jpg', out)

cv2.imshow('Imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()