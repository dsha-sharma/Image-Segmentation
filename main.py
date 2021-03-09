import numpy as np
from skimage.color import rgb2gray
import cv2 
import matplotlib.pyplot as plt 
from scipy import ndimage
# %matplotlib inline

image = plt.imread('1.jpg')
print(image.shape)
print(plt.imshow(image))

gray = rgb2gray(image)
print(plt.imshow(gray, cmap='gray'))

print(gray.shape)

gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
	if gray_r[i] > gray_r.mean():
		gray_r[i] = 1
	else:
		gray_r[i] = 0

gray = gray_r.reshape(gray.shape[0], gray.shape[1])
print(plt.imshow(gray, cmap='gray'))
