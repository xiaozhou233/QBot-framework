NAME = '[test]' #你的插件名字
VERSION = 'Beta 0.1' #你的插件版本

import plugins.send_msg as send_msg #你需要引入的库/文件

def start():
    ### 这里是初始化部分 ###
    return f"{NAME} Started. Version: {VERSION}"
    ### 这里是初始化部分 ###

def trigger(msg):
    ### 这里是你的代码 ###
    List = ['测试','test'] #关键词
    if msg['message'] in List: #判断对话里是否有关键词
    ### 这里是初始化部分 ###
        
