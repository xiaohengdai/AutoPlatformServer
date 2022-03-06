from celery import Celery
from celery.schedules import crontab

# 首先实例化一个celery对象
app = Celery('xh')
# 然后配置此对象
app.config_from_object('mycelery.config')

# # 通过celery对象.autodiscover_tasks 让woker自动去任务队列中发现任务
app.autodiscover_tasks(['mycelery.celery_task'])  # celery_task为存放tasks.py文件的目录



# tesk:test test为任务名称
app.conf.beat_schedule = {
    'auto_send': {
        'task': 'test',
        'schedule': crontab(minute='00',hour='7', day_of_week='0-6'),
        # 'schedule': crontab(minute='42',hour='18', day_of_week='0-6'),
        # 'schedule': crontab(minute='*/3'),
#     'schedule':timedelta(seconds=30)   # 1 每10秒钟执行一次
        'args': ()
    }
}
