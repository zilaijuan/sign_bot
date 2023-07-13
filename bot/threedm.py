#!/usr/local/bin/python
"""
3dm论坛自动签到脚本
"""

from random import Random
from sys import argv
import re


from utils.serverchan_push import push_to_wechat
from bs4 import BeautifulSoup
import logging
from bot.base_bot import Base_Bot
import config
import time
import gzip
import random

class THREEDM_Bot(Base_Bot):
    """
    南加论坛
    """

    baseUrl="https://bbs.3dmgame.com/"

    def checkin(self):
        """
        申请任务
        """
        msg = self.session.get(self.baseUrl+"home.php?mod=task")
        content = msg.content.decode('utf8',errors='ignore')
        taskListBS = BeautifulSoup(content,"html.parser")
        trs = taskListBS.select(".ptm table tr")
        res = {'error_code':-1,'error_msg':'3dm签到失败'}
        for tr in trs:
            td = tr.find_all("td")[3]
            taskApply = td.a["href"]
            pattern = re.compile('id=(\d+)')
            mn = re.search(pattern, taskApply)
            if mn:
                taskId = mn.group(1)
            if taskApply != "javascript:;":
                self.log.info("找到一个任务，{}".format(taskApply))
                res = self.process(taskId)
        return res
    def process(self, taskId):
        postUrl = self.getTaskPost(taskId)
        if len(postUrl) <=0:
            self.log.warn("未找到任务完成指南, id:{}".format(taskId))
            return {'error_code':-2,'error_msg':'3dm未找到任务完成指南'} 
        # 申请任务
        if not self.doApply(taskId):
            return {'error_code':-2,'error_msg':'3dm申请任务失败'} 
        # 完成任务
        if self.doTask(postUrl):
            """
            领取任务奖励
            """
            self.getReward(taskId)
        return  {'error_code':0}       
    def getTaskPost(self, taskId):
        taskUrl = "home.php?mod=task&do=view&id={}".format(taskId)
        msg = self.session.get(self.baseUrl+taskUrl)
        content = msg.content.decode('utf8',errors='ignore')
        taskDetailsBS = BeautifulSoup(content,"html.parser")
        #ct > div.mn > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > table
        post = taskDetailsBS.select("table table td.bbda a")
        if len(post)==1:
            return post[0]["href"]
        elif len(post) ==2:
            preTaskUrl = post[1]["href"]
            if not self.checkPreTask(preTaskUrl):
                self.log.info("前置任务未完成，{}".format(preTaskUrl))
                pattern = re.compile('id=(\d+)')
                mn = re.search(pattern, preTaskUrl)
                if mn:
                    taskId = mn.group(1)
                    self.process(taskId)
            return post[0]["href"]
        return ""
    
    def checkPreTask(self, taskUrl):
        self.log.info("检查前置任务，taskUrl:{}".format(taskUrl))
        msg = self.session.get(self.baseUrl+taskUrl)
        content = msg.content.decode('utf8',errors='ignore')
        pattern = re.compile('完成于(.*)后可以再次申请')
        mn = re.search(pattern, content)
        if mn:
            return True
        return False

    def doApply(self, taskId):
        self.log.info("申请任务，id:{}".format(taskId))
        taskApply = "home.php?mod=task&do=apply&id={}".format(taskId)
        msg = self.session.get(self.baseUrl+taskApply)
        content = msg.content.decode('utf8',errors='ignore')
        
        pattern = re.compile('申请此任务需要先完成另一个任务，任务页面跳转中请稍候')
        mn = re.search(pattern, content)
        if mn:
            self.log.error("任务申请失败，3dm出现bug。")
            return False
        return True

    def doTask(self, postUrl):
        pattern = re.compile('home\.php\?mod\=task\&do\=view')
        mn = re.search(pattern, postUrl)
        if mn:
            self.log.info("当前task无需回复帖子")
            return True
        self.log.info("开始回复帖子。。。。")
        maxTry = 5
        successCount = 0
        while(maxTry>0):
            res = self.doReply(postUrl)
            if res:
                successCount = successCount +1
            if successCount>=3:
                return True
            sleepTime = 30+random.randint(1,10)
            self.log.info("sleep {} sec".format(sleepTime))
            maxTry = maxTry-1
            if maxTry>0:
                time.sleep(sleepTime)
        return False

    def doReply(self, postUrl):
        msg = self.session.get(self.baseUrl+postUrl)
        content = msg.content.decode('utf8',errors='ignore')
        postBS = BeautifulSoup(content,"html.parser")
        form = postBS.select_one("form#fastpostform")
        inputs = form.select("input")
        params={}
        for input in inputs:
            if input.has_attr("name"):
                params[input['name']] = input['value']
        params['message'] = '每日签到'
        actionUrl = form['action']
        msg = self.session.post(actionUrl+"&inajax=1",params)
        content = msg.content.decode('utf8',errors='ignore')
        pattern = re.compile('非常感谢，回复发布成功')
        mn = re.search(pattern, content)
        if mn:
            return True
        return False
    def getReward(self, taskId):
        rewardUrl = "home.php?mod=task&do=draw&id={}".format(taskId)
        msg = self.session.get(self.baseUrl+rewardUrl)
        content = msg.content.decode('utf8',errors='ignore')
        pattern = re.compile('恭喜您，任务已成功完成，您将收到奖励通知，请注意查收')
        mn = re.search(pattern, content)
        if mn:
            self.log.info("task id: {}, 任务已成功完成".format(taskId))

