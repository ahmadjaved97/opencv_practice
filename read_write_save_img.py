import numpy as np 
import cv2

def show_image(image):
	cv2.imshow('Image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def save_image(image, mode='color'):
	if mode == 'grayscale':
		gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		cv2.imwrite('gray_image.png', gray_img)
	elif mode == 'color':
		cv2.imwrite('color_image.png', image)






if __name__ == '__main__':
	img = cv2.imread('messi5.jpg')
	show_image(img)
	save_image(img, 'color')