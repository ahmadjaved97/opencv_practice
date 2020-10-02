import numpy as np 
import cv2
import random
# # Create a black image
# img = np.zeros((512, 512, 3), np.uint8)

# # Draw a diagonal blue line with thickness 3px

# img = cv2.line(img, (0,0), (511, 511), color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA)

# # Draw a rectangle

# img = cv2.rectangle(img, (384, 0), (510, 128), color=(0, 255, 0), thickness=3)

# # Draw a circle
# img = cv2.circle(img, (450, 63), 55, color=(0, 0, 255), thickness=2)

# # Draw an ellipse

# img = cv2.ellipse(img, (256,256), (100, 50), 0, startAngle=40, endAngle=360, color=(255,0,255),thickness=2)

# # Draw a polygon
# pts = np.array([[10,5], [20, 30], [70,20], [50,10], [256,245], [70,321]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# img = cv2.polylines(img, [pts], True, (0,0,255), thickness=4)
# img = cv2.fillPoly(img, [pts], color=(0,255,255), shift=2)


# cv2.imshow('Blue Line', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = np.zeros((800, 800, 3), np.uint8)


# for i in range(15000):
# 	img = cv2.line(img, (random.randint(0,600), random.randint(0,800)), (random.randint(0,800), random.randint(0,512)),
# 							color = (
# 								random.randint(0,255),
# 								random.randint(0,255),
# 								random.randint(0,255)),
# 							thickness=2,
# 							lineType=cv2.LINE_AA)


# for i in range(50):
# 	img = cv2.circle(img, (random.randint(120,600), random.randint(0,800)),
# 			radius=random.randint(0,150),
# 			color = (
# 				random.randint(0,255),
# 				random.randint(0,255),
# 				random.randint(200,255)),
# 			thickness=2,
# 			lineType=cv2.LINE_AA)


# Draw random polygons
for i in range(50):
	pts = np.array([
		[random.randint(0,800), random.randint(0,800)],
		[random.randint(0,800), random.randint(0,800)],
		[random.randint(0,800), random.randint(0,800)],
		[random.randint(0,800), random.randint(0,800)]], np.int32)
	pts = pts.reshape((-1,1,2))
	img = cv2.polylines(img, [pts], False,
		color= (random.randint(0,255),
			random.randint(0,255),
			random.randint(0,255)),
			thickness=4)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
