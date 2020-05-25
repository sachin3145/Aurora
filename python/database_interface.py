import mysql.connector

key = input('Please Enter mysql root password : ')
db = mysql.connector.connect(host='localhost', user='root', passwd=key)

if db.is_connected():
    print('connected')

'''
try:
    db = mysql.connector.connect(host='localhost', user='root', passwd=key)
    del key
    if db.is_connected():
        print('Successfully connected')
    p = db.cursor()
    p.execute(open('../SQL/script002.sql').read())
    p.close()

except:
    print('Connection Failed!')
    if eval(input('Enter 1 to troubleshoot or any other key to exit : ')) == 1:
        raise
'''