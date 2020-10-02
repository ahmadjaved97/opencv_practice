import numpy as np 
import cv2

def nothing(x):
	pass

# Create a black image, a window

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('imagef')

# Create trackbars for color change
cv2.createTrackbar('R', 'imagef', 0, 255, nothing)
cv2.createTrackbar('G', 'imagef', 0, 255, nothing)
cv2.createTrackbar('B', 'imagef', 0, 255, nothing)

# Create switch for ON/ OFF functionality
switch = '0 : OFF \n1: ON'
cv2.createTrackbar(switch, 'imagef', 0, 1, nothing)

while True:
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break


	# get current positions of trackbars
	r = cv2.getTrackbarPos('R', 'imagef')
	g = cv2.getTrackbarPos('G', 'imagef')
	b = cv2.getTrackbarPos('B', 'imagef')
	s = cv2.getTrackbarPos(switch, 'imagef')


	if s == 0:
		img[:] = 0
	else:
		img[100:200, 200:300, :] = [b, g, r]


cv2.destroyAllWindows()


	