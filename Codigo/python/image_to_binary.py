import cv2 
  
imagen = cv2.imread('imagen.jpg',0)

#Codigo para mostrar la imagen leida
#cv2.namedWindow('ressult')
#cv2.imshow('ressult', imagen)
#key = cv2.waitKey()

imgLW = imagen.shape
print(imagen.shape)

pixeles = []
posX = 0; posY = 0

while posY < imgLW[1]:
    while posX < imgLW[0]:
        #Le da formato al valor decimal leido del pixel, convirtiéndolo en un binario de 8 bits
        pixeles.append(format(imagen[posX,posY],'08b')+"\n")
        #pixeles.append('{:08b}'.format(imagen[posX,posY])+"\n")
        posX = posX + 1
    posY = posY +1
    posX = 0

#print(pixeles)
f = open("./outBinario.txt", "w")
f.writelines(pixeles)
