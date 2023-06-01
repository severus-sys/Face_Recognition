import numpy as np
import cv2 as cv



#Haar sınıflandırıcısı kullanarak yüz tespiti yapmak için bir CascadeClassifier nesnesi oluşturuluyor. 
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# İnsanların isimlerini içeren bir liste oluşturuluyor. Bu liste, yüz tanıma sonuçlarında etiketleri (labels) temsil eder.
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

#features.npy dosyasından özellik vektörlerini (features) yükler. allow_pickle=True parametresi pickle formatını desteklemek için gereklidir.
features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy',allow_pickle=True)

#Yüz tanıma algoritması için bir LBPH tanıyıcı oluşturuluyor
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#Daha önce eğitilmiş olan yüz tanıma modelini face_trained.yml dosyasından okur.
face_recognizer.read('face_trained.yml')

#test edilecek görüntü
img = cv.imread(r'C:\Users\severus\Desktop\FaceRecognition\Faces\val\madonna\1.jpg')
#gri görüntü
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.resize(gray,(gray.shape[1]*2,gray.shape[0]*2))
img = cv.resize(img,(gray.shape[1],gray.shape[0]))

cv.imshow('Person',gray)

#Detect the face in the image
#gri tonlamalı görüntüdeki yüzleri tespit eder.
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 4)
#: Tespit edilen yüz bölgelerini döngüyle gezinir.
for (x,y,w,h) in face_rect:
    #yüz bölgesini keser ve face_roi değişkenine atar.
    face_roi = gray[y:y+h,x:x+h]
    label, confidence = face_recognizer.predict(face_roi)
    print(f'label = {label} with a confidence of {confidence}') #güvvenlik skoru 
    
    cv.putText(img,str(people[label]),(20,30),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.putText(img,'{:.3f}'.format(confidence),(x,y-10),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)


cv.imshow('Detected Face',img)

cv.waitKey(0)