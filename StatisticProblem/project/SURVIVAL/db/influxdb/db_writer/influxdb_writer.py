import logging
from influxdb import InfluxDBClient


class DBwriter:
    def __init__(self, time, float_value, int_value):
        self.__time = time
        self.__float_value = float_value
        self.__int_value = int_value

    def write(self):
        self.__time = self.strftime()
        self.dbwriter()
        return 0

    def strftime(self):
        return self.__time.strftime('%Y-%m-%dT%H:%M:%SZ')

    def dbwriter(self, host='localhost', port=8086):
        """Instantiate a connection to the InfluxDB."""
        user = 'root'
        password = 'root'
        dbname = "demo"
        hostname = "jim_test_server"
        region = "taiwan"
        measurement = "surf"
        json_body = [
            {
                "measurement": measurement,
                "tags": {
                    "host": hostname,
                    "region": region
                },

                "time": self.__time,
                "fields": {
                    "Float_value": self.__float_value,
                    "Int_value": self.__int_value,
                }
            }
        ]

        client = InfluxDBClient(host, port, user, password, dbname)

        logging.info("Create database: " + dbname)
        client.create_database(dbname)

        logging.info("Write points: {0}".format(json_body))
        client.write_points(json_body)

# # from datetime import datetime
# # below datetime declaration are available
# # current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
# # current_time = datetime.utcnow()
# # current_time = datetime.now()
# current_time = datetime(2018, 4, 3)
#
# # current_time = strftime(current_time)
# print(current_time)
#
# a = DBwriter(time=current_time, float_value=0.81, int_value=4)
# a.write()
