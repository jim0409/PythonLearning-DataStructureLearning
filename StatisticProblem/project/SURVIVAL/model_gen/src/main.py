# through this file, i start my generation from pre-define model scale
# using inverse cdf theory to generate a survival time via coxph-transformed model
# then store data into influxdb and visualize it with grafana

# !/usr/bin/env python3
import os
import sys
import configparser
import argparse
import logging

sample_config = """
[TestConf]
Distribution = "exponential"
Parameters = 1
"""

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', type=str, help='need to insert an valid conf file')
parser.add_argument('-s', '--sample_config', type=str, help='use --sample_config true to see config')
opts = parser.parse_args()

if opts.sample_config == 'true':
    print(sample_config)
    sys.exit(1)
else:
    pass

if opts.config is None:
    logging.info("need to put a valid conf")
    sys.exit(1)
else:
    if not os.path.isfile(opts.config):
        print("file doesn't exist")
    else:
        config = configparser.ConfigParser()
        config.read(opts.config)
        configFile = config['TestConf']
        conf1 = configFile.get('Distribution')
        conf2 = configFile.getfloat('Parameters')
        if conf1 is not None:
            if conf1.split('"')[1] != "Exponential":
                logging.info("only support Exponential now!")
                sys.exit(1)
            else:
                logging.info("Use distribution " + conf1 + " to generate data")
                if conf2 is not None:
                    logging.info("with parameter scale %d" % conf2)
