# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 17:14
# @Author  : 王梦汉
# @Site    :
# @File    : message_create_group.py
# @Software: PyCharm
import time

from krunner.core.base import ImgElement
from krunner.core.ios.element import BaseElement, Window, IosElement
from krunner.utils import logger

from pageobjects.ios.messages.message_list import ListMessage

class CreateGroupMessage(object):
    '''群聊-聊天信息页'''
    group_limit = BaseElement(name='已达建群上限', desc='当群建满时')
    choose_group = BaseElement(name='选择一个群', desc='发私信页')
    exit_group = BaseElement(name='退出并解散本群', desc='聊天信息页')
    exit_disband = BaseElement(name='退出并解散', desc='底部弹框')
    start_create = BaseElement(name='开始创建', desc='建群')
    industry_talk = BaseElement(name='行业交流', desc='选择群分类页')
    add_group_head = BaseElement(name='添加群头像', desc='编辑群资料')
    taking_picture = BaseElement(name='拍一张', desc='拍照')
    camera_picture = BaseElement(label="从相册选取", annotation="从相册选取")
    flip_lens = BaseElement(name='FrontBackFacingCameraChooser', desc='翻转镜头')
    shooting = BaseElement(name='PhotoCapture', desc='拍照')
    use_picture = BaseElement(name='使用照片', desc='使用照片')
    group_name = IosElement(xpath='//*[@label=""]', annotation='点击群名')
    group_address = BaseElement(nameContains='群地点', desc='点击群地点')
    group_address_ocr = ImgElement(template='群地点', desc='点击群地点')
    group_introduce = BaseElement(name='群介绍', desc='点击群介绍')
    write_group_introduce = BaseElement(name='填写群介绍，吸引更多人加入', desc='填写群介绍')
    submit_btn = BaseElement(name='提交', desc='点击提交按钮')
    group_manager = BaseElement(name='群主', desc='检查群主是否存在')
    group_classification = BaseElement(name='群分类', desc='检查群分类是否存在')
    group_place = BaseElement(name='群地点', desc='检查群地点是否存在')
    average_age = BaseElement(name='平均年龄', desc='检查平均年龄是否存在')
    editor_group_data = BaseElement(name='编辑群资料', desc='检查编辑群资料是否存在')
    group_management = BaseElement(name='群管理', desc='点击群管理按钮')
    administrator_number = IosElement(xpath='//*[@label="管理员(0/5)"]', desc='获取管理员数量')
    add_administrator = BaseElement(name='添加管理员', desc='点击添加管理员按钮')
    group_members_number = BaseElement(nameContains='群成员', desc='获取群成员数量')
    choose_friend1 = IosElement(xpath=('//Table/Cell[1]/Image[1]'), annotation='选择好友1')
    choose_friend2 = IosElement(xpath=('//Table/Cell[2]/Image[1]'), annotation='选择好友2')
    choose_friend3 = IosElement(xpath=('//Table/Cell[3]/Image[1]'), annotation='选择好友3')
    complete_btn = IosElement(label='完成', annotation='完成btn')
    choose_group_members = IosElement(xpath=('//Table/Cell[1]/Image[1]'), annotation='选择群成员')
    add_successful = BaseElement(name='添加成功', desc='添加成功toast')
    remove_successful = BaseElement(name='移出成功', desc='移出成功toast')
    remove_btn = BaseElement(xpath='//NavigationBar/Button[2]/StaticText[1]', desc='移出btn')
    group_works_switch = BaseElement(xpath='//Table/Cell[3]/Switch[1]', desc='不允许分享作品开关')
    return_btn = BaseElement(name='common nav back black', desc='右上角返回按钮')
    sharing_works_text = IosElement(xpath=('//*[@label="你已开启不允许群成员分享自己的作品"]/Other[1]'), annotation='你已开启不允许群成员分享自己的作品')
    close_sharing_works_text = IosElement(xpath=('//*[@label="你已关闭不允许群成员分享自己的作品"]/Other[1]'),annotation='你已关闭不允许群成员分享自己的作品')
    members_addgroup_switch = BaseElement(xpath='//Table/Cell[5]/Switch[1]', desc='允许群成员邀请加群')
    add_group_way = BaseElement(name='加群方式', desc='加群方式按钮')
    setup_addgroup_switch1 = BaseElement(name='需要审批', desc='设置加群方式')
    setup_addgroup_switch2 = BaseElement(name='无需审批直接加群', desc='设置加群方式')
    groupmembers_banned_switch = BaseElement(xpath='//Table/Cell[4]/Switch[1]', desc='群成员禁言')
    open_group_banned_text = IosElement(xpath=('//*[@label="本群已开启群成员禁言，只允许群主和管理员发言"]/Other[1]'), annotation='开启群成员禁言')
    close_group_banned_text = IosElement(xpath=('//*[@label="本群已关闭群成员禁言"]/Other[1]'),annotation='关闭群成员禁言')
    group_announcement = BaseElement(name='群公告', desc='群公告btn')
    key_copy = BaseElement(name='一键复制', desc='一键复制btn')
    editor_btn = BaseElement(name='编辑', desc='编辑btn')
    published = BaseElement(name='已发布', desc='已发布')
    addgroup_threshold = BaseElement(name='加群门槛', desc='加群门槛btn')
    setup_addgroup_threshold_text = BaseElement(name='设置加群门槛', desc='设置加群门槛btn')
    filter_btn1 = BaseElement(name='过滤互粉互赞用户', desc='过滤互粉互赞用户btn')
    filter_btn2 = BaseElement(name='过滤没有关注群主的用户', desc='过滤没有关注群主的用户btn')
    filter_btn3= BaseElement(name='过滤不是群主真爱粉的用户', desc='过滤不是群主真爱粉的用户btn')
    profile_showgroup_switch = BaseElement(xpath='//Table/Cell[10]/Switch[1]', desc='个人主页展示群开关')
    group_report_btn = BaseElement(name='群举报', desc='群举报btn')
    content_btn = IosElement(xpath=('//*[@label="群名、群头像、群简介、群公告"]'), desc='content')
    message_not_disturb_switch = IosElement(xpath=('//Table/Cell[8]/Switch[1]'), desc='消息免打扰btn')
    top_chat_switch = IosElement(xpath=('//Table/Cell[9]/Switch[1]'), desc='置顶聊天btn')
    empty_chatcontent_btn = BaseElement(name='清空聊天内容', desc='清空聊天内容btn')
    confirm_empty_bounced = BaseElement(name='确认要清空所有聊天内容吗？', desc='确认清空弹框')
    confirm_btn = BaseElement(label="确认", index=0)
    # beijing_text = BaseElement(label="北京市", index=0)  #经常报wda.exceptions.WDAStaleElementReferenceError错误
    beijing_text = ImgElement(template='北京市')
    camera_permission_text = BaseElement(labelContains="允许进入快手内读取和写入相册内容及属性信息")
    camera_permission_text1 = BaseElement(labelContains="访问您的相机")
    permisson_no_btn = BaseElement(label="不允许", index=0)
    permisson_yes_btn = BaseElement(label="好", index=0)
    known_btn = BaseElement(label="知道了", index=0)
    picture_permission_text = BaseElement(labelContains="想访问您的照片", annotation="相册权限上的弹窗title")
    permission_later_btn = BaseElement(label="以后再说", index=0, annotation="弹窗上的以后再说")
    allow_read_pics=BaseElement(label="允许访问所有照片")
    permisson_setting_btn = BaseElement(label="设置", index=0, annotation="弹窗上的设置")
    allow_one=BaseElement(label="允许一次", index=0)
    protocol_icon=ImgElement(category='checkbox', desc='用户协议checkbox')

    def create_group(self):
        '''点击+，创建群聊'''
        time.sleep(1)
        lmsg=ListMessage()
        lmsg.click_more_btn()

        if lmsg.create_group_btn.exist(alert_watcher=False):
            logger.info("当前页面存在创建群聊")
            lmsg.create_group_btn.click(alert_watcher=False)
        else:
            logger.info("当前页面不存在创建群聊")
            lmsg.more_btn.click(alert_watcher=False)
            lmsg.create_group_btn.click(alert_watcher=False)

    def create_group1(self):
        '''点击+，创建群聊'''
        time.sleep(1)
        lmsg = ListMessage()
        lmsg.click_more_btn()



    def group_upper_limit(self):
        '''当群建满时，删除已有群聊再继续创建'''
        while(self.group_limit.exist()):
            Window().tap_by_screen_percent(0.083, 0.064)
            lmsg = ListMessage()
            lmsg.more_btn.click()
            lmsg.send_message_btn.click()
            self.choose_group.click()
            Window().tap_by_screen_percent(0.408, 0.293)
            Window().tap_by_screen_percent(0.806, 0.058)
            lmsg.more_btn.click()
            Window().swipe_up()
            self.exit_group.click()
            self.exit_disband.click()
            self.create_group()

    def create_group_process(self):
        '''创建群聊流程'''
        lmsg = ListMessage()
        self.start_create.click()
        self.industry_talk.click()
        self.add_group_head.click()
        self.taking_picture.click()
        self.flip_lens.click()
        self.shooting.click()
        self.use_picture.click()
        Window().tap_by_screen_percent(0.936, 0.066)
        self.group_name.input_text('textGroup')
        self.group_address.click()
        Window().tap_by_screen_percent(0.449, 0.334)
        Window().tap_by_screen_percent(0.063, 0.053)
        self.group_introduce.click()
        self.write_group_introduce.input_text('This is a test group!')
        self.complete_btn.click()
        Window().tap_by_screen_percent(0.792, 0.846)
        Window().tap_by_screen_percent(0.806, 0.058)
        lmsg.more_btn.click()
        Window().swipe_up()
        self.exit_group.click()
        self.exit_disband.click()

    def check_group_profile(self):
        '''检查群profile页'''
        lmsg = ListMessage()
        lmsg.more_btn.click()
        lmsg.send_message_btn.click()
        self.choose_group.click()
        Window().tap_by_screen_percent(0.408, 0.293)
        Window().tap_by_screen_percent(0.806, 0.058)
        lmsg.more_btn.click()
        Window().tap_by_screen_percent(0.132, 0.158)

    def check_group_management(self):
        '''检查群管理'''
        cgm=CreateGroupMessage()
        cgm.check_group_members()
        self.group_management.click()
        Window().tap_by_screen_percent(0.129, 0.215)
        if self.administrator_number.exist():
            cgm.add_group_members()
            cgm.remove_group_members()
            assert self.remove_successful.exist()
        else:
            cgm.remove_group_members()
            cgm.add_group_members()
            assert self.add_successful.exist()

    def add_group_members(self):
        '''添加群成员'''
        self.add_administrator.click()
        self.choose_group_members.click()
        self.complete_btn.click()

    def remove_group_members(self):
        '''移除群成员'''
        self.remove_btn.click()
        self.choose_group_members.click()
        self.remove_btn.click()

    def check_group_members(self):
        '''检查群成员页'''
        lmsg = ListMessage()
        lmsg.more_btn.click()
        lmsg.send_message_btn.click()
        self.choose_group.click()
        Window().tap_by_screen_percent(0.408, 0.293)
        Window().tap_by_screen_percent(0.806, 0.058)
        lmsg.more_btn.click()
        if(self.group_members_number.info['text']=="群成员(1/200)"):
            Window().tap_by_screen_percent(0.299, 0.344)
            self.choose_friend1.click()
            self.choose_friend2.click()
            self.choose_friend3.click()
            self.complete_btn.click()

    def enter_group_management(self):
        '''进入群管理页'''
        cgm = CreateGroupMessage()
        cgm.enter_chatmessage_page()
        self.group_management.click()

    def enter_chatmessage_page(self):
        '''进入群聊天页'''
        lmsg = ListMessage()
        lmsg.more_btn.click()
        lmsg.send_message_btn.click()
        self.choose_group.click()
        Window().tap_by_screen_percent(0.408, 0.293)
        Window().tap_by_screen_percent(0.806, 0.058)
        lmsg.more_btn.click()

    def editor_group_announcement(self):
        '''编辑群公告'''
        self.group_announcement.click()
        if self.editor_btn.exist():
            self.editor_btn.click()
            self.key_copy.click()
            self.complete_btn.click()
            assert self.published.exist()
        else:
            self.key_copy.click()
            self.complete_btn.click()
            assert self.published.exist()

    def setting_works_switch(self):
        '''设置不允许群成员分享自己的作品开关'''
        switch1 = self.group_works_switch.info['value']
        self.group_works_switch.click()
        switch2 = self.group_works_switch.info['value']
        assert switch1 != switch2

    def setting_addgroup_switch(self):
        '''设置允许群成员邀请好友加群开关'''
        if self.members_addgroup_switch.info['value']== '0':
            self.members_addgroup_switch.click()
            assert self.members_addgroup_switch.info['value']== '1'
        else:
            self.members_addgroup_switch.click()
            assert self.members_addgroup_switch.info['value']== '0'

    def setup_addgroup_way(self):
        '''设置加群方式'''
        if self.setup_addgroup_switch1.exist():
            self.setup_addgroup_switch1.click()
            self.setup_addgroup_switch2.click()
            self.complete_btn.click()
            assert self.setup_addgroup_switch2.info['text'] == "无需审批直接加群"
        else :
            self.setup_addgroup_switch2.click()
            self.setup_addgroup_switch1.click()
            self.complete_btn.click()
            assert self.setup_addgroup_switch1.info['text'] == "需要审批"

    def setup_addgroup_threshold(self):
        '''设置加群门槛'''
        self.addgroup_threshold.click()
        self.filter_btn1.click()
        self.filter_btn2.click()
        self.filter_btn3.click()
        self.complete_btn.click()
        assert not self.setup_addgroup_threshold_text.exist()

    def setup_group_banned(self):
        '''设置群成员禁言开关'''
        switch1 = self.groupmembers_banned_switch.info['value']
        self.groupmembers_banned_switch.click()
        switch2 = self.groupmembers_banned_switch.info['value']
        assert switch1 != switch2

    def profile_show_group(self):
        '''个人主页展示该群'''
        Window().swipe_up()
        switch1 = self.profile_showgroup_switch.info['value']
        self.profile_showgroup_switch.click()
        switch2 = self.profile_showgroup_switch.info['value']
        assert switch1 != switch2

    def group_report(self):
        '''测试群举报'''
        Window().swipe_up()
        self.group_report_btn.click()
        Window().tap_by_screen_percent(0.428, 0.406)
        self.content_btn.click()
        self.submit_btn.click()
        assert self.complete_btn.exist()

    def message_not_disturb(self):
        '''测试消息免打扰开关'''
        Window().swipe_up()
        switch1 = self.message_not_disturb_switch.info['value']
        self.message_not_disturb_switch.click()
        switch2 = self.message_not_disturb_switch.info['value']
        assert switch1 != switch2

    def top_chat(self):
        '''测试置顶聊天开关'''
        switch1 = self.top_chat_switch.info['value']
        self.top_chat_switch.click()
        switch2 = self.top_chat_switch.info['value']
        assert switch1 != switch2

    def empty_chat_content(self):
        '''测试清空聊天内容'''
        self.empty_chatcontent_btn.click()
        assert not self.confirm_empty_bounced.exist()

    def check_is_exist(self):
        '''校验元素是否存在'''
        lmsg = ListMessage()
        if lmsg.more_btn.exist():
            return True
        else:
            return False

    def check_enter_pofile(self):
        ''''检查是否进入群profile页'''
        return self.group_classification.exist() and self.group_manager.exist() and self.average_age.exist() and self.editor_group_data.exist()


    def check_location_popup(self):
        '''检查定位服务服务弹窗'''
        return BaseElement(label="开启定位服务").exist(alert_watcher=False) and BaseElement(label="以后再说").exist(alert_watcher=False) and BaseElement(label="确认").exist(alert_watcher=False)

    def check_camera_popup(self):
        '''检查相机权限弹窗'''
        return (self.camera_permission_text.exist(alert_watcher=False) or self.camera_permission_text1.exist(alert_watcher=False))

    def check_picture_popup(self):
        '''检查相册权限'''
        return self.picture_permission_text.exist(alert_watcher=False) and self.permission_later_btn.exist(alert_watcher=False)