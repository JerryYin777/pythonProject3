import cv2 as cv
import numpy as np
img=cv.imread('image/1.png',0)

import cv2 as cv
import numpy as np
img=cv.imread('image/1.png',0)
print(img)
cv.imshow('image',img)

cv.waitKey(0)#对图像的显示

cv.destroyAllWindows()
