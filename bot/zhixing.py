"""
知行论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""

from sys import argv
import re
import config

from utils.serverchan_push import push_to_wechat

import logging
from bot.base_bot import Base_Bot

class ZHIXING_Bot(Base_Bot):
    """
    知行
    """

    def checkin(self):
        """
        首页登陆
        """
        msg = self.session.get("https://zhixing.bjtu.edu.cn/")        

        """
        签到函数
        """
        msg = self.session.get("https://zhixing.bjtu.edu.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=a8ba1df3&format=empty&inajax=1&ajaxtarget=JD_sign")
        
        """
        红包
        """
        url = "https://zhixing.bjtu.edu.cn/plugin.php?id=luckypacket&module=ajax&action=get&getsubmit=yes"
        payload='packetid=2'
        self.session.headers = config.ZHIXING__LUCKYPACKET__HEADERS
        msg = self.session.post(url=url, data=payload)
        
        res = {'error_code':0}
        return res