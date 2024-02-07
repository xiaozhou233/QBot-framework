###     INFO      ###
# Author: 筱周 
# Model: pluginLoader
# Description: 插件加载器


NAME = '[PluginsLoader]'
VERSION = "0.1 - test.ver"


import os

def get_all_plugins():
    #初始化列表
    all_plugins = []

    for root, dirs, files in os.walk('./plugins'):
        # 遍历每个文件
        for file in files:
            # 判断文件扩展名是否为 .py
            if file.endswith('.py'):
                # 将文件名加入到列表里
                all_plugins.append(file[:-3])
    #返回全部插件
    return all_plugins

print(get_all_plugins())

#加载插件
def load_plugins():
    #获得全部插件名
    all_plugins = get_all_plugins()

    with open('pluginsList.py', 'w+') as f:
        # 循环遍历文件名列表
        f.write("from log_recoeder import *\n")
        for file_name in all_plugins:
            # 写入 import 语句到 pluginsLoader.py 文件
            f.write(f"import plugins.{file_name} as {file_name}\nlog.info({file_name}.start())\n")
    print(f"{NAME} 插件列表:{all_plugins}")

    #每运行一次更新pluginsList.py文件
    #在main.py文件里使用from pluginsList import *就可以加载全部插件
