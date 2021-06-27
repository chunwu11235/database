import mysql.connector

conn = mysql.connector.connect(
    user='root', password='password',
    host='127.0.0.1',port=64245,
    database='classicmodels')
conn.close()
