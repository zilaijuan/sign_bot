"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import sys
import requests
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
            logging.error(f'Error : {e}')            
            return False
 
    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content

'''
def start(SERVERCHAN_SECRETKEY):
    logging.info("=================================================")
    logging.info("||                 smzdm Sign                  ||")
    logging.info("=================================================")
    sb = SMZDM_Bot()
    sb.load_cookie_str(config.SMZDM_COOKIE)
    # cookies = os.environ["COOKIES"]
    # sb.load_cookie_str(cookies)
    res = sb.checkin()
    
    # print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        if res['error_code'] != 0:
            logging.info('检测到 SCKEY， 准备推送')
            push_to_wechat(text = '什么值得买每日签到',
                            desp = str(res),
                            secretKey = SERVERCHAN_SECRETKEY)
    logging.info('代码完毕')
'''
