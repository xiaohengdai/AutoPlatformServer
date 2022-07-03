import shutil,os

videocutter_frame_path='/Users/xiaoheng/Downloads/meituan/AutoPlatformServer/frames/30/2022_07_03_15_18_23.mp4'
local_vue_img_path=os.path.join('/Users/xiaoheng/Downloads/xiaoheng/vue-manage-system/src/assets/img',videocutter_frame_path.split('/')[-1])

shutil.copytree(videocutter_frame_path, local_vue_img_path)