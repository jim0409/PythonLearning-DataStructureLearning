# http://stackoverflow.max-everyday.com/2017/10/python-logging/
import logging

# NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.basicConfig(level='DEBUG')
# logging.basicConfig(level='WARNING')  # if use 'WARNING' would not show info

logging.info('debug_test')
