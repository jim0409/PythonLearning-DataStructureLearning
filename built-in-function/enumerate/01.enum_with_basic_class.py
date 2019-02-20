from enum import Enum

class InputType(Enum):
    TRACK = 'track'
    ALBUM = 'album'
    ARTIST = 'artist'
    PLAYLIST = 'playlist'

class ResponseType(Enum):
    OK = 'ok'
    NO_RESULT = 'no_result'

print(InputType.ARTIST == InputType.ALBUM)
# False
print(InputType.ARTIST == InputType.ARTIST)
# True
print(ResponseType.OK == ResponseType.NO_RESULT)
# Flase

print(InputType.PLAYLIST.name)
# 'PLAYLIST'
print(InputType.PLAYLIST.value)
# 'playlist'

print(InputType('playlist'))
# 'InputType.PLAYLIST'
print(InputType['PLAYLIST'])
# 'InputType.PLAYLIST'


