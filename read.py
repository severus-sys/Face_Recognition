import cv2 as cv

#Reading Image and Videos
#-----------------

# imread görüntüyü okur ve bellekte bir görüntü nesnesi olarak temsil eder.
# img = cv.imread('Photos/cat_large.jpg')


#resmi gösteriyor
# cv.imshow('Cat',img)

#işlevi, bir tuşa basılmasını bekler.
#cv.waitKey(0)

#videoyu bu nesneye atıyoruz
# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     #video , görüntülerden oluşur, burada görüntü kareleri okuyor diyebiliriz, 
#     #görüntüyü frame ' e atıyor , frame numpy dizisi matrix dizisi gibi diyebilriiz
#     #isTrue da kare başarılı şekilde okunmuş mu kontrol ediyor.
#     isTrue,frame = capture.read()
    
#     cv.imshow('Video',frame)
    
#     #cv.waitKey() burada oynatma hızı işlevi görüyor parametresi 
#      ne kadar yüksekse o kadar oynatma hızı düşer
#     #0xFF == ord('d') : d'ye basınca çık
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# #VideoCapture nesnesini serbest bırakır ve video dosyasını kapatır.
# capture.release()


# # tüm açık pencereleri kapatır. Video veya görüntüyü görüntülerken 
# # oluşturduğunuz pencereleri kapatmak için bu fonksiyonu kullanabilirsiniz. 
# cv.destroyAllWindows()



