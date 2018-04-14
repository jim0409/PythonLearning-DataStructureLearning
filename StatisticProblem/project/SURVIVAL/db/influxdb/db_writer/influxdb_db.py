import argparse
import logging
from influxdb import InfluxDBClient
from datetime import datetime

def strftime(time):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')

database_name = "demo"
hostname = "jim_test_server"
region = "taiwan"

# below datetime declaration are available
# current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
# current_time = datetime.utcnow()
# current_time = datetime.now()
current_time = datetime(2018,4,14)

current_time = strftime(current_time)
print(current_time)
measurement = "surf"
float_value = 0.74
int_value = 3

def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'root'
    dbname = database_name
    # dbuser = ''
    # dbuser_password = ''
    # query = 'select value from cpu_load_short;'
    json_body = [
        {
            "measurement": measurement,
            "tags": {
                "host": hostname,
                "region": region
            },

            # "time": "2009-11-10T23:00:00Z",
            "time": current_time,
            "fields": {
                "Float_value": float_value,
                "Int_value": int_value,
                # "String_value": "place_some_string",
                # "Bool_value": True
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

    logging.info("Create database: " + dbname)
    client.create_database(dbname)

    # no need retention policy in 1.4.2 influxdb version
    # in our case no need to configure user/password and no need to drop database
    # use it when need it

    # print("Create a retention policy")
    # client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    # print("Switch user: " + dbuser)
    # client.switch_user(dbuser, dbuser_password)

    logging.info("Write points: {0}".format(json_body))
    client.write_points(json_body)

    # logging.info("Querying data: " + query)
    # result = client.query(query)

    # logging.info("Result: {0}".format(result))

    # print("Switch user: " + user)
    # client.switch_user(user, password)
    #
    # print("Drop database: " + dbname)
    # client.drop_database(dbname)


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False, default='localhost', help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086, help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
