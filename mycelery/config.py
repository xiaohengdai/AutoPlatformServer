# broker_url = 'amqp://guest:guest@localhost:5672//'  #rabbitmq做任务队列
broker_url='redis://127.0.0.1:6379/1'  #redis做任务队列
result_backend='redis://127.0.0.1:6379/2'  #做结果存储


enable_utc = False  #系统时间是北京时间
timezone = 'Asia/Shanghai'  #系统时间是北京时间