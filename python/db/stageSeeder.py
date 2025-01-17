import mysql.connector
from . import conn

def seed():
    trancate()

    cnx = conn.connect()

    cursor = cnx.cursor()

    query = 'insert ignore into randamoon.stages (stage_name) values '\
    '("ユノハナ大渓谷")'\
    ',("ゴンズイ地区")'\
    ',("ヤガラ市場")'\
    ',("マテガイ放水路")'\
    ',("ナメロウ金属")'\
    ',("マサバ海峡大橋")'\
    ',("キンメダイ美術館")'\
    ',("マヒマヒリゾート＆スパ")'\
    ',("海女美術大学")'\
    ',("チョウザメ造船")'\
    ',("スメーシーワールド")'\
    ',("クサヤ温泉")'\
    ',("ヒラメが丘団地")'\
    ',("ナンプラー遺跡")'\
    ',("マンタマリア号")'\
    ',("タラポートショッピングパーク")'\
    ',("コンブトラック")'\
    ',("タカアシ経済特区")'\
    ',("オヒョウ海運")'\
    ',("バイガイ亭")'\
    ',("ネギトロ炭鉱")'\
    ',("カジキ空港")'\
    ',("リュウグウターミナル")'\
    ',("ザトウマーケット");'
    cursor.execute(query)

    cnx.commit()
    cnx.close()

def trancate():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "truncate table randamoon.stages;"
    cursor.execute(query)
    cnx.close()