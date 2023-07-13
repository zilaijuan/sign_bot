"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""

import logging

from bot.base_bot import Base_Bot

class SMZDM_Bot(Base_Bot):
    

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            return True
        except Exception as e:
            self.log.error(f'Error : {e}')            
            return False
 
    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        url = 'https://zhiyou.smzdm.com/user/'
        msg = self.session.get(url)
        print(msg.text)
        if self.__json_check(msg):
            return msg.json()
        return msg.content


