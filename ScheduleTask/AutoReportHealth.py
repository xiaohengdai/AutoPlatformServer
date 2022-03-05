import re

import uiautomator2 as u2
import time
from paddleocr import PaddleOCR

def is_target_in_ocr_result(ocr_result, target_text):
    """
       判断target_text是否在ocr识别结果中
       """
    # ocr_result = refine_ocr_result(ocr_result)
    print("target_text:", target_text)
    print("ocr_result:", ocr_result)
    if target_text == "" and len(ocr_result) == 0:
        return True
    if target_text == "" and len(ocr_result) != 0:
        return False
    for key in ocr_result:
        # print("target_text:", target_text)
        # print("key[1]:", key[1])
        res = re.findall(target_text, key[1][0])
        if len(res) > 0:
            point=key[0]
            x=int((point[0][0]+point[1][0])/2)
            y=int((point[1][1]+point[2][1])/2)
            return True,[x,y]
    return False,None


d = u2.connect('6HJ4C19713036738')
# print("d.info:",d.info)
app_package_name='net.whty.app.eyu'


d.app_stop(app_package_name)
d.app_start(app_package_name)
time.sleep(4)
d(text='学习').click()
time.sleep(2)
d(text='健康上报').click()
time.sleep(4)

ocr = PaddleOCR(use_gpu=False, use_angle_cls=True, lang="ch")
img_path = '/Users/xh/Downloads/ks/AutoPlatformServer/tmp/去上报.png'
d.screenshot(img_path)

ocr_result = ocr.ocr(img_path, cls=True)
print("ocr_result:",ocr_result)


# line是一个列表' [[文本框的位置],(文字,置信度)] '
target_text='去上报'
res=is_target_in_ocr_result(ocr_result=ocr_result, target_text=target_text)
print("res:",res)
d.click(x=res[1][0], y=res[1][1])
time.sleep(3)
d.set_fastinput_ime(True) # 切换成FastInputIME输入法
d(className='android.widget.EditText').click()
#
#
d.send_keys("36.3") # adb广播输入
d(text='正常到校').click()
d.swipe(0.5, 0.95, 0.5, 0.75)
if d(text='完成').exists:
    d(text='完成').click()
time.sleep(1)
d(text='阴性').click()
d.swipe(0.5, 0.95, 0.5, 0.75)
time.sleep(1)
if d(text='完成').exists:
    d(text='完成').click()
time.sleep(1)
d(className='android.widget.EditText')[-1].click()
d.clear_text()
d.send_keys("湿疹不宜接种疫苗")
d(description='提交').click()
