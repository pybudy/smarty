import cv2
img1 = cv2.imread("C://Users//Mnn//Desktop//ak.jpg",1)
#cas_f = cv2.CascadeClassifier("C://Users//Mnn//Desktop//face_extended.xml")
cas_f = cv2.CascadeClassifier("C://Users//Mnn//Desktop//face.xml")

gryimg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces = cas_f.detectMultiScale(gryimg,scaleFactor=1.008,minNeighbors=5)
for x,y,w,h in faces:
    #if x == 276:
     #   break
    img1=cv2.rectangle(img1,(x-70,y-70),(x+w+50,y+h+50),(0,255,0),2)

#print(img1)
print(type(gryimg))
print(type(faces))
print(faces)
print(gryimg.shape)
cv2.imshow("GRAY",img1)
cv2.waitKey(10000)
cv2.destroyAllWindows()