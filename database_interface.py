import mysql.connector

key = input('Please Enter mysql root password : ')

try:
    db = mysql.connector.connect(host='localhost', user='root', passwd = key)
    if db.is_connected(): print('Successfully connected')
    del key
    p = db.cursor()
    p.execute(open('SQL/script002.sql').read())
    p.close()
except:
    print('Connection Failed!')


