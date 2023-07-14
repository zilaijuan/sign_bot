#!/usr/local/bin/python

from bot.southplus import SOUTHPLUS_Bot

import log.LogConfig
import ast
import os
try:
    import config
except ModuleNotFoundError:
    # Error handling
    pass


spb = SOUTHPLUS_Bot(ast.literal_eval(os.environ["SOUTHPLUS__HEADERS"]))
spb.start()
