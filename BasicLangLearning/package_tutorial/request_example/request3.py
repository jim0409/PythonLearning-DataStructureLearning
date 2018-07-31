# refer to

# - run a server with nc
# sudo nc -l 8888

# run this python script

import requests

requests.post('http://localhost:8888', data={u'post': u'Andr\xe9 T\xe9chin\xe9'})

# run check encode
# import urllib.parse
# urllib.parse.unquote('Andr%C3%A9+T%C3%A9chin%C3%A9')