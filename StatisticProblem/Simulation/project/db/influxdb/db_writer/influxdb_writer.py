import logging
from influxdb import InfluxDBClient


class DBwriter:
    def __init__(self, time, ai_value, stat_value, true_value):
        self.__time = time
        self.__ai_value = ai_value
        self.__stat_value = stat_value
        self.__true_value = true_value

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
                    "ai_value": self.__ai_value,
                    "stat_value": self.__stat_value,
                    "true_value": self.__true_value,
                }
            }
        ]

        client = InfluxDBClient(host, port, user, password, dbname)

        logging.info("Create database: " + dbname)
        client.create_database(dbname)

        logging.info("Write points: {0}".format(json_body))
        client.write_points(json_body)

