# through this file, i start my generation from pre-define model scale
# using inverse cdf theory to generate a survival time via coxph-transformed model
# then store data into influxdb and visualize it with grafana

# !/usr/bin/env python3
import os
import sys
import configparser
import argparse
import logging
from datetime import datetime
from project.simulation.gen.rand_dist.linear import LinearSimulation

sample_config = """
[FitModel]
Model = "Linear"
number_of_points = 500

[Linear-Parameters]
slope = 0.22
intercept = 0.78
"""

current_time = datetime(2018, 4, 14)

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
        configFile = config['FitModel']
        conf1 = configFile.get('Model')
        if conf1 is not None:
            if conf1.split('"')[1] != "Linear":
                logging.info("only support Linear model now!")
                sys.exit(1)
            else:
                conf2 = config['Linear-Parameters']
                logging.info("Use " + conf1 + " model to generate data")
                if conf2 is not None:
                    slope = conf2.getfloat('slope')
                    intercept = conf2.getfloat('intercept')
                    logging.info(
                        "with parameter slope %0.3f and intercept %0.3f" % (slope,intercept))
                    linear_fit_model = LinearSimulation(time=current_time, a=slope, b=intercept)
                    linear_fit_model.estimator_ai()
                    linear_fit_model.writedb()