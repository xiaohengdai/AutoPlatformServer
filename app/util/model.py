from playhouse import pool
from playhouse.shortcuts import model_to_dict

db=pool.PooledMySQLDatabase(host=,port=,passwd=,user,database=,autoconnect=False,max_connection=,stale_timeout=)

class VideoFrameDetailed():
    job_id=AutoField()