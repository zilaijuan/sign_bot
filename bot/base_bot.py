import requests
import logging

from utils.serverchan_push import push_to_wechat
from config import SERVERCHAN_SECRETKEY

class Base_Bot(object):
    def __init__(self,HEADERS):
        self.log = logging.getLogger(self.__class__.__name__)
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = HEADERS
        # 添加 cookie
        # self.session.headers['cookie'] = cookies

    def checkin(self):
        """
        签到函数
        """
        pass


    def start(self):
        thisName = self.__class__.__name__
        self.log.info("=================================================")
        self.log.info(thisName)
        self.log.info("=================================================")
        
        # sb.load_cookie_str(config.TEST_COOKIE)
        #self.load_cookie_str(cookies,headers)
        res = self.checkin()
        # logging.info(res)
        if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
            if res['error_code'] != 0:
                self.log.info('检测到 SCKEY， 准备推送')
                push_to_wechat(text = thisName,
                                desp = str(res),
                                secretKey = SERVERCHAN_SECRETKEY)
        self.log.info('代码完毕')
        self.log.info('-> 任务圆满完成')
