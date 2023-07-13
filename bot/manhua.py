#!/usr/local/bin/python
"""
漫画补档论坛自动签到脚本
"""

from sys import argv
import re


from utils.serverchan_push import push_to_wechat

import logging
from bot.base_bot import Base_Bot
import config
import time
import gzip

class MANHUA_Bot(Base_Bot):
    """
    漫画补档
    """

    def checkin(self):
        """
        登陆
        """
        msg = self.session.get("https://www.manhuabudang.com/")
        content = msg.content.decode('gbk',errors='ignore')
        
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
        url = "https://www.manhuabudang.com/jobcenter.php?action=punch&verify=%s&nowtime=%s&verify=%s" %(formhash,nowtime,formhash)
        payload={'step':'2'} 
        msg = self.session.post(url=url, data=payload)
        data = msg.content.decode('gbk')
        
        # print(data)
        
        #  校验结果是否正确
        pattern = re.compile('漫画\+(\d+).*flag.*1')
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
            res = {'error_code':-1,'error_msg':'漫画补档签到失败'}
        return res