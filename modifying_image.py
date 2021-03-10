import cv2
import random


img = cv2.imread('assets/logo.jpg', -1)
"""
-1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
"""

# img = cv2.resize(img, (300, 400))
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# print(img)  # numpy array
print(type(img))
print(img.shape)  # (height, width, channels) <- channels: colour space of the image(BGR - Blue Green Red)

print(img[155][45])

# modify image by changing pixel values
# for i in range(100):
#     for j in range(img.shape[1]):
#         # (rows, columns, channels)
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# tag = img[280:290, 70:80]
# img[260:270, 95:105] = tag  # paste part of image on the designated area

cv2.imwrite('new_img.jpg', img)  # write out the modified image
cv2.imshow('Image', img)
cv2.waitKey(0)  # go through it if pushing any key cf. 5: this code is going to be skipped without any key in 5 seconds
cv2.destroyAllWindows()
