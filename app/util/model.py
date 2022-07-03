from peewee import *
from playhouse import pool
from playhouse.shortcuts import model_to_dict
from playhouse.shortcuts import ReconnectMixin

class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass

db = ReconnectMySQLDatabase(host="127.0.0.1", port=3306, passwd='xh123', user='root', database='auto_test',
                              autoconnect=False)


class VideoFrameDetailed(Model):
    job_id = AutoField()
    scene_frame_pic_set=TextField()
    stage_num=IntegerField(verbose_name='多阶段数目')
    scene_start_frame_index=CharField(verbose_name="场景开始帧序号",default='[]')
    scene_end_frame_index=CharField(verbose_name="场景结束帧序号",default='[]')
    scene_page_load_times=CharField(verbose_name="场景页面加载耗时")
    mainFormData=CharField(default='{}')
    frame_rate=IntegerField(verbose_name='拆帧率')

    class Meta:
        database=db
        table_name='frame_detailed'

if __name__ == '__main__':

    db.create_tables([VideoFrameDetailed])