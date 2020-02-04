# first is to read an image and conver it greyscale

import cv2

def readImage(path, width=28, height=28):
    # Using cv2.imread() method
    # Using 0 to read image in grayscale mode
    img = cv2.imread(path, 0)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    return resized

path = '../training/training/n0/n0018.jpg'

img = readImage(path)

# flatten the image
img = img.flatten(order='C')

print(img.shape)
