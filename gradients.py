import cv2 as cv
import numpy as np

img = cv.imread('Photos/Park.jpg')
cv.imshow('Park',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Laplaction // kenar tespiti için 
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel x ',sobelx)
cv.imshow('Sobel y ' ,sobely)
cv.imshow('Combined Solbel' ,combined_sobel)
cv.waitKey(0)