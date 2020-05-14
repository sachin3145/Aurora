import mysql.connector


def create_user(name, key):

    db = mysql.connector.connect(host='localhost', user='root', passwd = key)
    p = db.cursor()
    sql_file = open('SQL/script001.sql')
    p.execute(sql_file.read().format(name))

