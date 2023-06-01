import cv2 as cv
#Resizing and Rescaling Frame


#bir kareyi yeniden boyutlandırmak için yazdık fonksiyonu
def rescaleFrame(frame,scale = 0.75):
    #Images , Videos and Live Video

    #frame.shape[1] karenin genişliğini 
    width =int (frame.shape[1] * scale)
    #frame.shape[0] karenin uzunluğunu veriyor.
    height = int(frame.shape[0] * scale)

    #dimension karenin boyutlarını tutan tupple değişkenidir.     
    dimension = (width,height)
    
    #interpolation parametresi olarak cv.INTER_AREA değerini 
    # kullanarak piksel kaybını minimize eder.
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live video
    capture.set(3,width)
    capture.set(4,height)


#reading video or image

img = cv.imread('Photos/cat_large.jpg')
capture = cv.VideoCapture('Videos/dog.mp4')
resized_image = rescaleFrame(img,0.3)

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame=frame,scale= .25)
    cv.imshow("Originial Image",img)
    cv.imshow("Resized Immage",resized_image)
    cv.imshow('Original Video',frame)
    cv.imshow('Video Resized'  , frame_resized)
    if cv.waitKey(50) & 0XFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()




