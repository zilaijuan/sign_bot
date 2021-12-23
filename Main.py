from bot.smzdm import SMZDM_Bot
from bot.wndflb import FLB_Bot
from bot.shhuu import SHHUU_Bot
from bot.haidan import HaiDan_Bot
from bot.zhixing import ZHIXING_Bot
import config
import log.LogConfig



sb = SMZDM_Bot(config.SMZDM__HEADERS)
sb.start()

fb = FLB_Bot(config.FLB__HEADERS)
fb.start()

shb = SHHUU_Bot(config.SHHUU__HEADERS)
shb.start()

zxb = ZHIXING_Bot(config.ZHIXING__HEADERS)
zxb.start()

hdb = HaiDan_Bot(config.HAIDAN_HEADERS)
hdb.start()