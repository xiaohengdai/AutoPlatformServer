import os
import shutil
import subprocess

from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
import cv2
from PIL import Image
import ffmpy3


def sizeConvert( size):  # 单位换算
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(round(size / G,2)) + 'G Bytes'
    elif size >= M:
        return str(round(size / M,2)) + 'M Bytes'
    elif size >= K:
        return str(round(size / K,2)) + 'K Bytes'
    else:
        return str(round(size,2)) + 'Bytes'

def get_filesize(filepath):
    u"""
    获取文件大小（M: 兆）
    """
    file_byte = os.path.getsize(filepath)
    file_size=sizeConvert(file_byte)
    return file_size

def get_video_length(filepath):#这个更精确，小数点更多,video = r"/Users/xh/Downloads/ks/timeCostCalc/records/file.mp4"
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def get_video_time(video_abs_path):
    clip = VideoFileClip(video_abs_path)
    video_time = clip.duration
    print("video_time:", video_time)
    return video_time


# def get_video_fps(video_file):
#     video=cv2.VideoCapture(video_file)
#     major_ver=(cv2.getVersionMajor())
#     if int(major_ver)<3:
#         fps=video.get(cv2.CAP_PROP_FPS)
#         return fps
#     else:
#         fps=video.get(cv2.CAP_PROP_FPS)
#         return fps
#
def get_video_width(video_file):
    video=cv2.VideoCapture(video_file)
    width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    return width

def get_video_height(video_file):
    video=cv2.VideoCapture(video_file)
    height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return height

def get_video_resolution(video_file):
    video = cv2.VideoCapture(video_file)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width,height

def clip_video(source_video_abs_path, target_video_abs_path, start_time, stop_time):
    """
    利用moviepy进行视频剪切
    :param source_video_abs_path: 原视频的路径，mp4格式
    :param target_video_abs_path: 生成的目标视频路径，mp4格式
    :param start_time: 剪切的起始时间点（第start_time秒）
    :param stop_time: 剪切的结束时间点（第stop_time秒）
    :return:
    """
    validate_file(source_video_abs_path)
    source_video = VideoFileClip(source_video_abs_path)
    video = source_video.subclip(int(start_time), int(stop_time))  # 执行剪切操作
    video.write_videofile(target_video_abs_path)  # 输出文件

def clip_video_hold_end(source_video_abs_path, target_video_abs_path, start_time,stop_time=None):

    clip_video(source_video_abs_path, target_video_abs_path, start_time,stop_time)

def clip_audio(source_file, target_file, start_time, stop_time):
    """
    利用pydub进行音频剪切。pydub支持源文件为 mp4格式，因此这里的输入可以与视频剪切源文件一致
    :param source_file: 原视频的路径，mp4格式
    :param target_file: 生成的目标视频路径，mp4格式
    :param start_time: 剪切的起始时间点（第start_time秒）
    :param stop_time: 剪切的结束时间点（第stop_time秒）
    :return:
    """
    validate_file(source_file)
    audio = AudioSegment.from_file(source_file, "mp4")
    audio = audio[start_time * 1000: stop_time * 1000]
    audio_format = target_file[target_file.rindex(".") + 1:]
    audio.export(target_file, format=audio_format)


def combine_video_audio(video_file, audio_file, target_file, delete_tmp=False):
    """
    利用 ffmpeg将视频和音频进行合成
    :param video_file:
    :param audio_file:
    :param target_file:
    :param delete_tmp: 是否删除剪切过程生成的原视频/音频文件
    :return:
    """
    validate_file(video_file)
    validate_file(audio_file)
    # 注：需要先指定音频再指定视频，否则可能出现无声音的情况
    command = "ffmpeg -y -i {0} -i {1} -vcodec copy -acodec copy {2}".format(audio_file, video_file, target_file)
    print("command:",command)
    os.system(command)
    if delete_tmp:
        os.remove(video_file)
        os.remove(audio_file)


def get_target_video_path(source_video_abs_path):
    # video_dir = os.path.abspath(os.path.join(source_video_abs_path, ".."))
    # print("source_video_abs_path:", source_video_abs_path)
    # start_time = 1
    #
    # # 设置目标文件名
    # target_name = str(start_time) + "s_"
    # target_video_abs_path = os.path.join(video_dir, "clip_" + target_name + ".mp4")
    # print("target_video_abs_path:", target_video_abs_path)
    target_video_abs_path=source_video_abs_path
    return target_video_abs_path

