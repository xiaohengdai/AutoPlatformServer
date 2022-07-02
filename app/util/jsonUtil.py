from flask import jsonify


def json_resp(data, msg="成功",status=0):
    return _json_resp(data=data, status=status, msg=msg)


def json_err_resp(msg,data={}):
    return _json_resp(msg=msg, status=1, data=data)

def _json_resp(status, data, msg):
    return jsonify(
        status=status,
        data=data,
        msg=msg
    )
