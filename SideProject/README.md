# This is a side project to compare the linear regression intercept term estimator with statistic inference, statistic method and NN.
### in this side project
1. Use random normal to generate a sample data with thes pecific value for slope and intercept values.
2. Compare intercept estimator from normality estimator, statistic method (BLUE; Best Linear Unbiased Estimator) and simple NN.
3. Save the estimator into influxdb
4. Record the loss and NN model with tensorflow package method `name_scope`

# requirements before execute this project
1. Install related packages with cli `pip3 install -r requirements.txt`
2. Run an influxdb service at localhost:8086;`docker run -p 8086:8086 -d influxdb`
3. run python3 main.py -c demo.conf

# check the simulation process with tensorboard
1. Execute command `tensorboard --logdir=logs`
