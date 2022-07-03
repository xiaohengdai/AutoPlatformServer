import os
import shutil

import ffmpy3

from app.util.img_video_controller import ImgVideoController

#-gscale:v 2 -f image2

def video_cutter(input_video_path,frame_rate=30,frame_parameter=' -r ',videocutter_threads_num=1):
    file_name=input_video_path.split("/")[-1]
    frame_dir=os.path.join(os.getcwd(),"frames")
    if not os.path.exists(frame_dir):
        os.mkdir(frame_dir)
    file_path=os.path.join(frame_dir,str(frame_rate))
    dest_dir=os.path.join(file_path,file_name)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    out_pic="{}/%05d.jpg".format(dest_dir)
    out_pic_cmd=frame_parameter+str(frame_rate)+" -threads "+str(videocutter_threads_num)
    print("out_pic_cmd:",out_pic_cmd)
    ff=ffmpy3.FFmpeg(executable="/usr/local/bin/ffmpeg",inputs={input_video_path:None},outputs={out_pic:None})
    ff.run()
    return  dest_dir



def video_cutter_to_save_to_internet(input_video_path,frame_rate=30,frame_parameter=' -r ',type=0):
    videocutter_frame_path=video_cutter(input_video_path=input_video_path,frame_rate=frame_rate,frame_parameter=frame_parameter)
    if type==1:#复制到vue目录
        local_vue_img_path = os.path.join('/Users/xiaoheng/Downloads/xiaoheng/vue-manage-system/src/assets/img',
                                          videocutter_frame_path.split('/')[-1])
        shutil.copytree(videocutter_frame_path, local_vue_img_path)
        videocutter_frame_path=local_vue_img_path
    all_file_list=os.listdir(videocutter_frame_path)
    all_file_list.sort()
    videocutter_frame_pic_num=len(all_file_list)
    pic_path=os.path.join(videocutter_frame_path,all_file_list[0])

    frame_pic_set=[]
    for i in range(0,len(all_file_list)):
        frame_pic_path=os.path.join(videocutter_frame_path,all_file_list[i])
        img_video_controller=ImgVideoController(frame_pic_path)
        img_video_controller.put_stream(open(frame_pic_path,'rb'))
        image_url=img_video_controller.get()
        frame_pic_set.append(image_url)
    return pic_path,videocutter_frame_path,frame_pic_set