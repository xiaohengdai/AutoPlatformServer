from mycelery.main import app
import os

@app.task(name="test")  # name指定任务名称
def test():
    os.system("/Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer1/bin/python3 /Users/xh/Downloads/ks/AutoPlatformServer/ScheduleTask/AutoReportHealth.py")