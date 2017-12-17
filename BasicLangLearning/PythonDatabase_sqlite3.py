# refer to website
# https://docs.python.org/3/library/sqlite3.html
# http://www.pfinn.net/python-check-if-file-exists.html

import os
import sqlite3

# # if  example_jim.db exist then do not execute below code
if not os.path.isfile('/Users/mac/PycharmProjects/PythonLearning-DataStructureLearning/BasicLangLearning/example_jim.db'):
    # create db
    conn = sqlite3.connect('example_jim.db')

    # create db cursor()
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

# connect db again
conn = sqlite3.connect('example_jim.db')
c = conn.cursor()

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)