# https://stackoverflow.com/questions/43186129/importing-csv-file-data-into-influxdb?rq=1

# def read_data():
#     with open('file.csv') as f:
#         return [x.split(',') for x in f.readlines()[1:]]
#
# a = read_data()
#
# for metric in a:
#     influx_metric = [{
#         'measurement': 'your_measurement',
#         'time': metric[0],
#         'fields': {
#              'value': metric[1]
#         }
#     }]
#     db.write_points(influx_metric)