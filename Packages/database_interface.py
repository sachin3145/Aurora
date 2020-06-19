import mysql.connector

key = input('Please Enter mysql root password : ')

try:
    db = mysql.connector.connect(host='localhost', user='root', passwd=key)
    del key
    if db.is_connected():
        print('Successfully connected')

except:
    print('Connection Failed!')
    if eval(input('Enter 1 to troubleshoot or any other key to exit : ')) == 1:
        raise
    exit()


p = db.cursor()
#    p.execute(open('../SQL/script002.sql').read())


def execute_sql(code):
    p.execute(code)
    return p.fetchall()


p.close()
