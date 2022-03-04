#主要利用airtest中的图像识别方法
from airtest.core.cv import Template
import numpy as np
import cv2


def mark_border_img(img_path, x0,y0,x1,y1,offset=0, words='airtest'):
    """
    mark the element of the img which has been operated via border
    :param img_path:
    :param x0,y0,x1,y1: 左上角x,y，右下角x,y
    :param offset:
    :param words:
    :return:
    """
    img = cv2.imread(img_path)
    draw = cv2.rectangle(img,
                         pt1=(int(x0), int(y0)),
                         pt2=(int(x1), int(y1)),
                         color=(0, 0, 255), thickness=12)
    cv2.imwrite(img_path, draw)
    if words:
        org = (int(x1) + offset * 2, int(y1) + offset)
        draw = cv2.putText(img, words, org, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
        cv2.imwrite(img_path, draw)

# small_patch="/Users/xh/Downloads/ks/vision-ui/image/airtest/smatch_2.png"
# screen_image_path="/Users/xh/Downloads/ks/vision-ui/image/airtest/origin_2.png"
# screen_image=cv2.imdecode(np.fromfile(screen_image_path, dtype=np.uint8), 100)
# template=Template(small_patch, threshold=0.7)
# res=template._cv_match(screen_image)
# print("res:",res)
# rectangle=res['rectangle']
# x0=rectangle[0][0]
# y0=rectangle[0][1]
# x1=rectangle[2][0]
# y1=rectangle[2][1]
# print(x0,y0,x1,y1)
#
# mark_border_img(screen_image_path,x0,y0,x1,y1)