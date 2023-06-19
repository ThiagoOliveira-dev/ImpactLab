import cv2
import numpy as np

img = cv2.imread('lena.jpg',0)

min_val = np.min(img)
max_val = np.max(img)

out = ((img - min_val) / (max_val - min_val)) * 255


cv2.imshow('Imagem',out)

cv2.waitKey(0)
cv2.destroyAllWindows()