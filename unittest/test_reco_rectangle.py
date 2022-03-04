import cv2
#参考文章：
# 利用opencv2python实现图像中矩形与正方形的区分：https://www.cnpython.com/qa/176780

raw_image = cv2.imread('/Users/xh/Downloads/ks/vision-ui/unittest/green.png')
# cv2.imshow('Original Image', raw_image)
# cv2.waitKey(0)

bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
# cv2.imshow('Bilateral', bilateral_filtered_image)
# cv2.waitKey(0)

edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
# cv2.imshow('Edge', edge_detected_image)
# cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
# for contour in contours:
#     approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
#     area = cv2.contourArea(contour)
#     if ((len(approx) >= 3)):
#         contour_list.append(contour)
#
# cv2.drawContours(raw_image, contour_list,  -1, (0,0,0), 2)
# cv2.imshow('Objects Detected',raw_image)
# cv2.waitKey(0)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)   #对指定的点集进行多边形逼近的函数，其逼近的精度可通过参数设置。
    area = cv2.contourArea(contour)  #此函数利用格林公式计算轮廓的面积。对于具有自交点的轮廓，该函数几乎肯定会给出错误的结果。
    # print("approx:",approx)
    if ((len(approx) == 4)):
        (x, y, w, h) = cv2.boundingRect(approx)  #矩形边框（Bounding Rectangle）是说，用一个最小的矩形，把找到的形状包起来。还有一个带旋转的矩形，面积会更小，效果见下图
        print("x,y,w,h:",x,y,w,h)
        if ((w>=3) or (h>=5)):
            if  ((float(w)/h)==1):
                cv2.putText(raw_image, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)   #正方形
            else:
                cv2.putText(raw_image, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)  #长方形

        contour_list.append(contour)
cv2.imshow('',raw_image)
cv2.waitKey()
cv2.destroyAllWindows()