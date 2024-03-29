#FaceDetection 1.0
#(C) 2019 Ariel Roque /UFCG

import cv2

webcam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	s,video = webcam.read()
	
	video = cv2.flip(video,180)
	
	faces = face_cascade.detectMultiScale(video,minNeighbors = 20, minSize = (30,30), maxSize = (400,400))
	
	for (x,y,w,h) in faces:
		cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),4)
	
	cv2.imshow("Face Detection", video)
	
	if (cv2.waitKey(1) and 0xFF == ord('q')):
		break

webcam.release()
cv2.destroyAllWindows()
	
