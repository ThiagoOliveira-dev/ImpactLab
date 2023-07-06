import cv2



img = cv2.imread("PDS/lena.jpg",-1)

print("Bem vindo ao Python com OPenCV\n")

cv2.imshow('ImagemTeste',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
