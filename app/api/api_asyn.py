from flask import Blueprint, jsonify
from mycelery.celery_task.tasks import test_celery
from mycelery.celery_task.tasks import test_celery2

api_asyn = Blueprint('api_asyn', __name__,url_prefix='/api/asyn')


@api_asyn.route('/test_asyn', methods=['GET'])
def test_asyn():
    print("test")
    # 立即告知celery去执行test_celery任务，并传入一个参数
    result = test_celery.delay('第一个的执行')
    print("result1.id:", result.id)
    result = test_celery2.delay('第二个的执行')
    print("result2.id:", result.id)

    return jsonify({"msg": "开启成功", "code": 200})
