import mysql.connector


db = mysql.connector.connect(host='localhost', user='root', passwd = 'openupuser')
p = db.cursor()
p.execute(open('SQL/script002.sql').read())
