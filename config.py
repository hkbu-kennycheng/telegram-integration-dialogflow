#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Configuration file.
"""

import logging
import argparse

# Set cli arguments
OPTIONS = argparse.ArgumentParser(prog='run.py',
                                  description='A Telegram Bot who answers to all of your questions')
OPTIONS.add_argument('--TELEGRAM_TOKEN', help='Insert Telegram Token', required=True)
OPTIONS.add_argument('--ADMIN_CHAT_ID', help='Insert Telegram ChatID', nargs="*", default=[])
OPTIONS.add_argument('--DIALOGFLOW_KEY', help='Specify Dialogflow Key Path', required=True)
OPTIONS.add_argument('--WIT_TOKEN', help='Specify Wit Token', default='')
OPTIONS.add_argument('--CUSTOMVISION_PREDICTION_URL', help='Specify Custom Vision Prediction API URL', default='')
OPTIONS.add_argument('--CUSTOMVISION_PREDICTION_KEY', help='Specify Custom Vision Prediction API Key', default='')
OPTIONS.add_argument('--LANG', help='Specify language cod', default='en')
OPTIONS.add_argument('--log', help='Set logging value', default='DEBUG')
ARGUMENTS = OPTIONS.parse_args()

# Logging configs
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s.',
                    level=ARGUMENTS.log)

# Telegram configs
TELEGRAM_TOKEN = ARGUMENTS.TELEGRAM_TOKEN
ADMIN_CHAT_ID = ARGUMENTS.ADMIN_CHAT_ID

# Dialogflow configs
DIALOGFLOW_KEY = ARGUMENTS.DIALOGFLOW_KEY

# WIT configs
WIT_TOKEN = ARGUMENTS.WIT_TOKEN

# Custom Vision configs
CUSTOMVISION_PREDICTION_URL = ARGUMENTS.CUSTOMVISION_PREDICTION_URL
CUSTOMVISION_PREDICTION_KEY = ARGUMENTS.CUSTOMVISION_PREDICTION_KEY

# Language configs
LANG = ARGUMENTS.LANG
