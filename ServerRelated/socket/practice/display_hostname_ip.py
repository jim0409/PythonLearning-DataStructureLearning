import socket

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname: {}".format(host_name))
        print("IP: {}".format(host_ip))
    
    except:
        print("Unable to get Hostname and IP.")

get_Host_name_IP()