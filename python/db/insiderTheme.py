from . import conn

def selectRandom():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select *"\
    " from randamoon.insider_themes as insider_themes"\
    " ORDER BY RAND() LIMIT 1;"
    
    cursor.execute(query)

    theme = cursor.fetchone()

    cnx.close()

    return {"theme": theme[1]}