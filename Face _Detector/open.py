# copy this folder on the desktop and then in the command prompt type 'cd Desktop'(for Linux)/'cd desktop' (for windows), 
# then type 'cd Face_Detector' and then finally type 'python open.py' to view the face detector for Elon Musk


import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("index.jpeg")
 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,
                                      minNeighbors=5)


print(faces)


for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Gray",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
