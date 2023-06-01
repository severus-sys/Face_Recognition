import cv2 as cv
import numpy as np

#aynı boyutlarda bir siyah görüntü
blank = np.zeros((400,400),dtype='uint8')

#blank.copy() ifadesi, blank adlı bir görüntünün bir kopyasını oluşturur
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise lar 0 ve 1 verir 
 
#bitwise and -- intersecting regions
#2sinin ortak olarak doldurduğu yeri alıyor 
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

#bitwise or --- non intersecting and intercesting regions
#2sinin ayrı ayrı doldurduğu yeri gösteriyor birleştiriyor yani
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise or',bitwise_or)

#bitwise xor -- non intersecting regions
#yani aynı piksel(koordinat) de olurlarsa 0 yani siyah 
# farklı piksel yani koordinatda olurlarsa 1 yani beyaz
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor',bitwise_xor)


#bitwise not
#obje hariç her şeyi 1 ' e yani beyaza
bitwise_not = cv.bitwise_not(circle)
cv.imshow('circle',bitwise_not)
 

cv.waitKey(0)