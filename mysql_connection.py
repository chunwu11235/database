import mysql.connector

conn = mysql.connector.connect(
    user='root', password='password',
    # :30597
    host='192.168.49.2',port=30597,
    database='mysql')
conn.close()
