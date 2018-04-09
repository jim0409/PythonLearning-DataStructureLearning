import csv

dates = []
names = []

# with會打開一個I/O stream 並且使用預先宣告好的array做append把資料存取下來
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        name = row[3]
        date = row[0]

        dates.append(date)
        names.append(name)

print(names)
print(dates)