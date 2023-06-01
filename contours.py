import cv2 as cv
import numpy as np 


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

#aynı boyutlarda bir siyah görüntü
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

#griye çalma
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5) ,cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edge',canny)

#gri tonlamalı bir görüntü üzerinde eşikleme işlemi yapar
# Eşikleme işlemi her pikselin eşik değeriyle karşılaştırıldığı bir işlemdir
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY) 
#125 eşik değeri olarak belirlenmiştir yani piksel değeri 125'in üzerindeyse beyaz (255)
# altında veya eşitse siyah (0) olacak şekilde bir eşikleme yapılacak
cv.imshow('Thresh', thresh)



#Kontur, bir nesnenin sınırlarını belirleyen bir eğri veya çizgidir
#Konturlar, birbirleriyle ilişkili olabilirler. 
# Örneğin, bir nesnenin içinde başka bir nesne olabilir. 
# Bu durumda, içteki nesne, dıştaki nesneye bağlı olarak bir alt kontur olarak kabul edilir.
#  hierarchies değeri, bu tür ilişkileri belirtir
contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#cv.RETR_LIST -->  tüm konturların listesini döndürür.
#CHAIN_APPROX_NONE ---> konturun tüm noktalarını saklar.

print(f'{len(contours)} found')

#blankın üstünde contours
#-1 Konturların tamamını çizmek için kullanılan parametre.
#4.parametre kalınlık
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn Black' , blank)

cv.waitKey(0)