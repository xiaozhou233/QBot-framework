###     INFO      ###
# Author: 筱周 
# Model: main
# Description:程序的入口

#引入外部库
import asyncio
import json
import websockets

#pluginLoader.py等文件
import config_qbot
import pluginLoader
import log_recoeder

#开始日志记录
log_recoeder.start_log_record()

#开始加载插件
pluginLoader.load_plugins()
from pluginsList import *

#获得插件列表
obj_plugins = [globals()[item] for item in pluginLoader.get_all_plugins()]

#允许判断的消息
allow_message = ['group', 'private']

async def handle_message(websocket, path):
    async for message in websocket:
        #将json数据加载成msg列表
        msg = json.loads(message)
        #如果消息类似在allow_message列表里
        if msg.get('message_type') in allow_message:
            #传输msg列表给每一个插件的trigger (触发器)
            for pluginObj in obj_plugins:
                pluginObj.trigger(msg)

            #输出Q群号、发送的用户信息及内容
            log.info(f"UserSendMsg: [{msg['group_id']}] {msg['sender']['nickname']}({msg['user_id']}): {msg['message']}")

#创建一个websockets服务器，和go-cqhttp的反向websockets连接获取信息,IP和端口在config_qbot.py文件修改
start_server = websockets.serve(handle_message, config_qbot.WebSocketsIP, config_qbot.WebSocketsPort)

#输出启动信息
print(f"Started Server. at {config_qbot.WebSocketsIP}:{config_qbot.WebSocketsPort}")


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

