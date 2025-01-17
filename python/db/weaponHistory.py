from . import conn

def insert(weapon_id, participant_id):
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "insert ignore into randamoon.weapon_histories (weapon_id, participant_id) values ({}, {});".format(weapon_id, participant_id)
    cursor.execute(query)

    cnx.commit()
    cnx.close()

def trancate():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "truncate table randamoon.weapon_histories;"
    cursor.execute(query)
    cnx.close()
