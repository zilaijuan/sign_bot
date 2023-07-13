#!/usr/local/bin/python

from bot.southplus import SOUTHPLUS_Bot

import config
import log.LogConfig
import ast
import os


spb = SOUTHPLUS_Bot(ast.literal_eval(os.environ["SOUTHPLUS__HEADERS"]))
spb.start()
