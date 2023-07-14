#!/usr/local/bin/python
from bot.smzdm import SMZDM_Bot
from bot.wndflb import FLB_Bot
from bot.shhuu import SHHUU_Bot
from bot.haidan import HaiDan_Bot
from bot.zhixing import ZHIXING_Bot
from bot.jinfopai import JINFOPAI_Bot
from bot.manhua import MANHUA_Bot
from bot.moeshare import MOESHARE_Bot
from bot.southplus import SOUTHPLUS_Bot
from bot.threedm import THREEDM_Bot
import log.LogConfig
import ast
import os

try:
    import config
except ModuleNotFoundError:
    # Error handling
    pass



fb = FLB_Bot(ast.literal_eval(os.environ["FLB__HEADERS"]))
fb.start()

jfpb = JINFOPAI_Bot(ast.literal_eval(os.environ["JINFOPAI__HEADERS"]))
jfpb.start()

msb1 = MOESHARE_Bot(ast.literal_eval(os.environ["MOESHARE_1__HEADERS"]))
msb1.start()

# zxb = ZHIXING_Bot(config.ZHIXING__HEADERS)
# zxb.start()

#mhb = MANHUA_Bot(config.MANHUA__HEADERS)
#mhb.start()

#shb = SHHUU_Bot(config.SHHUU__HEADERS)
#shb.start()

# hdb = HaiDan_Bot(config.HAIDAN_HEADERS)
# hdb.start()



# msb2 = MOESHARE_Bot(config.MOESHARE_2__HEADERS)
# msb2.start()
# sb = SMZDM_Bot(config.SMZDM__HEADERS)
# sb.start()
'''
tdmb = THREEDM_Bot(config.THREEDM__HEADERS)
tdmb.start()
'''