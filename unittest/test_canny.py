import cv2
import numpy as np

img = cv2.imread("/Users/xh/Downloads/ks/vision-ui/unittest/green.png", 0)
cv2.imwrite("/Users/xh/Downloads/ks/vision-ui/unittest/canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("/Users/xh/Downloads/ks/vision-ui/unittest/canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
