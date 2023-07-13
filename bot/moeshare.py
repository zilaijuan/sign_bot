#!/usr/local/bin/python
"""
萌享论坛自动签到脚本
"""

from sys import argv
import re


from utils.serverchan_push import push_to_wechat

import logging
from bot.base_bot import Base_Bot
import config
import time
import gzip

class MOESHARE_Bot(Base_Bot):
    """
    萌享漫画
    """

    def checkin(self):
        """
        登陆
        """
        msg = self.session.get("https://www.moeshare.cc/")
        content = msg.content.decode('utf8',errors='ignore')
        
        """
        获取formhash
        """
        pattern = re.compile('var verifyhash = \'(.*?)\'')
        mn = re.search(pattern, content)
        formhash = ''
        if mn:
            formhash =  mn.group(1)
        else:
            self.log.error('verifyhash查找不到')
            res = {'error_code':-1,'error_msg':'verifyhash查找不到'}
            return res

        """
        签到函数
        """
        nowtime = int(time.time() * 1000)
        url = "https://www.moeshare.cc/jobcenter.php?action=punch&verify=%s&nowtime=%s&verify=%s" %(formhash,nowtime,formhash)
        payload={'step':'2'} 
        msg = self.session.post(url=url, data=payload)
        data = msg.content.decode('utf8',errors='ignore')
        
        # print(data)
        
        #  校验结果是否正确
        pattern = re.compile('获得\s+(\d+)MB.*flag.*1')
        mn = re.search(pattern, data)
        res = {'error_code':0}
        if mn:
            self.log.info('签到成功,获得漫画 '+ mn.group(1) )
        else:
            pattern = re.compile('你已经打卡,请明天再试')
            mn = re.search(pattern, data)
            if mn:
                self.log.info('今日已签到！')
                return res
            self.log.error(data)
            res = {'error_code':-1,'error_msg':'萌享签到失败'}
        return res