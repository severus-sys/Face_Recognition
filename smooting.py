import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow("Cats",img)

#Averaging
average = cv.blur(img,(7,7))
cv.imshow("Average Blur",average)

#Gaussing Blur

gaus = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussing blur',gaus)

#Median Blur

median = cv.medianBlur(img,7)
cv.imshow('Median Blur',median)

#Bilateral
bilateral = cv.bilateralFilter(img,50,100,75)
cv.imshow('bilateral',bilateral)

#Bütün blurlama fonksiyonlarının farkı sadece matemmatiksel olarak farklı hesaplamalardır.

#Belirli bir bölgeyi blurlayalım

#(x1, y1) sol üst köşe koordinatı 
# (x2, y2) sağ alt köşe koordinatı
x1 ,y1 = 100, 100
x2 , y2 = 300,300

regition_interested = img[y1:y2,x1:x2]

blurred =  cv.GaussianBlur(regition_interested,(25,25),0)

img[y1:y2,x1:x2] = blurred

cv.imshow('Blurred region',img)

cv.waitKey(0)