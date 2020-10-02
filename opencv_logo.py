import numpy as np 
import cv2

img = np.zeros((512, 512, 3), np.uint8)

img = cv2.ellipse(img, (243, 90), (80, 80), 0, 100, 360, (0, 0, 255), 5)
img = cv2.ellipse(img, (89,308), (80, 80), 0, 100, 360, (0, 0, 255), 5)
img = cv2.ellipse(img, (355,320), (80, 80), 0, 100, 360, (0, 0, 255), 5)
cv2.imshow('OpenCV Logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()