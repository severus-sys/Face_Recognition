import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#img görüntüsünün boyutlarına sahip
#(sadece genişlik ve yükseklik) siyah bir görüntü oluşturur.
blank = np.zeros(img.shape[:2],dtype='uint8')

#BGR kanallarını ayırır
b,g,r = cv.split(img)
                #blue,green,red
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

            #3 renk kanalı
#(427, 640, 3)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


#birleştiriyoruz ve ana resim ortaya çıkıyor
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

cv.waitKey(0)