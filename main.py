import numpy as np
from skimage.color import rgb2gray
import cv2 
import matplotlib.pyplot as plt 
from scipy import ndimage
# %matplotlib inline

image = plt.imread('1.jpeg')
print(image.shape)
print(plt.imshow(image))

gray = rgb2gray(image)
print(plt.imshow(gray, cmap='gray'))

print(gray.shape)
