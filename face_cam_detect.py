# import numpy as np
import cv2

###------- Initializing data --------###
face_cascade = cv2.CascadeClassifier(
	'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('capture.avi', fourcc, 20.0, (640, 480))

""" 
	Loop to keep recording video
	from the default webcam
"""
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret:
		# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAYSCALE)
		
		""" 
			The detectMultiScale function detects objects - 
			in this case, it will use the face cascade
			to detect a face (or what it thinks is a face)
		"""
		faces = face_cascade.detectMultiScale(frame, 1.3, 5) 
		""" 
			The second argument, the 'scaleFactor'
			compensates for distance and size of faces. 
		
			The third argument, 'miniNeighbors' defines the number
			of objects near the current one before it deciding
			that it found an object 
		"""

		"""
			cv2.rectangle draws a rectangle around
			faces - which returns dimensions of a rectangle.
			fx and fy -> location of rectangle
			fw and fh -> width and height of rectangle
		"""
		for (fx, fy, fw, fh) in faces:
			cv2.rectangle(
				frame, (fx, fy), (fx+fw, fy+fh),
				(255, 0, 0), 3
			)
		# saving webcame video
		out.write(frame)

		# display webcame
		cv2.imshow('Video', frame)

		# Wait for keyboard input
		# & 0xFF is required for 64bit machine
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()