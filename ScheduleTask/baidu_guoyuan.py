import uiautomator2 as u2
import time

d = u2.connect('38573286')
# print("d.info:",d.info)


for i in range(0,10000):
    print(f"执行第{i+1}次")
    # d(textContains='79').click()
    # if d(textContains='300').exists():
    #     d(textContains='300').click()
    if (i%50==0):
        d.click(0.045,0.568)
    d.click(0.808,0.823)
    time.sleep(2)
    if d(textContains='可开启').exists():
        d(textContains='可开启').click()
        time.sleep(2)
        # d(textContains='开心收下').click()
        d.click(0.585,0.636)