def clip_handle(source_video_abs_path, start_time=1, stop_time=None,tmp_path=None, delete_tmp=True,target_video_abs_path=None):
    """
    将一个视频文件按指定时间区间进行剪切
    :param source_video_abs_path: 原视频文件
    :param target_video_abs_path: 目标视频文件
    :param start_time: 剪切的起始时间点（第start_time秒）
    :param stop_time: 剪切的结束时间点（第stop_time秒）
    :param tmp_path: 剪切过程的文件存放位置
    :param delete_tmp: 是否删除剪切生成的文件
    :return:
    """
    # 设置临时文件名
    if not target_video_abs_path:
        target_video_abs_path=get_target_video_path(source_video_abs_path)
    if tmp_path is None or not os.path.exists(tmp_path):
        # 如果没有指定临时文件路径，则默认与目标文件的位置相同
        tmp_path = target_video_abs_path[: target_video_abs_path.rindex("/") + 1]
    target_file_name = target_video_abs_path[target_video_abs_path.rindex("/") + 1: target_video_abs_path.rindex(".")]
    tmp_video = tmp_path + "v_" + target_file_name + ".mp4"
    tmp_audio = tmp_path + "a_" + target_file_name + ".mp4"
    clip = VideoFileClip(source_video_abs_path)
    video_time=clip.duration
    print("video_time:",video_time)
    if not stop_time:
        stop_time = clip.duration
    elif stop_time>video_time:
        print("传入裁剪视频的结束时间大于视频本身的时间")
        stop_time=video_time
    print("stop_time:", stop_time)
    # 执行文件剪切及合成
    clip_video_hold_end(source_video_abs_path, tmp_video, start_time,stop_time)
    clip_video_hold_end(source_video_abs_path, tmp_audio, start_time,stop_time)
    combine_video_audio(tmp_video, tmp_audio, target_video_abs_path, delete_tmp=delete_tmp)
    return target_video_abs_path


def validate_file(source_file):
    if not os.path.exists(source_file):
        raise FileNotFoundError("没有找到该文件：" + source_file)


def size_convert(size):  # 单位换算
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(size / G) + 'G Bytes'
    elif size >= M:
        return str(size / M) + 'M Bytes'
    elif size >= K:
        return str(size / K) + 'K Bytes'
    else:
        return str(size) + 'Bytes'


def get_img_size(img_filename):
    im=Image.open(img_filename)
    width=im.size[0]
    height=im.size[1]
    return width,height

def crop_img(pic_path, crop_area=[0,0,1,1], reco_type_mark="crop"):
    if crop_area != [0,0,1,1]:
        fp = open(pic_path, 'rb')
        img = Image.open(pic_path)
        width, height = get_img_size(pic_path)
        x1 = crop_area[0] * width
        y1 = crop_area[1] * height
        x2 = crop_area[2] * width
        y2 = crop_area[3] * height
        cropped = img.crop((x1, y1, x2, y2))
        file_name = pic_path.split("/")[-1]
        parentPath = os.path.abspath(os.path.join(pic_path, '..'))
        reco_type_mark_dir = os.path.join(parentPath, reco_type_mark)
        print("reco_type_mark_dir:",reco_type_mark_dir)
        if not os.path.exists(reco_type_mark_dir):
            os.makedirs(reco_type_mark_dir)
        copy_pic_path = os.path.join(reco_type_mark_dir, file_name)
        cropped.save(copy_pic_path)
        fp.close()
        return copy_pic_path
    return pic_path

def crop_img_abs_resolution(pic_path, crop_area, reco_type_mark="crop"):
    if crop_area != []:
        fp = open(pic_path, 'rb')
        img = Image.open(pic_path)
        x1 = crop_area[0]
        x2 = crop_area[1]
        y1= crop_area[2]
        y2 = crop_area[3]
        cropped = img.crop((x1, y1, x2, y2))
        file_name = pic_path.split("/")[-1]
        parentPath = os.path.abspath(os.path.join(pic_path, '..'))
        reco_type_mark_dir = os.path.join(parentPath, reco_type_mark)
        print("reco_type_mark_dir:",reco_type_mark_dir)
        if not os.path.exists(reco_type_mark_dir):
            os.makedirs(reco_type_mark_dir)
        copy_pic_path = os.path.join(reco_type_mark_dir, file_name)
        cropped.save(copy_pic_path)
        fp.close()
        return copy_pic_path
    return pic_path


def get_video_cutter(input_video_path, frame_count = 60 ,frame_parameter='-qscale:v 2 -f image2 -r '):
    '''
    默认是对视频高清拆帧
    '''

    file_name=input_video_path.split("/")[-1].split('.')[0]

    # input_video_path = "records/jingxuan_share_1616064514.mp4"
    file_path = os.getcwd() + '/frames/'+str(frame_count) + '/'
    print("file_path:",file_path )
    dest_dir = file_path + file_name
    print("dest_dir:", dest_dir)

    # 创建目标文件夹，如果之前存在先清除
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    # 对视频进行分帧
    out_pic = "{}/%05d.jpg".format(dest_dir)
    ffmpeg_path = "/usr/local/bin/ffmpeg"
    # ffmpeg_path=os.path.join(os.getcwd(),'ffmpeg')
    # logger.info("ffmpeg_path:" + str(ffmpeg_path))
    # ff = ffmpy3.FFmpeg(executable="/usr/local/ffmpeg/bin/ffmpeg",
    #     inputs={input_video_path: None},
    #     outputs={out_pic: '-r {}'.format(str(frame_count))}
    # )
    videocutter_threads_num = 2
    if '60' in frame_parameter:
        frame_parameter=frame_parameter.replace('60','')
    ff = ffmpy3.FFmpeg(executable=ffmpeg_path,
        inputs={input_video_path: None},
        outputs={out_pic: frame_parameter+str(frame_count)+" -threads "+str(videocutter_threads_num)}
    )
    print("ff.cmd:",ff.cmd)

    ff.run()
    print("拆帧结束")

    return dest_dir

if __name__ == "__main__":
    dest_dir=get_video_cutter(input_video_path='/Users/xh/Downloads/爱奇艺.mp4')
    print("dest_dir:",dest_dir)





