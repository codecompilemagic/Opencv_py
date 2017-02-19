import numpy as np
import cv2
import sys

video_path = sys.argv[1]
cap = cv2.VideoCapture(video_path)

while (cap.isOpened()):
	ret, frame = cap.read()
	if ret:
		cv2.imshow('Video', frame)

		if cv2.waitKey(100) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()