import psycopg2

conn = psycopg2.connect(host="localhost", database="template1", user="postgres", password="password")

cur = conn.cursor()

sql ='''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);'''

cur.execute(sql)

# cur.execute(sql, (value1,value2))