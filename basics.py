import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park',img)

#grayscale --> gri ton 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade --> kara kalem , kenarları tespit etmek için
#  2.paremetre kenar tespiti için alt eşik 
# 3.parametre kenar tespiti için üst eşik
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edge',canny)


#dilating 
# görüntüdeki beyaz bölümleri genişleterek kenarları daha belirgin hale getirir 

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)


#Eroding
# görüntüdeki beyaz bölümleri küçültür ve
#  siyah bölümleri genişterek küçük nesneleri veya gürültüyü kaldırır.
eroded = cv.erode(dilated , (7,7) ,iterations=3)
cv.imshow('Eroded', eroded)


#Resize

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Cropping kırpma
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)