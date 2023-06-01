import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple threshing
#150 nin altındaki kalan piksel 0  siyah
#150yi geçen piksekller  255 e ayarlanacak beyaz yani 
thresold ,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple thresold',thresh)

# 150 nin altındaki kalan piksel 255 beyaz
#150yi geçen piksekller  0 e ayarlanacak siyah yani 
thresold ,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple thresold inv',thresh_inv)



#Adaptive Thresholding
#255: Maksimum değer olarak atanacak yoğunluk değeri. Eşik değerini geçen pikseller bu değeri alır
#cv.ADAPTIVE_THRESH_MEAN_C: Adaptif eşik değerleme yöntemi. 
# Pikselin etrafındaki bölgenin ortalaması kullanılarak adaptif eşik değeri hesaplanır.
#cv.THRESH_BINARY: Eşik değerini geçen piksellerin atanacağı değer. Bu durumda, 
# eşik değerini geçen pikseller 255 olarak ayarlanır.
#11: Blok boyutu parametresi. Bu adaptif eşik değerinin hesaplanması 
# için kullanılan piksellerin etrafındaki bölgenin boyutunu belirtir 11x11
#3: C parametresi. Hesaplama yapılan bölgenin ortalama değerinden çıkarılacak
#sabit bir değeri ifade eder.

#Eğer bu ortalamaya göre piksel değeri 255'ten küçükse, 
# o piksel değeri 0 olarak atanır (siyah renk).
#  Eğer ortalamaya göre piksel değeri 255'ten büyük veya eşitse, 
# o piksel değeri 255 olarak atanır (beyaz renk).
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) 
cv.imshow('Adaptive thresh',adaptive_thresh)

cv.waitKey(0)
