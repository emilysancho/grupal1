from cgi import print_arguments
import cv2 

imagen = cv2.imread('imagen2.jpg',0)

""" 
#Codigo para mostrar la imagen leida
cv2.namedWindow('ressult')
cv2.imshow('ressult', imagen)
key = cv2.waitKey()
"""

imgLW = imagen.shape
print(imagen.shape)

sizeX = imgLW[0]
sizeY = imgLW[1]

segmentX = sizeX / 4
segmentY = sizeY / 4
 
pixeles = []
pixeles1 = []; pixeles2 = []; pixeles3 = []; pixeles4 = []; pixeles5 = []; pixeles6 = []; pixeles7 = []; pixeles8 = []
pixeles9 = []; pixeles10 = []; pixeles11 = []; pixeles12 = []; pixeles13 = []; pixeles14 = []; pixeles15 = []; pixeles16 = []

posX = 0; posY = 0

while posY < sizeY:
    while posX < sizeX:
        #Le da formato al valor decimal leido del pixel, convirtiéndolo en un hexadecimal de 2 bits
        pixeles.append(format(imagen[posY,posX],'02x')+"\n")
        #pixeles.append('{:08b}'.format(imagen[posX,posY])+"\n")
        posX += 1
    posY += 1
    posX = 0

posRow = 0
while posRow < sizeY:
    if posRow < segmentY:
        index1a = int(posRow*sizeX); index1b = int(segmentX+posRow*sizeX)
        index2a = int(segmentX+posRow*sizeX); index2b = int(2*segmentX+posRow*sizeX)
        index3a = int(2*segmentX+posRow*sizeX); index3b = int(3*segmentX+posRow*sizeX)
        index4a = int(3*segmentX+posRow*sizeX); index4b = int(4*segmentX+posRow*sizeX)
        pixeles1 += pixeles[index1a:index1b]
        pixeles2 += pixeles[index2a:index2b]
        pixeles3 += pixeles[index3a:index3b]
        pixeles4 += pixeles[index4a:index4b]
    elif posRow < 2*segmentY:
        index1a = int(posRow*sizeX); index1b = int(segmentX+posRow*sizeX)
        index2a = int(segmentX+posRow*sizeX); index2b = int(2*segmentX+posRow*sizeX)
        index3a = int(2*segmentX+posRow*sizeX); index3b = int(3*segmentX+posRow*sizeX)
        index4a = int(3*segmentX+posRow*sizeX); index4b = int(4*segmentX+posRow*sizeX)
        pixeles5 += pixeles[index1a:index1b]
        pixeles6 += pixeles[index2a:index2b]
        pixeles7 += pixeles[index3a:index3b]
        pixeles8 += pixeles[index4a:index4b]
    elif posRow < 3*segmentY:
        index1a = int(posRow*sizeX); index1b = int(segmentX+posRow*sizeX)
        index2a = int(segmentX+posRow*sizeX); index2b = int(2*segmentX+posRow*sizeX)
        index3a = int(2*segmentX+posRow*sizeX); index3b = int(3*segmentX+posRow*sizeX)
        index4a = int(3*segmentX+posRow*sizeX); index4b = int(4*segmentX+posRow*sizeX)
        pixeles9 += pixeles[index1a:index1b]
        pixeles10 += pixeles[index2a:index2b]
        pixeles11 += pixeles[index3a:index3b]
        pixeles12 += pixeles[index4a:index4b]
    elif posRow < 4*segmentY:
        index1a = int(posRow*sizeX); index1b = int(segmentX+posRow*sizeX)
        index2a = int(segmentX+posRow*sizeX); index2b = int(2*segmentX+posRow*sizeX)
        index3a = int(2*segmentX+posRow*sizeX); index3b = int(3*segmentX+posRow*sizeX)
        index4a = int(3*segmentX+posRow*sizeX); index4b = int(4*segmentX+posRow*sizeX)
        pixeles13 += pixeles[index1a:index1b]
        pixeles14 += pixeles[index2a:index2b]
        pixeles15 += pixeles[index3a:index3b]
        pixeles16 += pixeles[index4a:index4b]
    posRow+=1

        
#Genera un archivo con el hexadecimal de todos los pixeles de la imagen
f = open("./outHexa.txt", "w")
f.writelines(pixeles)

#Genera los 16 archivos para cada segmento de imagem en codigo hexadecimal
f1 = open("./segmento1.txt", "w")
f1.writelines(pixeles1)

f2 = open("./segmento2.txt", "w")
f2.writelines(pixeles2)

f3 = open("./segmento3.txt", "w")
f3.writelines(pixeles3)

f4 = open("./segmento4.txt", "w")
f4.writelines(pixeles4)

f5 = open("./segmento5.txt", "w")
f5.writelines(pixeles5)

f6 = open("./segmento6.txt", "w")
f6.writelines(pixeles6)

f7 = open("./segmento7.txt", "w")
f7.writelines(pixeles7)

f8 = open("./segmento8.txt", "w")
f8.writelines(pixeles8)

f9 = open("./segmento9.txt", "w")
f9.writelines(pixeles9)

f10 = open("./segmento10.txt", "w")
f10.writelines(pixeles10)

f11 = open("./segmento11.txt", "w")
f11.writelines(pixeles11)

f12 = open("./segmento12.txt", "w")
f12.writelines(pixeles12)

f13 = open("./segmento13.txt", "w")
f13.writelines(pixeles13)

f14 = open("./segmento14.txt", "w")
f14.writelines(pixeles14)

f15 = open("./segmento15.txt", "w")
f15.writelines(pixeles15)

f16 = open("./segmento16.txt", "w")
f16.writelines(pixeles16)
