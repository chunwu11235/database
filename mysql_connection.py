import mysql.connector

conn = mysql.connector.connect(
    user='root', password='password',
    host='127.0.0.1',port=57950,
    database='classicmodels')

cursor = conn.cursor()

query = (
    'SELECT * FROM customers LIMIT 5'
)

cursor.execute(query)
for row in cursor:
    print(row)

conn.close()
