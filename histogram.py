import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

mask = cv.circle(blank,(img.shape[1]//2 , img.shape[0]//2),100,255,-1)
cv.imshow('mask',mask)

#Her bir piksel değeri, belirli bir aralığa düşer ve bu aralıklar "bins" olarak adlandırılır.
#piksel değerlerinin (0-255 aralığında) olur

masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('masked',masked)

cv.waitKey(0)
gray_hist = cv.calcHist([masked],[0],masked,[256],[0,256])
plt.figure()
plt.title('GrayScale')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

