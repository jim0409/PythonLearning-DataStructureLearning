class Client:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name


# 如果有需要初始化一些個別事件，可以在這邊定義，
# 如此一台，在增加新的ClientEvent時就會被呼叫
class ClientEvent:
    pass


class ClientQueue:
    def __init__(self):
        self.clients = []
        self.listeners = []
    
    def addClientListener(self, listener):
        self.listeners.append(listener)
    
    def removeClientListener(self, listener):
        self.listeners.remove(listener)
    
    def notifyAdded(self, client):
        event = ClientEvent()
        event.ip = client.ip
        event.name = client.name
        for listener in self.listeners:
            # 定義在Client Logger裡面
            listener.clientAdded(event)
            print("client {} is attending to  ".format(event.name) + listener.show(self))

    def notifyRemoved(self, client):
        event = ClientEvent()
        event.ip = client.ip
        event.name = client.name
        for listener in self.listeners:
            # 定義在Client Logger裡面
            listener.clientRemoved(event)
            print("client {} is not belong to ".format(event.name) + listener.show(self))
    
    def add(self, client):
        self.clients.append(client)
        self.notifyAdded(client)
    
    def remove(self, client):
        self.clients.remove(client)
        self.notifyRemoved(client)

    # def __str__(self):
        # return "{} has data {}".format(type(self).__name__, [(i.ip, i.name) for i in self.clients])
    

class ClientLogger:
    def clientAdded(self, event):
        print(event.ip + " added ...")

    def clientRemoved(self, event):
        print(event.ip + " removed ...")

    def show(self, clientqueue):
        return "{} has Logger {}".format(type(self).__name__, [(i.ip, i.name) for i in clientqueue.clients])


class ClientFormater:
    def clientAdded(self, event):
        print(event.name + " is comming ...")
    
    def clientRemoved(self, event):
        print(event.name + " is gone ...")

    def show(self, clientqueue):
        return "{} has Format {}".format(type(self).__name__, [(i.ip, i.name) for i in clientqueue.clients])


queue = ClientQueue()

queue.addClientListener(ClientLogger())
queue.addClientListener(ClientFormater())

c1 = Client("10.10.0.2", "caterpillar")
c2 = Client("192.168.0.2", "justin")
queue.add(c1)
# print(queue)

queue.add(c2)
# print(queue)

queue.remove(c1)
# print(queue)

queue.remove(c2)
# print(queue)