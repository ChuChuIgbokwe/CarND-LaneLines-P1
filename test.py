#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 21, 2017 by 12:45 AM

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
def select_rgb_white_yellow(image):
    # white color mask
    lower = np.uint8([200, 200, 200])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(image, lower, upper)
    # yellow color mask
    lower = np.uint8([255,255, 0])
    upper = np.uint8([255, 255, 204])
    yellow_mask = cv2.inRange(image, lower, upper)
    # combine the mask
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked

# image = mpimg.imread('test_images/solidWhiteRight.jpg')
img = cv2.imread('test_images/solidWhiteRight.jpg')

#printing out some stats and plotting
# print('This image is:', type(image), 'with dimensions:', image.shape)
# plt.imshow(image)  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='g
xxx = select_rgb_white_yellow(img)

cv2.imshow('',xxx)
cv2.waitKey(0)