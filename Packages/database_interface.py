import mysql.connector

key = input('Please Enter mysql root password : ')

try:
    db = mysql.connector.connect(host='localhost', user='root', passwd=key)
    del key
    if db.is_connected():
        print('Successfully connected')
    p = db.cursor()

    def execute_sql(query):
        """can be used to execute sql query within Database : Aurora"""
        p.execute(query)
        if p.rowcount > 0:
            return p.fetchall()


    def execute_sql_from_file(path):
        sql_file = open(path)
        sql_code = sql_file.read()
        sql_file.close()
        sql_commands = sql_code.split(';')
        for command in sql_commands:
            p.execute(command)


    def is_unlocked(player_name, name, a_type):
        execute_sql('USE AURORA;')
        if a_type == 'spell':
            a_type = 'player_spells'
        elif a_type == 'troop':
            a_type = 'player_troops'
        else:
            return
        data_set = execute_sql(f'SELECT {name} FROM {a_type} WHERE PLAYER_NAME = {player_name};')
        if data_set is not None and data_set[0][0] == 1:
            return True
        return False


    def create_player(player_name):
        execute_sql('USE AURORA;')
        tables = ['game_stats', 'player_troops' 'player_spells', 'spells',
                  'delta', 'tardis', 'benzamite', 'mandalore', 'nemesis', 'armada', 'elysium', 'demogorgon']
        for table in tables:
            execute_sql(f'INSERT INTO {table} (PLAYER_NAME) VALUES {player_name};')

    execute_sql_from_file('../SQL/script001.sql')
    create_player('player_1')

#    if __name__ == '__main__':
#        p.close()
#        db.close()


#except mysql.connector.Error as err:
#    print(f"Something went wrong: {err}")
#    exit()

finally:
    print('Hello world')