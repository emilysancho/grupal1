import cv2
import numpy as np
  
imagen = cv2.imread('imagen.jpg')

f = open("outBinario.txt","r")
text = f.readlines()
#print(text)

#Codigo para mostrar la imagen leida
#cv2.namedWindow('ressult')
#cv2.imshow('ressult', imagen)
#key = cv2.waitKey()


imgLW = imagen.shape
col = 0; row = 0
cols = imgLW[0]; rows = imgLW[1]
index = 0

imageMatrix = [[0]*cols]*rows
nArray = np.zeros((rows, cols), np.int32)

print(nArray)

while row < rows:
    while col < cols:
        #imageMatrix[row][col] = int(text[index],2)
        nArray[row][col] = int(text[index],2)
        index = index + 1
        col = col + 1
    row = row +1
    col = 0

print(nArray)
cv2.imwrite('outImagen.jpg',nArray)
 