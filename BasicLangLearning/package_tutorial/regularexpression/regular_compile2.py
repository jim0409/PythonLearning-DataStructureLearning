import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小寫
m = pattern.match("Hello World Wide Web")

print(m)

# show all the match parts of regular expression
print(m.group())

# show all the match parts of regular expression place
print(m.span(0))

# the first and second group of match parts
print(m.group(1))
print(m.group(2))

# the first and second parts of regular expression place
print(m.span(1))
print(m.span(2))

# particular groups
print(m.groups())

# print(m.groups()) # 不存在第三分組