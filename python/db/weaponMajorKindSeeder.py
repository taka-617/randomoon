import mysql.connector
from . import conn

def seed():
    trancate()

    cnx = conn.connect()

    cursor = cnx.cursor()

    query = 'insert ignore into randamoon.weapon_major_kinds (weapon_major_kind_name) values '\
    '("シューター")'\
    ',("ローラー")'\
    ',("チャージャー")'\
    ',("スロッシャー")'\
    ',("スピナー")'\
    ',("マニューバー")'\
    ',("シェルター")'\
    ',("ブラスター")'\
    ',("フデ")'\
    ',("ストリンガー")'\
    ',("ワイパー");'
    cursor.execute(query)

    cnx.commit()
    cnx.close()

def trancate():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "truncate table randamoon.weapon_major_kinds;"
    cursor.execute(query)
    cnx.close()