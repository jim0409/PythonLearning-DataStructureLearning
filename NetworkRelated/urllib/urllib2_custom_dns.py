# # refer from
# https://stackoverflow.com/questions/2236498/tell-urllib-to-use-custom-dns
# https://stackoverflow.com/questions/4518431/requests-equiv-of-curl-resolve?noredirect=1&lq=1
# https://stackoverflow.com/questions/22609385/python-requests-library-define-specific-dns
# https://www.cnblogs.com/toops/p/8228133.html
# https://docs.python.org/3/library/http.client.html
# https://blog.51cto.com/718693/1691625
# https://hack0nair.me/2013-05-14-how-to-customize-domain-parsing-on-python/
# https://www.cnblogs.com/liutong3310/p/3741813.html
# https://stackoverflow.com/questions/13778252/import-httplib-importerror-no-module-named-httplib


import http.client
import urllib


# replace to the IP needed to be access
access_ip = ""
# replace to the FQDN needed to be resovle
FQDN_replace = ""
# replace with the querystring
access_querystring = ""


reqheaders = {
    'MobileType': 'Android',
    'DeviceToken': 'xxxxxxxxx',
    'OSVersion': '1.0.3',
    'AppVersion': '14',
    'Host': FQDN_replace}

reqconn = http.client.HTTPConnection(access_ip)
reqconn.request("GET", access_querystring, None, reqheaders)
res = reqconn.getresponse()
print(res.status,  res.reason)
print(res.msg)
print(res.read())
