# This is a side project to prvoe that statistic inference is somehow import rather than math or deeplearning
### in this side project
1. I use random normal to generate a sample data with specific value for slope and intercept term
2. Compare estimator from simple NN with statistic method (BLUE; Best Linear Unbiased Estimator) and normality estimator
3. Save the estimator into influxdb

# requirements before execute this project
1. Install python and tensorflow and related packages with `pip3 install -r requirements.txt`
2. Run an influxdb service at localhost:8086
3. run python3 main.py -c demo.conf

# check the simulation process with tensorboard
1. Execute command `tensorboard --logdir=logs`
