"""
请求头
"""
DEFAULT_HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }


"""
调试用 COOKIE
"""
TEST_COOKIE = ''


"""
调试用 SERVERCHAN_SECRETKEY
"""
SERVERCHAN_SECRETKEY = 'SCT100876TQo282FWqbFNyKQuEcuNdeEUE'


"""
福利吧
"""
FLB_COOKIES = 'S5r8_2132_saltkey=clBW4FFZ; S5r8_2132_lastvisit=1638070270; S5r8_2132_auth=6021e9gDICGAuLBYtL9hrsnyYOfHqgB0ib8Y%2FrGz7D3YgQ99wY1mWAN4S58flGSBO4Nq8wUBN3BNY%2B50d%2Bz27BVoVg; S5r8_2132_lastcheckfeed=12334%7C1638074828; S5r8_2132_nofavfid=1; S5r8_2132_atarget=1; S5r8_2132_smile=1D1; S5r8_2132_forum_lastvisit=D_2_1638464180; S5r8_2132_visitedfid=2D62; S5r8_2132_sid=tJ35EA; S5r8_2132_lip=120.204.150.112%2C1638464180; S5r8_2132_ulastactivity=3374Oy62wDUYpE3%2BiAhDwdV4FC01hxcZIO1qxQctl0GTj3GfAmIZ; S5r8_2132_sendmail=1; S5r8_2132_lastact=1638622733%09misc.php%09patch'
FLB__HEADERS = {
  'authority': 'www.wnflb99.com',
  'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
  'sec-ch-ua-platform': '"Windows"',
  'accept': '*/*',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.wnflb99.com/',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': 'S5r8_2132_saltkey=nfFP863p; S5r8_2132_lastvisit=1639017571; S5r8_2132_sid=oDiMdk; S5r8_2132_sendmail=1; S5r8_2132_ulastactivity=8271gTo0nqOfGtD1Nf9FwYy0r1FaHaXg2gdbmkqilsCkhQS2AgFf; S5r8_2132_auth=5fc8JaIoI3dUZY9IXdKB%2FZYAkkGoX7yHF%2B6wW9eUim0Sfdzmwu4349fJyTeGUoHzJZPAJ7RTgel4Zxh%2FBz45oRmTBg; S5r8_2132_lastcheckfeed=12334%7C1639021184; S5r8_2132_checkfollow=1; S5r8_2132_lip=120.204.150.112%2C1638885687; S5r8_2132_nofavfid=1; S5r8_2132_checkpm=1; S5r8_2132_lastact=1639021184%09misc.php%09patch'
}
"""
手机淘
"""

SHHUU_COOKIES = 'Grix_144c_saltkey=x1n9z1yN; Grix_144c_lastvisit=1638619263; Grix_144c_connect_is_bind=1; Grix_144c_nofavfid=1; Grix_144c_smile=1D1; Grix_144c_visitedfid=105D23; Grix_144c_sid=uDzDQx; Grix_144c_viewid=tid_355741; safedog-flow-item=0DD7890BAE8A379D84A751B0A807D2F4; Grix_144c_sendmail=1; __51cke__=; Grix_144c_ulastactivity=990eHOb2qi0Lm6SYzs2oUkJZ1LRULS30yFCQCc0AOo5vbYXwqJs6; Grix_144c_auth=990eHOb2qi0Lm6SYzp%2BkCkMJhbMNKnmhmAHDC88AOYVgYoulp89m7PoYCM%2B1SBSkZn2QUqWG1Kbdbp8ay9FV7SIox9I; Grix_144c_creditnotice=0D0D0D0D5D0D0D0D0D154104; Grix_144c_creditbase=0D36D55D-2D6943D0D1642D0D0; Grix_144c_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; Grix_144c_security_cookiereport=630dGOW8Lhj5hMMJoUkZ%2BxEEAx6C0ep%2FURL4f3LEE85whryXHlHj; Grix_144c_st_p=154104%7C1638884836%7C6d156c623013e3bcfcff83bd7b40906f; Grix_144c_onlineusernum=751; Grix_144c_checkpm=1; Grix_144c_lastcheckfeed=154104%7C1638884928; Grix_144c_checkfollow=1; __tins__17492567=%7B%22sid%22%3A%201638884752584%2C%20%22vd%22%3A%2010%2C%20%22expires%22%3A%201638886736820%7D; __51laig__=10; Grix_144c_lastact=1638884928%09connect.php%09check'
SHHUU__HEADERS= {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.shhuu.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.shhuu.com/dsu_paulsign-sign.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'Grix_144c_saltkey=x1n9z1yN; Grix_144c_lastvisit=1638619263; Grix_144c_connect_is_bind=1; Grix_144c_nofavfid=1; Grix_144c_smile=1D1; Grix_144c_visitedfid=105D23; Grix_144c_sid=uDzDQx; Grix_144c_viewid=tid_355741; safedog-flow-item=0DD7890BAE8A379D84A751B0A807D2F4; Grix_144c_sendmail=1; __51cke__=; Grix_144c_ulastactivity=990eHOb2qi0Lm6SYzs2oUkJZ1LRULS30yFCQCc0AOo5vbYXwqJs6; Grix_144c_auth=990eHOb2qi0Lm6SYzp%2BkCkMJhbMNKnmhmAHDC88AOYVgYoulp89m7PoYCM%2B1SBSkZn2QUqWG1Kbdbp8ay9FV7SIox9I; Grix_144c_creditnotice=0D0D0D0D5D0D0D0D0D154104; Grix_144c_creditbase=0D36D55D-2D6943D0D1642D0D0; Grix_144c_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; Grix_144c_security_cookiereport=630dGOW8Lhj5hMMJoUkZ%2BxEEAx6C0ep%2FURL4f3LEE85whryXHlHj; Grix_144c_st_p=154104%7C1638884836%7C6d156c623013e3bcfcff83bd7b40906f; Grix_144c_onlineusernum=751; Grix_144c_checkpm=1; Grix_144c_lastcheckfeed=154104%7C1638884928; Grix_144c_checkfollow=1; __tins__17492567=%7B%22sid%22%3A%201638884752584%2C%20%22vd%22%3A%2010%2C%20%22expires%22%3A%201638886736820%7D; __51laig__=10; Grix_144c_lastact=1638884928%09connect.php%09check'
        }
