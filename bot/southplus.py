#!/usr/local/bin/python
"""
南加论坛自动签到脚本
"""

from sys import argv
import re


from utils.serverchan_push import push_to_wechat
from bs4 import BeautifulSoup
import logging
from bot.base_bot import Base_Bot
import config
import time
import gzip

class SOUTHPLUS_Bot(Base_Bot):
    """
    南加论坛
    """

    def checkin(self):
        """
        申请任务
        """
        msg = self.session.get("https://south-plus.org/plugin.php?H_name-tasks.html")
        content = msg.content.decode('utf8',errors='ignore')
        taskListBS = BeautifulSoup(content,"html.parser")
        jobs = taskListBS.select(".t table tr span a")
        for job in jobs:
            pattern = re.compile('startjob\(\'(\d+)\'\)\;')
            mn = re.search(pattern, job["onclick"])
            if mn:
                jobId = mn.group(1)
                jobUrl = 'https://south-plus.org/plugin.php?H_name=tasks&action=ajax&actions=job&cid='+jobId
                msg = self.session.get(jobUrl)
                content = msg.content.decode('utf8',errors='ignore')
                print(content)
        """
        领取任务奖励
        """
        msg = self.session.get("https://south-plus.org/plugin.php?H_name-tasks-actions-newtasks.html.html")
        content = msg.content.decode('utf8',errors='ignore')
        taskListBS = BeautifulSoup(content,"html.parser")
        jobs = taskListBS.select(".t table tr span a")
        for job in jobs:
            pattern = re.compile('startjob\(\'(\d+)\'\)\;')
            mn = re.search(pattern, job["onclick"])
            if mn:
                jobId = mn.group(1)
                jobUrl = 'https://south-plus.org/plugin.php?H_name=tasks&action=ajax&actions=job2&cid='+jobId
                msg = self.session.get(jobUrl)
                content = msg.content.decode('utf8',errors='ignore')
                print(content)
        
        
        res = {'error_code':0}
        
        return res