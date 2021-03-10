import numpy as np
from skimage.color import rgb2gray
import cv2 
import matplotlib.pyplot as plt 
from scipy import ndimage
# %matplotlib inline
# reading the input image
image = plt.imread('1.jpeg')
print(image.shape)
print(plt.imshow(image))
# converting the input image to grayscale
gray = rgb2gray(image)
print(plt.imshow(gray, cmap='gray'))

print(gray.shape)
# take the mean of the pixel values and use that as threshold
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
	if gray_r[i] > gray_r.mean():
		gray_r[i] = 1
	else:
		gray_r[i] = 0

gray = gray_r.reshape(gray.shape[0], gray.shape[1])
print(plt.imshow(gray, cmap='gray'))
# defining multiple thresholds to detect multiple objects
gray = rgb2gray(image)
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    elif gray_r[i] > 0.5:
        gray_r[i] = 2
    elif gray_r[i] > 0.25:
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray, cmap='gray')