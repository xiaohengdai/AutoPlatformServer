"""
    Code creation time:September 11, 2021
    Author:PanBo
    Realize function:It mainly realizes the recognition and calibration of fonts with different colors
"""

#python+opencv实现文字颜色识别与标定功能：https://www.jb51.net/article/222708.htm
#Mac系统下查看鼠标所在点的RGB值--数码测色计:https://blog.csdn.net/iteye_20812/article/details/82405136
#如何用Python PIL获取图片的RGB数值？:https://www.zhihu.com/question/29807693

#识别字体中的颜色：先判断页面是否有这个文字，有的话用ocr提取文字并去除对应坐标，然后判断坐标中是否有相应字体的rgb值

from PIL import Image

im = Image.open('/Users/xh/Downloads/ks/qa-irs/app/task/frames/60/irs-270058e13e4e465321b1e671d424e547.mp4.mp4/00265.jpg')#打开图片
pix = im.load()#导入像素
# print("pix:",pix)
width = im.size[0]#获取宽度
height = im.size[1]#获取长度

for x in range(width):
    for y in range(height):
        print("pix[x, y]:",pix[x, y])
        r, g, b = pix[x, y]  # pix获取rgb值
        rgb = r, g, b




