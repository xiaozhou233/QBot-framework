###     INFO      ###
# Author: 筱周 
# Model: pluginLoader
# Description: 插件加载器


#多久没碰的代码了...能跑就行，不注释了(?)

NAME = '[Log_record]'
VERSION = "0.1"


import logging as log
import sys
from datetime import datetime

def start_log_record():
    formatted_time = datetime.now().strftime("%Y_%m_%d")
    log.basicConfig(filename=f'./logs/{formatted_time}.log', filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=log.INFO)

    console_handler = log.StreamHandler(sys.stdout)
    console_handler.setLevel(log.DEBUG)
    console_formatter = log.Formatter("%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    console_handler.setFormatter(console_formatter)

    # 将处理器添加到日志记录器
    log.getLogger('').addHandler(console_handler)

    log.info(f"{NAME} Started.")
