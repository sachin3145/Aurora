import mysql.connector

#key = input('Please Enter mysql root password : ')
key = 'openupuser'
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


p = db.cursor(buffered=True)
p.execute(open('../SQL/script001.sql').read(), multi=True)


def execute_sql(query):
    """can be used to execute sql query"""
    p.execute(query)
    if p.rowcount > 0:
        return p.fetchall()


def is_unlocked(player_id, name, a_type):
    if a_type == 'spell':
        a_type = 'player_spells'
    elif a_type == 'troop':
        a_type = 'player_troops'
    else:
        return
    execute_sql('USE AURORA;')
    data_set = execute_sql('SELECT {} FROM {} WHERE PLAYER_ID = {};'.format(name, a_type, player_id))
    if data_set is not None and data_set[0][0] == 1:
        return True
    return False


# print(is_unlocked('0123456789', 'RAY_OF_SICKNESS', 'spell')) -- TEST

if __name__ == '__main__':
    p.close()
