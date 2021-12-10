"""
手机淘论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests
import os
from sys import argv
import re

import config
from utils.serverchan_push import push_to_wechat

import logging
from bot.base_bot import Base_Bot

class SHHUU_Bot(Base_Bot):
    """
    手机淘
    """

    def checkin(self):
        """
        签到函数
        """
        url = "http://www.shhuu.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
        payload='formhash=58ec4a84&qdxq=kx&qdmode=2&todaysay=&fastreply=0'
        msg = self.session.post(url=url, data=payload)
        data = msg.content.decode('gbk')
        #  校验结果是否正确
        pattern = re.compile('恭喜你签到成功!获得随机奖励\s+购机币\s+(\d+)\s+')
        mn = re.search(pattern, data)
        res = {'error_code':0}
        if mn:
            logging.info('签到成功,获得购机币 '+ mn.group(1) )
        else:
            pattern = re.compile('您今日已经签到，请明天再来！')
            mn = re.search(pattern, data)
            if mn:
                logging.info('今日已签到！')
                return res
            logging.error(data)
            res = {'error_code':-1,'error_msg':'手机淘签到失败'}
        return res