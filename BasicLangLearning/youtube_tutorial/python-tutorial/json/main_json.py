import json

# load json from external files
json_file = open("./data.json", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()
print(movie)
