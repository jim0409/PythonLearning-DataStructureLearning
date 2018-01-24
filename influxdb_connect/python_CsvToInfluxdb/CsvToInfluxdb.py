# https://stackoverflow.com/questions/43186129/importing-csv-file-data-into-influxdb?rq=1
import time
from influxdb import client as influxdb

# 宣告InfluxDBClient後面用以生成instance
db = influxdb.InfluxDBClient(host='localhost', port=8086, username='root', password='root',database='mydb')

# 建立db
db.create_database('mydb')

# 讀取csv內2~10行的資料
def read_data(filename):
    with open(filename) as f:
        return [x.split(',') for x in f.readlines()[1:10]]


if __name__ == '__main__':
    filename='/home/ubuntu/Desktop/backblaze/2017-01-01.csv'
    a=read_data(filename)

    for metric in a:
        influx_metric = [{
            'measurement': 'JimMea',
            # 用於計算毫秒 :註 因為influxdb在沒有tag做區別下同一時間點會覆寫
            'time': int(round(time.time()*100000)),
            'fields': {
                'value': metric[1],
                'smart_9_raw':metric[20],
            }
        }]
        db.write_points(influx_metric)