"""
什么值得买
"""
SMZDM__HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'cookie': '__ckguid=QNU5lf69kErGkl62Kw5ATV27; device_id=213070643316386231488579944e225e5e7ea5fbefc0b9b71d0641476a; homepage_sug=c; r_sort_type=score; __jsluid_s=e4c6dcb0e17c246283ebb4037068d7b2; _zdmA.vid=*; sajssdk_2015_cross_new_user=1; footer_floating_layer=0; ad_date=4; ad_json_feed={}; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638623159; sess=AT-nYAX1/NAcgkd4Ai884qxbYLr5xS4cq2wybwpgDsTkJF9GtPWMrv8icH0ROs1b/XWKpJkqDBD9Ji/iuLrcDg8GrHnXIu5e3CHYYirlRq/ZMuSkZ8iayn74vsp; user=user:9838077729|9838077729; smzdm_id=9838077729; _zdmA.uid=ZDMA.6KsPugTH4.1638623384.2419200; bannerCounter=[{"number":1,"surplus":1},{"number":0,"surplus":1},{"number":1,"surplus":1},{"number":1,"surplus":1},{"number":0,"surplus":1},{"number":1,"surplus":1}]; _zdmA.time=1638623409886.15239.https://www.smzdm.com/; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638623411; sensorsdata2015jssdkcross={"distinct_id":"9838077729","first_id":"17d858d103455-0f84592decffd9-5919145b-1049088-17d858d10363ea","$device_id":"17d858d103455-0f84592decffd9-5919145b-1049088-17d858d10363ea"}'
        }
SMZDM_COOKIE = '__ckguid=QNU5lf69kErGkl62Kw5ATV27; device_id=213070643316386231488579944e225e5e7ea5fbefc0b9b71d0641476a; homepage_sug=c; r_sort_type=score; __jsluid_s=e4c6dcb0e17c246283ebb4037068d7b2; _zdmA.vid=*; sajssdk_2015_cross_new_user=1; footer_floating_layer=0; ad_date=4; ad_json_feed={}; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638623159; sess=AT-nYAX1/NAcgkd4Ai884qxbYLr5xS4cq2wybwpgDsTkJF9GtPWMrv8icH0ROs1b/XWKpJkqDBD9Ji/iuLrcDg8GrHnXIu5e3CHYYirlRq/ZMuSkZ8iayn74vsp; user=user:9838077729|9838077729; smzdm_id=9838077729; _zdmA.uid=ZDMA.6KsPugTH4.1638623384.2419200; bannerCounter=[{"number":1,"surplus":1},{"number":0,"surplus":1},{"number":1,"surplus":1},{"number":1,"surplus":1},{"number":0,"surplus":1},{"number":1,"surplus":1}]; _zdmA.time=1638623409886.15239.https://www.smzdm.com/; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638623411; sensorsdata2015jssdkcross={"distinct_id":"9838077729","first_id":"17d858d103455-0f84592decffd9-5919145b-1049088-17d858d10363ea","$device_id":"17d858d103455-0f84592decffd9-5919145b-1049088-17d858d10363ea"}'

"""
海胆之家
"""
'''
HAIDAN_HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'cookie': 'c_secure_login=bm9wZQ%3D%3D; c_secure_uid=MjgyMDA%3D; c_secure_pass=be3ea9140610746590f9ebdbe7ac6879',
        }

'''
HAIDAN_LOGIN = 'bm9wZQ%3D%3D'

HAIDAN_PASS = 'be3ea9140610746590f9ebdbe7ac6879'

HAIDAN_UID = 'MjgyMDA%3D'

HAIDAN_HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'cookie': 'c_secure_login=' + HAIDAN_LOGIN + '; c_secure_uid=' + HAIDAN_UID + '; c_secure_pass=' + HAIDAN_PASS,
}
