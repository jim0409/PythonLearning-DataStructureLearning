import enum

class StrEnum(str, enum.Enum):
    pass

class Browser(StrEnum):
    FIREFOX = 'firefox'
    CHROME = 'chrome'

print(Browser.FIREFOX == 'firefox')
# True

print(Browser.CHROME == 'chromium')
# False