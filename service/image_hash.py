from PIL import Image
import imagehash

#图像感知hash算法，http://www.srcmini.com/61197.html
image_hash1=imagehash.phash(Image.open('/Users/xh/Downloads/ks/qa-irs/app/task/frames/60/irs-1cd298e4ed39042588cb5224662f79b2.mp4.mp4/00001.jpg'))
print(image_hash1)
image_hash2=imagehash.phash(Image.open('/Users/xh/Downloads/ks/qa-irs/app/task/frames/60/irs-1cd298e4ed39042588cb5224662f79b2.mp4.mp4/00002.jpg'))
print(image_hash2)
if (image_hash1==image_hash2):
    print("相似")
else:
    print("不相似")