import requests
import matplotlib.pyplot as plt
# r = requests.post('http://httpbin.org/post', json={"key": "value"})
# select usage_idle from cpu

def showmeasurements(x):
    data = []
    date = []
    if len(x) < 3:
        print("do nothing")

    else:
        for i in range(len(x)):
            date.append(x[i][0])
            data.append(x[i][1])
    return date,data




if __name__=='__main__':

    # select io_time from diskio where "name" = 'sda'
    querystring = "http://localhost:8086/query?db=telegraf&q= select io_time from diskio where " + '"name"' + "='sda' "
    r = requests.post(querystring, json={"key": "value"})

    # print(r.json()['results'])

    if r.status_code != 200:
        print("no such response")
    else:
        x = r.json()['results'][0]['series'][0]['values']
        date,data = showmeasurements(x)

        print(date)
        print(data)
        plt.plot(date,data)
        plt.show()
