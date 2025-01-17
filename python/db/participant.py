from . import conn

def insert(user_id):
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "insert ignore into randamoon.participants (user_id) values ({});".format(user_id)
    cursor.execute(query)

    cnx.commit()
    cnx.close()

def delete(user_id):
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "delete from randamoon.participants where user_id = {};".format(user_id)
    cursor.execute(query)

    cnx.commit()
    cnx.close()

def trancate():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "truncate table randamoon.participants;"
    cursor.execute(query)
    cnx.close()

def selectAll():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select * from randamoon.participants;"
    cursor.execute(query)

    participants = cursor.fetchall()

    cnx.close()

    return participants

def selectOne(user_id):
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select * from randamoon.participants where user_id = {};".format(user_id)
    cursor.execute(query)

    participants = cursor.fetchone()

    cnx.close()

    return participants