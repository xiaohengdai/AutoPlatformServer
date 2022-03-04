import cv2

img='/Users/xh/Downloads/ks/qa-irs/app/task/frames/60/irs-1cd298e4ed39042588cb5224662f79b2.mp4.mp4/00001.jpg'
# 把图片转换为单通道的灰度图
img=cv2.imread(img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 获取灰度图矩阵的行数和列数
r, c = gray_img.shape[:2]
piexs_sum = r * c  # 整个弧度图的像素个数为r*c

# 获取偏暗的像素(表示0~19的灰度值为暗) 此处阈值可以修改
dark_points = (gray_img < 20)
target_array = gray_img[dark_points]
dark_sum = target_array.size
# 判断灰度值为暗的百分比
dark_prop = dark_sum / (piexs_sum)
if dark_prop >= 0.85:
    print("black")
else:
    print("no black")
