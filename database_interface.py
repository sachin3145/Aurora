import mysql.connector


def create_user():

    db = mysql.connector.connect(host='localhost', user='root', passwd = 'openupuser')
    p = db.cursor()
    sql_file = open('SQL/script002.sql')
    print(sql_file.read())
    p.execute(sql_file.read())


create_user()


