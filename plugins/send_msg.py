###     INFO      ###
# Author: 筱周 
# Model: send_msg
# Description: 发送消息的插件



NAME = "[send_msg]"
VERSION = "2.0"

import requests

HttpAPI = "http://localhost:5700"

def start():
    return f"{NAME} Started. Version: {VERSION}"

def trigger(msg):
    return 0


def http_get(url, params):
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    else:
        return f"请求失败：{response.status_code}"

def http_get_not_json(url, params):
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.text
    else:
        return f"请求失败：{response.status_code}"

def send_group_msg(group_id, message, auto_escape):
    params = {
    "group_id": group_id,
    "message": message,
    "auto_escape": auto_escape
    }
    return http_get(HttpAPI+"/send_group_msg", params)

