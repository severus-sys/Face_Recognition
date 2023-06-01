import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

#(img.shape[1]//2, img.shape[0]//2) ifadesi 
# görüntünün genişlik ve yükseklik boyutlarının yarısını alır (merkezini)
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('mask',mask)


#cv.bitwise_and() işlevi iki giriş görüntüsü ve 
# bir maske arasında ve mantıksal işlemi uygular.


#-------------
#Her iki giriş görüntüsündeki piksel değerleri ve maske değerleri arasında karşılaştırma yapılır.

#Eğer maske değeri 0 ise, çıktı görüntüsünde piksel değeri 0 olur.

#Eğer maske değeri 0 değilse çıktı görüntüsünde piksel değeri 
# ilgili giriş görüntüsündeki piksel değeriyle aynı olur.

#3.parametre için
#İlk parametre (src1): İşlemin ilk giriş görüntüsünü belirtir.
#İkinci parametre (src2): İşlemin ikinci giriş görüntüsünü belirtir.
#mask parametresi: Maske görüntüsünü belirtir. Bu maske, her pikselin 0 veya 255 değerine sahip olduğu bir siyah-beyaz görüntüdür.

masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow('masked image',masked)

#---------------------

#Görüntüyü kaydırarak maskeyi koyalım 

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

rotated_image = translate(img,100,0)
cv.imshow('rotated_image',rotated_image)

masked = cv.bitwise_and(rotated_image,rotated_image,mask = mask)
cv.imshow('masked_rotated',masked)
cv.waitKey(0)