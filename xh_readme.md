 /Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer/bin/python3 -m flask run  -p 9090
  
 /Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer/bin/python3 -m pip uninstall paddlepaddle
 /Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer/bin/python3 -m pip install paddlepaddle==1.8.5 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com


错别字检测：
mac下kenlm安装---pycorrector：https://www.pianshen.com/article/4448408404/
pycorrector:https://gitee.com/lets_see_the_thunderstorm/pycorrector/blob/master/README.md
https://github.com/shibing624/pycorrector
【深度学习】PyCorrector中文文本纠错实战：https://blog.csdn.net/luojie140/article/details/112306913

边缘和轮廓检测——计算机视觉的应用：https://zhuanlan.zhihu.com/p/419110847


文字分割:
OpenCV案例分析-水平&垂直投影分割:https://zhuanlan.zhihu.com/p/75351673


目标检测中的mAP是什么含义？:https://www.zhihu.com/question/53405779

#待添加功能
1、对视频进行拆帧


任务调度:
celery -A tasks worker -l INFO

Mac 启动和关闭rabbitmq:https://www.jianshu.com/p/65c221b9d4ac
爬虫架构|Celery+RabbitMQ快速入门（二）:https://www.jianshu.com/p/42b98f5eacb3
celery简单入门:http://t.zoukankan.com/landpack-p-5555955.html 
celery+rabbitmq消息队列使用笔记：https://blog.csdn.net/weixin_43262264/article/details/111573159 
mac brew install rabbitmq 
启动 报"Error when reading /Users/liyaochu/.erlang.cookie: eacces：https://blog.csdn.net/weixin_42047790/article/details/92798324 
Celery的监控工具flower：https://blog.csdn.net/hhd1988/article/details/108759042
celery5: 
Python之Celery定时任务:https://blog.csdn.net/panda_225400/article/details/121883120

worker启动命令: 这个命令会开启一个在前台运行的 worker，解释这个命令的意义：

worker: 运行 worker 模块。 -A: –app=APP, 指定使用的 Celery 实例。 -l: –loglevel=INFO, 指定日志级别，可选：DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL

其它常用的选项： -P: –pool=prefork, 并发模型，可选：prefork (默认，multiprocessing), eventlet, gevent, threads. -c: –concurrency=10, 并发级别，prefork 模型下就是子进程数量，默认等于 CPU 核心数


问题:
在m1芯片和big sur安装有问题，ocr的库安装不上去
解决：https://blog.csdn.net/solocao/article/details/109921277
升级shapely到最新


paddleocr安装
Python：paddleocr库安装及使用补充:https://blog.csdn.net/Fan_shine/article/details/123089196

定时任务：
Celery定时任务:https://blog.51cto.com/u_15127692/3834109
celery中crontab参数及秒的定时任务：https://blog.csdn.net/weixin_45707730/article/details/118079548
开启两个终端：
1、/Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer1/bin/python3 -m celery -A mycelery.main worker -l info -P eventlet
2、/Users/xh/Downloads/ks/AutoPlatformServer/venv_AutoPlatformServer1/bin/python3 -m celery -A mycelery.main beat -l info