import os
import cv2 as cv
import numpy as np
import random

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']


#eğitmek için gereken resimlerin ana dizini
DIR = r'C:\Users\severus\Desktop\FaceRecognition\Faces\train'

#Yüz Algılama Sınıflayıcısının Yüklenmesi
haar_cascade = cv.CascadeClassifier('haar_face.xml')


#features listesi, yüz görüntülerinin özelliklerini içerir.
#  Her bir yüz görüntüsü, yüz algılama ile tespit edilen 
# yüz bölgesinden çıkarılan özellikler olarak temsil edilir. 
features = []


#labels listesi her bir yüz görüntüsünün etiketlerini içerir
# Etiketler, people listesindeki kişilerin indekslerine karşılık gelen sayılardır.
labels = []

def create_train():
    for person in people:
        #belirtilen dizin yolunu ve person değişkeniyle belirtilen kişi adını birleştirerek
        #tam bir dosya yolunu oluşturur.
        #os.path.join() fonksiyonu, platforma bağlı olarak doğru şekilde dosya yolununu oluşturur

        #mesala bu böyle olucak C:\Users\severus\Desktop\FaceRecognition\Faces\train\Ben Afflek'
        path = os.path.join(DIR,person)
        
        #people listesinde person değişkeninin değerine karşılık gelen indeksi döndürür.
        #Ben Afflek in indexi 0 mesala
        label = people.index(person)
        
        #mesala C:\Users\severus\Desktop\FaceRecognition\Faces\train\Ben Afflek dizinin içindekinleri resimleri döndürecek
        for img in os.listdir(path=path):
            
            #birleştirerek C:\Users\severus\Desktop\FaceRecognition\Faces\train\Ben Afflek\1.jpg yapıyor mesala
            img_path = os.path.join(path,img)

            # bu da resimlerimiz
            img_array = cv.imread(img_path)
            #resmi griye çekiyoruz
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            cv.imshow('photos',gray)
            #daha görsel şölen olsun diye böyle yaptım 
            x_position = random.randint(0, 1800)  # X koordinatı
            y_position = random.randint(0, 750)  # Y koordinatı
            cv.moveWindow('photos', x_position, y_position)
            cv.waitKey(10) # 10 salise bekle

            
            
            #scaleFactor: Yüz tespiti için görüntünün ölçeklendirme faktörü. 
            #Bu parametre, görüntünün her ölçeğinde yüzlerin boyutunu ne kadar azaltılacağını belirler. 
            #Örneğin, scaleFactor=1.1 ise her ölçekte görüntünün boyutu %10 azaltılır.
            #scaleFactor ne kadar artarsa  yanlış tespit yapar
            #ne kadar azalırsa da yüzleri tespi etmek için daha büyük tespit yapar ama küçük yüzleri ve uzak yüzleri tanımaz

            #minNeighbors: Her bir tespit edilen yüz için minimum komşu sayısı. 
            # Bu parametre, yüzlerin etrafındaki bölgeyi kontrol ederek yanlış pozitif 
            # tespitleri azaltmaya yardımcı olur. Daha yüksek bir minNeighbors değeri
            # daha az yanlış pozitif tespitlere ve daha az duyarlılık sağlar.
            #daha az olursa da yüzleri kaçırır.
            #2 ucu boklu değnek


            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors =5) #yüzleri tespit etmek için
            
            #Bu kısım yüz tespiti sonucunda tespit edilen yüz bölgelerini kesip özellik olarak kullanmak 
            # için features listesine ekler ve her bir tespit edilen yüz bölgesi için etiketi  labels listesine ekler.
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
          



create_train()
print('Traning done ----')

#Bu dönüşümler, daha sonra yüz tanıma algoritmasını eğitmek için kullanılan veri setinin numpy dizilerine dönüştürülmesini sağlar

#np.array(features, dtype='object') ifadesi features listesini numpy dizisine dönüştürür. 
# dtype='object' parametresi, dizinin veri tipini "object" olarak belirtir. 
# Bu, her bir öğenin farklı veri tiplerine sahip olabileceği anlamına gelir.
features= np.array(features,dtype='object')
#Aynı şekilde, np.array(labels) ifadesi labels listesini numpy dizisine dönüştürür.
# Burada veri tipi belirtilmediği için numpy otomatik olarak uygun veri tipini seçer.

labels = np.array(labels)



print(f'Length of the features   : {len(features)}')
print(f'Length of the Labels   : {len(labels)}')


#Yüz tanıma algoritması
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#train on recognizer on the featuers list and the labels lits
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)