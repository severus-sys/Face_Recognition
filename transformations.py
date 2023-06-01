import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')

cv.imshow('Boston', img)

#translation
def translate(img,x,y):
    # 2x3'lük (2 satır, 3 sütun) bir float32 tipinde matris 
    transMat = np.float32([[1,0,x],[0,1,y]])
    #img.shape[1] görüntünün genişliğini, 
    # img.shape[0] görüntünün yüksekliği
    dimensions = (img.shape[1],img.shape[0])

    #, bir görüntüyü belirtilen bir dönüşüm matrisiyle kaydırır
    #1.parametre kare
    #2.parametre dönüşüm matrisi
    #3.parametre boyut
    return cv.warpAffine(img,transMat,dimensions)


#-x---> left
#-y----> Up
#x ---> right
#y ---> down

translated = translate(img,-100,100)
cv.imshow("Translated",translated)



#Rotation
def rotate(img,angle,rotPoint = None):
    #görüntünün yüksekliği ve genişliği 
    height,width = img.shape[:2]
    #rot point belirlenmesisse görüntünün ortasından alır 
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    # döndürme matrisini hesaplar
    rotMat = cv.getRotationMatrix2D(rotPoint,angle=angle,scale=1.0)
    dimensions = (width,height)

    #döndürülmüş görüntüyü hesaplar ve döndürülmüş görüntüyü döndürür.
    return cv.warpAffine(img,rotMat,dimensions)


rotated = rotate(img,90)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated,-90)
cv.imshow('Rotated double' , rotated_rotated)

#Resizing
resized = cv.resize(img,(500,300),interpolation= cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
flip = cv.flip(img,1)
cv.imshow('Flip',flip)

cv.waitKey(0)