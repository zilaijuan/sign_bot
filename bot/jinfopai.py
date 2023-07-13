#!/usr/local/bin/python
"""
金灵异论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""

from sys import argv
import re


from utils.serverchan_push import push_to_wechat

import logging
from bot.base_bot import Base_Bot
import config

class JINFOPAI_Bot(Base_Bot):
    """
    金灵异
    """

    def checkin(self):
        """
        登陆
        """
        msg = self.session.get("http://www.jinfopai.com/")
        content = msg.content.decode('gbk',errors='ignore')
        self.save_cookies(self.session.cookies,'a.txt')
        """
        获取formhash
        """
        pattern = re.compile('formhash=(.*)\"')
        mn = re.search(pattern, content)
        formhash = ''
        if mn:
            formhash =  mn.group(1)
        else:
            self.log.error('formhash查找不到')
            res = {'error_code':-1,'error_msg':'formhash查找不到'}
            return res
        """
        签到函数
        """
        url = "http://www.jinfopai.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
        payload='formhash=%s&qdxq=kx&qdmode=2&todaysay=&fastreply=0' %(formhash)
        msg = self.session.post(url=url, data=payload)
        data = msg.content.decode('gbk')
        #  校验结果是否正确
        pattern = re.compile('恭喜你签到成功!.*获得随机奖励\s+灵异币\s+(\d+)\s+')
        mn = re.search(pattern, data)
        res = {'error_code':0}
        if mn:
            self.log.info('签到成功,获得灵异币 '+ mn.group(1) )
        else:
            pattern = re.compile('您今日已经签到，请明天再来！')
            mn = re.search(pattern, data)
            if mn:
                self.log.info('今日已签到！')
                return res
            self.log.error(data)
            res = {'error_code':-1,'error_msg':'金灵异签到失败'}
        return res