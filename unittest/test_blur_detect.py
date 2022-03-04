import cv2
#利用拉普拉斯识别图片清晰度
def getImageVar(imgPath):
    image = cv2.imread(imgPath)
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    return imageVar
imageVar = getImageVar("/Users/xh/Downloads/ks/vision-ui/unittest/test/gaoqing.jpg")
print(imageVar)