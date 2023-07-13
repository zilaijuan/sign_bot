import requests
import logging
import os

from utils.wx_pusher import push_to_wechat
from config import SERVERCHAN_SECRETKEY
import pickle
class Base_Bot(object):
    def __init__(self,HEADERS):
        self.log = logging.getLogger(self.__class__.__name__)
        self.session = requests.Session()
        # 添加 cookie
        cookies = HEADERS['Cookie']
        cookies_dict={}
        for entity in cookies.split(";"):
            kv = entity.split("=")
            cookies_dict[kv[0]] = kv[1]
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookies_dict)
        HEADERS.pop('Cookie')
        # 添加 headers
        self.session.headers = HEADERS
        
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
        filename = self.__class__.__name__ + ".cookies"
        if os.path.exists(filename):
            cookies = self.load_cookies(filename)
            self.session.cookies.update(cookies)
            self.log.info("cookies updated")
        


        res = self.checkin()

        self.save_cookies(self.session.cookies, filename)
        # logging.info(res)
        # if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        if res['error_code'] != 0:
            self.log.info('签到异常， 准备推送')
            push_to_wechat(summary = thisName,
                            text = str(res))
        self.log.info('代码完毕')
        self.log.info('-> 任务圆满完成')
    
    def save_cookies(self, requests_cookiejar, filename):
        with open(filename, 'wb') as f:
            pickle.dump(requests_cookiejar, f)

    def load_cookies(self, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)