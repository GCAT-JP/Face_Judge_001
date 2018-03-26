import cv2

imageNum = 1
for img in range(100):
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(r'C:\Users\Face_Judge_001\Images\Image' +str(imageNum)+'.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imwrite(r'C:\Users\Face_Judge_001\Images_OnlyFace\Image' +str(imageNum) + '.png', img[y:y+h, x:x+w])
    
    imageNum = imageNum + 1
    