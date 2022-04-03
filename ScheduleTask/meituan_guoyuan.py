import uiautomator2 as u2
import time

d = u2.connect('38573286')
# print("d.info:",d.info)


for i in range(0,1000):
    print(f"执行第{i+1}次")
    # d(textContains='79').click()
    # if d(textContains='300').exists():
    #     d(textContains='300').click()

    d.click(0.808,0.823)
    time.sleep(2)
