# import numpy as np 
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
# 	# Capture frame by frame
# 	ret, frame = cap.read()
# 	print(cap.get(10))
# 	# Our operations on the frame
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 	#Display the resulting frame
# 	cv2.imshow('Video Frame', gray)
# 	if cv2.waitKey(1) &0xFF == ord('q'):
# 		break

# cap.release()
# cv2.destroyAllWindows()

# Save a video file

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640, 480),0)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame, 0)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Write the flipped frame
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) &0xFF == ord('q'):
			break
	else:
		break


# Release everything is job is fininsed
cap.release()
out.release()
cv2.destroyAllWindows()