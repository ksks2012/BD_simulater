import sqlite3
import os
import pandas as pd

from char_data import Char_data

db_name = 'character.sqlite3'


def connect(name):
    create = not os.path.exists(name)
    conn = sqlite3.connect(name)
    if create:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE data ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "name TEXT NOT NULL, "
                       "type TEXT NOT NULL, "
                       "url TEXT NOT NULL, "
                       "atk INTEGER NOT NULL, "
                       "hp INTEGER NOT NULL, "
                       "defen FLOAT NOT NULL, "
                       "CT_rate FLOAT NOT NULL, "
                       "CT_bonus FLOAT NOT NULL, "
                       "dex FLOAT NOT NULL, "
                       "up_time TimeStamp NOT NULL DEFAULT (datetime('now','localtime'))) ")
        conn.commit()

    return conn


def add_data(data):

    conn = connect(db_name)
    #director_id = get_and_set_director(conn, director)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data "
                   "(name, type, url, atk, hp, defen, CT_rate, CT_bonus, dex) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (data['name'], data['type'], data['url'], data['atk'], data['hp'], data['defen'], data['CT_rate'], data['CT_bonus'], data['dex']))
    conn.commit()
    pass


def get_all_data():

    #data = Char_data()

    conn = connect(db_name)
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM data WHERE name!='None' ORDER BY type ")
    sql = "SELECT * FROM data WHERE name!='None' ORDER BY type "

    data_df = pd.read_sql(sql, conn)

    return data_df

    pass


def get_all_data_no_support():

    #data = Char_data()

    conn = connect(db_name)
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM data WHERE name!='None' ORDER BY type ")
    sql = "SELECT * FROM data WHERE name!='None' and type!='support' ORDER BY type "
    #sql = "SELECT * FROM data WHERE name!='None' and type!='support' ORDER BY hp"

    data_df = pd.read_sql(sql, conn)

    return data_df

    pass


def get_all_support_data():

    #data = Char_data()

    conn = connect(db_name)
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM data WHERE name!='None' ORDER BY type ")
    sql = "SELECT * FROM data WHERE name!='None' and type=='support'"

    data_df = pd.read_sql(sql, conn)

    return data_df

    pass


def get_support_skill(_id):

    conn = connect(db_name)
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM data WHERE name!='None' ORDER BY type ")
    sql = "SELECT * FROM sup_skill WHERE id==" + str(_id)

    data_df = pd.read_sql(sql, conn)

    return data_df


if __name__ == "__main__":

    #db_name = 'character.sqlite3'
    #conn = connect(db_name)

    # add_data(conn)
    #add_dvd(conn, 'Python Tutorial 2013', 2013, 1, 'Justin')
    # print(all_directors(conn))
    # print(all_dvds(conn))
    data_list = []

    data_df = get_support_skill(252)
    print(data_df)
    pass
