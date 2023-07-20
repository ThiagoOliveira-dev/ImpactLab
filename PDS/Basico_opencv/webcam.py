import cv2

# Se conecta a webcam do computador
webcam = cv2.VideoCapture(0)
print(webcam.isOpened()) # retorna True se tem a conexão com a webcam do computador

if webcam.isOpened:
    validaçao, frame = webcam.read() # Retorna a tupla (True ou false, Array), o primeiro parametro é em relação se conseguiu 
                                     # ler o frame da webcam, o segundo paramentro é uma matriz relacionada ao frame do video.
    while validaçao:
        cv2.imshow("Video",frame)
        key = cv2.waitKey(1) # espera 1 ms para cada frame e retorna a tecla pressionada do teclado
        if key == 32: # 32 - tecla do espaço
            break
        validaçao, frame = webcam.read()
   # cv2.imwrite("PDS/Basico_opencv/ultimo frame.png",frame) # salva o ultimo frame em um arquivo
    
webcam.release() # desconecta a webcam
cv2.destroyAllWindows() # fecha todas as janelas, se houver