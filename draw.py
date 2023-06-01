import cv2 as cv
import numpy as np

# belirtilen boyutda 0 dizisi oluşruyor, 3 de Rgb görüntü için
blank = np.zeros((500,500,3),dtype="uint8")
cv.imshow('Blank',blank)

#renk ekleyelim
#blank[:] = tamamı demek ,  rgb kod 0,255,0 vs
#blank[:] = 0,255,0
# blank[200:300,300:400] = 0,300,0
# cv.imshow('Green',blank)

#dikdörtgen

#  -1 içini dolduruyorr
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
#(0,0) sol üst kose koordinat
#(250,500) yada (blank.shape[1]//2,blank.shape[0]//2) sağ alt koordinatıdır dikdörtgenin
#blank.shape boyutu temsil eder
#blank.shape[1] yatay boyut
#blank.shape[0] dikey boyut
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectange',blank)

#çember

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow("Circle",blank)

#çizgi
#(100,250) yani 2.parametre başlangıç koordinatı
#(300,400) yani 3.parametre bitiş koordinatı
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#metin
#3.parametre (0,255) metnin sol alt köşesi koordinatı
cv.putText(blank,'Hello it is text',(100,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(250,30,40),thickness=1)
cv.imshow('Text',blank)

cv.waitKey(0)
