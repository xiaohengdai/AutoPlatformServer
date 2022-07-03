import datetime
import os
import time

from cv2 import cv2
from airtest.core.cv import Template
import numpy as np
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import make_response
from flask_cors import cross_origin
from app.util.jsonUtil import json_resp
from app.util.model import VideoFrameDetailed
from app.util.videocutter import video_cutter_to_save_to_internet
from service.image_airtest import mark_border_img
from service.image_cluster import reco_by_page_main_tonal_value
from service.image_diff import ImageDiff
from service.image_merge import Stitcher
from service.image_similar import HashSimilar
# from service.image_text import get_image_text
from service.image_utils import get_pop_v, get_image_text
from tools.video_tools import *
import pycorrector
from celery.utils.log import get_task_logger
from nb_log import LogManager
from nb_log.handlers import ColorHandler

logger=get_task_logger(__name__)
# logger = LogManager("logger").get_logger_and_add_handlers(
#     log_path='/Users/xiaoheng/Downloads/meituan/AutoPlatformServer/log',
#     log_filename='AutoPlatformServer_%s.log' % time.strftime('%Y_%m_%d_%H_%M_%S'))
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/diff', methods=["POST"])
def api_diff():
    print("request.json:", request.json)
    data = {
        "code": 0,
        "data": ImageDiff().get_image_score(request.json['image1'], request.json['image2'],
                                            request.json['image_diff_name'])
    }
    return jsonify(data)


@api.route('/merge', methods=["POST"])
def vision_merge():
    data = {
        "code": 0,
        "data": Stitcher(request.json['image_list']).image_merge(
            request.json['name'],
            without_padding=request.json.get('without_padding')
        )
    }
    return jsonify(data)


@api.route('/similar', methods=["POST"])
def vision_similar():
    data = {
        "code": 0,
        "data": HashSimilar().get_hash_similar(request.json['image1'], request.json['image2'])
    }
    return jsonify(data)


@api.route('/pop', methods=["POST"])
def vision_pop():
    data = {
        "code": 0,
        "data": get_pop_v(request.json['image'])
    }
    return jsonify(data)


@api.route('/text', methods=["POST"])
def vision_text():
    data = {
        "code": 0,
        "data": get_image_text(request.json['image'])
    }
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/json;charset=utf-8"
    return resp


