

from mycelery.main import app
import os,time
from celery.utils.log import  get_task_logger

logger=get_task_logger(__name__)

@app.task(name="test")  # name指定任务名称
def test():
    logger.debug('start scherule task run')
    os.system("/Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer1/bin/python3 /Users/xh/Downloads/ks/AutoPlatformServer/ScheduleTask/AutoReportHealth.py")

@app.task(name='test_celery')
def test_celery(res):
    logger.debug('start test_celery run')
    time.sleep(5)
    return "test_celery任务结果:%s"%res

@app.task(name='test_celery2')
def test_celery2(res):
    logger.debug('start test_celery2 run')
    time.sleep(5)
    return "test_celery2任务结果:%s"%res