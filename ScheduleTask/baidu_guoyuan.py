import uiautomator2 as u2
import time

d = u2.connect('38573286')
# print("d.info:",d.info)
app_package_name='com.baidu.searchbox'

for i in range(0,10):
    d(textContains='82').click()
    time.sleep(3)
    if d(textContains='可开启').exists():
        d(textContains='可开启').click()
        time.sleep(2)
        d(textContains='开心收下').click()