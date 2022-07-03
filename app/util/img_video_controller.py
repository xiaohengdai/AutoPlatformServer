class ImgVideoController:
    def __init__(self,img_video_local_path):
        self.img_video_local_path=img_video_local_path
        self.file_stream=''

    def put(self):
        with open(self.img_video_local_path,'rb') as f:
            self.file_stream=f.read()

    def put_stream(self,file_stream):
        self.file_stream=file_stream

    def get(self):
        return self.img_video_local_path

    def get_origin_file(self):
        if len(self.file_stream)==0:
            with open(self.img_video_local_path,'rb') as f:
                self.file_stream=f.read()
        return self.file_stream

    def save_img_byte_flow_to_img(self,img_byte_flow,local_img_path):
        with open(local_img_path,'wb') as saveFp:
            saveFp.write(img_byte_flow)

    def abs_path_img_to_url(self):
        return self.img_video_local_path