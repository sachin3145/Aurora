import mysql.connector

key = input('Please Enter mysql root password : ')

try:
    db = mysql.connector.connect(host='localhost', user='root', passwd=key)
    del key
    if db.is_connected():
        print('Successfully connected')
    p = db.cursor()
    p.execute(open('SQL/script002.sql').read())
    p.close()

except:
    print('Connection Failed!')
    if eval(input('Enter 0 to exit or 1 to troubleshoot : ')) == 1:
        raise
