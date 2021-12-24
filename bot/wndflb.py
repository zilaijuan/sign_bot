"""
福利吧论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""
import re
import logging
import requests

from bot.base_bot import Base_Bot
import config


class FLB_Bot(Base_Bot):
    """
    福利吧论坛
    """

    def checkin(self):
        """
        登陆
        """
        url = "https://www.wnflb99.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        payload="username=%s&password=%s&quickforward=yes&handlekey=ls" % (config.FLB_USERNAME,config.FLB_PASSWORD)
        msg = self.session.post(url,  data=payload)
        self.session.cookies = msg.cookies
        
        cookie = requests.utils.dict_from_cookiejar(msg.cookies)
        msg = self.session.get("https://www.wnflb99.com",cookies=cookie)
        content = msg.content.decode('utf-8',errors='ignore')
        """
        获取formhash
        """
        pattern = re.compile('plugin\.php\?id=fx_checkin\:checkin\&formhash=(.*)\'\);')
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
        url = 'https://www.wnflb99.com/plugin.php?id=fx_checkin:checkin&formhash=%s&infloat=yes&handlekey=fx_checkin&inajax=1&ajaxtarget=fwin_content_fx_checkin' % (formhash)
        msg = self.session.get(url,cookies=cookie)
        data = msg.content.decode('utf-8')
        #  校验结果是否正确
        pattern = re.compile('errorhandle_fx_checkin\(\'签到成功,您今日第(\d+)个签到,累计签到(\d+)天!')
        mn = re.search(pattern, data)
        res = {'error_code':0}
        if mn:
            self.log.info('签到成功,您今日第'+ mn.group(1)+'个签到,累计签到'+ mn.group(2)+'天!' )
        else:
            self.log.error(data)
            res = {'error_code':-1,'error_msg':'福利吧签到失败'}
        return res


