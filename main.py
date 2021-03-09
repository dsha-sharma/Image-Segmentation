import numpy as np
from skimage.color import rgb2gray
import cv2 
import matplotlib.pyplot as plt 
from scipy import ndimage
# %matplotlib inline

image = plt.imread('1.jpeg')
image.shape
plt.imshow(image)