@api.route('/ocr/start_run', methods=["POST"])
def vision_ocr_start_run():
    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    if '.' not in file_name:
        file_name = file_name + '.png'
    print("file_name:", file_name)
    print("request.files:", request.files)
    img_obj = request.files['file'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    image_dir = os.path.join(current_dir, "image")
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    ocr_dir = os.path.join(current_dir, "image", "ocr")
    if not os.path.exists(ocr_dir):
        os.mkdir(ocr_dir)
    print("ocr_dir:", ocr_dir)
    local_img_path = os.path.join(ocr_dir, file_name)
    print("local_img_path:", local_img_path)
    with open(local_img_path, 'wb') as saveFp:
        saveFp.write(img_obj)

    data = {
        "code": 0,
        "data": get_image_text(local_img_path)
    }
    print("data:", data)
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


@api.route('/image/opencv/search', methods=["POST"])
def image_opencv_search():
    threshold = float(request.values.get('threshold', default=0.7))
    big_image_file_name = request.values.get('big_image', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    small_patch_file_name = time.strftime("%Y_%m_%d_%H_%M_%S")
    if '.' not in big_image_file_name:
        big_image_file_name = 'big_image' + big_image_file_name + '.png'
    small_patch_file_name = 'small_patch' + small_patch_file_name + '.png'
    print("big_image_file_name:", big_image_file_name)
    print("request.files:", request.files)
    big_img_obj = request.files['big_image'].stream.read()
    small_patch_img_obj = request.files['small_patch'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    search_dir = os.path.join(current_dir, "image", "search")
    if not os.path.exists(search_dir):
        os.mkdir(search_dir)
    print("search_dir:", search_dir)
    local_big_img_path = os.path.join(search_dir, big_image_file_name)
    small_patch_img_path = os.path.join(search_dir, small_patch_file_name)
    print("local_big_img_path:", local_big_img_path)
    print("small_patch_img_path:", small_patch_img_path)
    with open(local_big_img_path, 'wb') as saveFp:
        saveFp.write(big_img_obj)
    with open(small_patch_img_path, 'wb') as saveFp:
        saveFp.write(small_patch_img_obj)
    screen_image = cv2.imdecode(np.fromfile(local_big_img_path, dtype=np.uint8), 100)
    print("threshold:", threshold)
    template = Template(small_patch_img_path, threshold=threshold)
    res = template._cv_match(screen_image)
    data = {
        "code": 0,
        "data": res
    }
    res = template._cv_match(screen_image)
    print("res:", res)
    rectangle = res['rectangle']
    x0 = rectangle[0][0]
    y0 = rectangle[0][1]
    x1 = rectangle[2][0]
    y1 = rectangle[2][1]
    print(x0, y0, x1, y1)

    mark_border_img(local_big_img_path, x0, y0, x1, y1)
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


@api.route('/diff/start_run', methods=["POST"])
def vision_diff_start_run():
    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    file_name1 = file_name + '_1'
    diff_file_name = file_name + '_diff'
    if '.' not in file_name:
        file_name = file_name + '.png'
        file_name1 = file_name1 + '.png'
        diff_file_name = diff_file_name + '.png'
    print("file_name:", file_name)
    print("request.files:", request.files)
    request_files_dict = request.files.to_dict()
    request_files = request.files
    img_list = []
    for key in request_files_dict:
        img_file = request_files[key].stream.read()
        img_list.append(img_file)
    img_obj = img_list[0]
    img_obj1 = img_list[1]
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    diff_dir = os.path.join(current_dir, "image", "diff")
    if not os.path.exists(diff_dir):
        os.mkdir(diff_dir)
    print("diff_dir:", diff_dir)
    local_img_path = os.path.join(diff_dir, file_name)
    print("local_img_path:", local_img_path)
    with open(local_img_path, 'wb') as saveFp:
        saveFp.write(img_obj)

    local_img_path1 = os.path.join(diff_dir, file_name1)
    print("local_img_path1:", local_img_path1)
    with open(local_img_path1, 'wb') as saveFp:
        saveFp.write(img_obj1)
    diff_file_path = os.path.join(diff_dir, diff_file_name)
    score = ImageDiff().get_image_score(local_img_path, local_img_path1,
                                        diff_file_path)
    print("diff_file_path:", diff_file_path)
    img = cv2.imread(diff_file_path, 0)
    img1 = img.copy()

    front_diff_dir = "/Users/xh/Downloads/ks/stitch-frontend/src/assets/img"
    front_diff_image = os.path.join(front_diff_dir, "diff.png")
    cv2.imwrite(front_diff_image, img1)
    data = {'score': score, 'diff_image': diff_file_name}
    print("data:", data)
    data = {
        "code": 0,
        "data": [data]
    }
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


@api.route('/img/cluster/start_run', methods=["POST"])
def img_cluster_start_run():
    # target_main_tonal_value=request.values.get('target_value')
    # if not target_main_tonal_value:
    #     data = {
    #         "code": -1,
    #         "data": {}
    #     }
    #     resp = make_response(jsonify(data))
    #     resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    #     return resp

    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    if '.' not in file_name:
        file_name = file_name + '.png'
    print("file_name:", file_name)
    print("request.files:", request.files)
    img_obj = request.files['file'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    cluster_dir = os.path.join(current_dir, "image", "cluster")
    if not os.path.exists(cluster_dir):
        os.mkdir(cluster_dir)
    print("cluster_dir:", cluster_dir)
    local_img_path = os.path.join(cluster_dir, file_name)
    print("local_img_path:", local_img_path)
    with open(local_img_path, 'wb') as saveFp:
        saveFp.write(img_obj)
    res = str(reco_by_page_main_tonal_value(local_img_path, target_main_tonal_value="DARK_RED"))
    print("res:", res)
    data = {
        "code": 0,
        "data": {'data': [{'value': res}]}
    }
    print('data:', data)
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


@api.route('/wrong_word/detect', methods=["POST"])
def wrong_word_detect():
    text = request.values.get('text')
    print("text:", text)
    idx_errors = pycorrector.detect(
        text)  # 返回类型是list, [error_word, begin_pos, end_pos, error_type]，pos索引位置以0开始。begin_pos=<实际位置<end_pos
    print("idx_errors:", idx_errors)
    new_detect_value = [''] * len(idx_errors)
    for i in range(0, len(idx_errors)):
        new_detect_value[i] = {"error_word": idx_errors[i][0], "begin_pos": idx_errors[i][1],
                               "end_pos": idx_errors[i][2], "error_type": idx_errors[i][3]}
    data = {
        "code": 0,
        "data": {"res": new_detect_value}
    }
    print('data:', data)
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


@api.route('/wrong_word/correct', methods=["POST"])
def wrong_word_correct():
    text = request.values.get('text')
    print("text:", text)
    idx_errors = pycorrector.correct(
        text)  # 返回类型是list, [error_word, begin_pos, end_pos, error_type]，pos索引位置以0开始。begin_pos=<实际位置<end_pos
    print("idx_errors:", idx_errors)
    print("idx_errors[0]:", idx_errors[0])
    print("idx_errors[1]:", idx_errors[1])
    new_detect_value = [''] * len(idx_errors[1])
    for i in range(0, len(idx_errors[1])):
        new_detect_value[i] = {"new_sentence": idx_errors[0], "error_word": idx_errors[1][i][0],
                               "correct_word": idx_errors[1][i][1], "begin_pos": idx_errors[1][i][2],
                               "end_pos": idx_errors[1][i][3]}

    data = {
        "code": 0,
        "data": {"res": new_detect_value}
    }
    print('data:', data)
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


# 对视频进行裁剪
@api.route('/video/cutter', methods=["POST"])
def video_cutter():
    start_time = request.values.get("start_time", default=str(1))
    stop_time = request.values.get("stop_time", default=None)
    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    if '.' not in file_name:
        file_name = file_name + '.mp4'
    video_obj = request.files['video_file'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    video_dir = os.path.join(current_dir, "video")
    print("video_dir:", video_dir)
    if not os.path.exists(video_dir):
        os.mkdir(video_dir)
    video_path = os.path.join(video_dir, file_name)
    with open(video_path, 'wb') as saveFp:
        saveFp.write(video_obj)
    cutter_dir = os.path.join(video_dir, 'cutter')
    print("cutter_dir:", cutter_dir)
    if not os.path.exists(cutter_dir):
        os.mkdir(cutter_dir)
    cutter_video_path = os.path.join(cutter_dir, file_name)
    target_video_abs_path = clip_handle(source_video_abs_path=video_path, target_video_abs_path=cutter_video_path,
                                        start_time=int(start_time), stop_time=int(stop_time))
    print("target_video_abs_path:", target_video_abs_path)
    data = {
        "code": 0,
        "data": {"target_video_abs_path": target_video_abs_path}
    }
    resp = make_response(jsonify(data))
    resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    return resp


# 对视频进行裁剪
@api.route('/video/get', methods=["POST", "GET"])
def get_video():
    video_url = "/Users/xh/Downloads/ks/qa-irs/time_cost_calc/test/dy-friend-2.mp4"
    data = {
        "code": 0,
        "data": {"video_url": video_url}
    }
    print("data:", data)
    # resp = make_response(jsonify(data))
    # resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    # print("resp:",resp)
    # return resp
    return jsonify(data)


@api.route('/string', methods=["POST", "GET"])
def get_string():
    video_url = "/Users/xh/Downloads/ks/qa-irs/time_cost_calc/test/dy-friend-2.mp4"
    data = {
        "code": 0,
        "data": {"string": video_url}
    }
    print("data:", data)
    # resp = make_response(jsonify(data))
    # resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    # print("resp:",resp)
    # return resp
    return jsonify(data)


@api.route('/video/getVideoInfo', methods=["POST", "GET"])
def get_video_info():
    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    if '.' not in file_name:
        file_name = file_name + '.mp4'
    print("file_name:", file_name)
    print("request.files:", request.files)
    img_obj = request.files['file'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    cluster_dir = os.path.join(current_dir, "video")
    if not os.path.exists(cluster_dir):
        os.mkdir(cluster_dir)
    print("cluster_dir:", cluster_dir)
    local_img_path = os.path.join(cluster_dir, file_name)
    print("local_img_path:", local_img_path)
    with open(local_img_path, 'wb') as saveFp:
        saveFp.write(img_obj)
    video_length = get_video_length(filepath=local_img_path)
    width, height = get_video_resolution(video_file=local_img_path)
    file_size = get_filesize(filepath=local_img_path)
    video_info = [
        {"video_time": str(video_length) + 's', 'video_width': width, 'video_height': height, 'file_size': file_size}]
    dest_dir = get_video_cutter(input_video_path=local_img_path)
    img_list = os.listdir(dest_dir)
    img_list = sorted(img_list)
    img_list_dict = {}
    for i in range(0, len(img_list)):
        img_list_dict["video_frame_" + str(i + 1)] = os.path.join(dest_dir, img_list[i])
    video_frame = [img_list_dict]
    data = {
        "code": 0,
        "data": {"video_info": video_info, "video_frame": video_frame}
    }
    print("data:", data)
    # resp = make_response(jsonify(data))
    # resp.headers["Content-Type"] = "application/x-www-form-urlencoded"
    # print("resp:",resp)
    # return resp
    return jsonify(data)


@api.route('/video/videoFrame', methods=["POST", "GET"])
def video_rame():
    frame_rate = int(request.values.get("frame_rate"))
    logger.info("frame_rate:" + str(frame_rate))
    stage_num = int(request.values.get('stage_num'))
    # logger.info("stage_num:"+str(stage_num))
    pagenum = int(request.values.get("pagenum"))
    pagesize = int(request.values.get("pagesize"))
    file_name = request.values.get('file_name', default=time.strftime("%Y_%m_%d_%H_%M_%S"))
    if '.' not in file_name:
        file_name = file_name + '.mp4'
    print("file_name:", file_name)
    # print("request.files:", request.files)
    img_obj = request.files['file'].stream.read()
    current_dir = os.getcwd()
    print("current_dir:", current_dir)
    cluster_dir = os.path.join(current_dir, "video")
    if not os.path.exists(cluster_dir):
        os.mkdir(cluster_dir)
    print("cluster_dir:", cluster_dir)
    local_img_path = os.path.join(cluster_dir, file_name)
    print("local_img_path:", local_img_path)
    with open(local_img_path, 'wb') as saveFp:
        saveFp.write(img_obj)

    # dest_dir=get_video_cutter(input_video_path=local_img_path, frame_count=30)
    pic_path, videocutter_frame_path, img_list = video_cutter_to_save_to_internet(input_video_path=local_img_path,
                                                                                  frame_rate=frame_rate,type=1)
    print("pic_path:",pic_path)
    print("videocutter_frame_path:",videocutter_frame_path)
    # print("img_list:", img_list)


    video_frame = []
    scene_frame_pic_set = []
    data_list = []
    data_dict = {}
    for i in range(0, len(img_list)):
        if (i >= (pagenum - 1) * pagesize) and (i < pagenum * pagesize):
            data_dict[i + 1] = img_list[i]
            data_list.append({"frame_num": (i + 1), "img_src": img_list[i]})
        img_list_dict = {}
        # img_list_dict["video_frame_"+str(i+1)]=os.path.join(dest_dir,img_list[i])
        img_list_dict['frame_num'] = str(i + 1)
        img_list_dict['img_src'] = img_list[i]
        video_frame.append(img_list_dict)
        scene_frame_pic_set.append(img_list[i])

    mainFormData = {}
    formItemList = []
    scene_start_frame_index = []
    scene_end_frame_index = []
    for i in range(0, stage_num):
        form_item_dict = {"label": "第" + str(i + 1) + '阶段起始帧', "key": "start_" + str(i + 1)}
        formItemList.append(form_item_dict)
        mainFormData["start_" + str(i + 1)] = -1
        scene_start_frame_index.append(mainFormData["start_" + str(i + 1)])
        form_item_dict = {"label": "第" + str(i + 1) + '阶段结束帧', "key": "end_" + str(i + 1)}
        formItemList.append(form_item_dict)
        mainFormData["end_" + str(i + 1)] = -1
        scene_end_frame_index.append(mainFormData["end_" + str(i + 1)])
    print("开始插入数据")
    videoFrameDetailed = VideoFrameDetailed(scene_frame_pic_set=scene_frame_pic_set, updated_time=datetime.datetime.now,
                                            stage_num=stage_num, frame_rate=frame_rate,
                                            scene_start_frame_index=scene_start_frame_index,
                                            scene_end_frame_index=scene_end_frame_index, mainFormData=mainFormData)
    print("插入数据完成")
    videoFrameDetailed.save()
    job_id = videoFrameDetailed.job_id
    # print("video_frame:",video_frame)

    return json_resp(
        data={"video_frame": data_list, "total": len(img_list), "job_id": job_id, "mainFormData": mainFormData,
              "formItemList": formItemList}, msg="success")
