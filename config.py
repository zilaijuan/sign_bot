"""
请求头
"""
DEFAULT_HEADERS = {}


"""
调试用 COOKIE
"""
TEST_COOKIE = ''


"""
调试用 SERVERCHAN_SECRETKEY
"""
SERVERCHAN_SECRETKEY = ''


"""
福利吧
"""
FLB_COOKIES = ''
FLB__HEADERS = { }

"""
手机淘
"""
SHHUU_COOKIES = ''
SHHUU__HEADERS= { }

"""
什么值得买
"""
SMZDM__HEADERS = { }
SMZDM_COOKIE = ''

"""
海胆之家
"""
HAIDAN_LOGIN = ''

HAIDAN_PASS = ''

HAIDAN_UID = ''

HAIDAN_HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'cookie': 'c_secure_login=' + HAIDAN_LOGIN + '; c_secure_uid=' + HAIDAN_UID + '; c_secure_pass=' + HAIDAN_PASS,
        }
