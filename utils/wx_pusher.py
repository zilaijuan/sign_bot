from wxpusher import WxPusher
from config import WXPUSHER_APPTOKEN

def push_to_wechat(text,summary=''):
    WxPusher.send_message(text,
                          summary=summary,
                          uids=['UID_NY2XaP87yCnZhFQqg30a5yYBWvLs'],
                          token=WXPUSHER_APPTOKEN)

if __name__ == '__main__':
    push_to_wechat(text = 'this is a test message', summary="summary")
    