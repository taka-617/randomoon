from . import conn
 
def countAll():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select count(id) as count from randamoon.stages;"
    cursor.execute(query)

    stage_count = cursor.fetchone()

    cnx.close()

    return stage_count[0]

def selectRandom(selected_stages):
    cnx = conn.connect()

    cursor = cnx.cursor()

    if len(selected_stages) == 0:
        query = "select * from randamoon.stages ORDER BY RAND() LIMIT 1;"
    else:
        stages = ','.join(selected_stages)
        query = "select * from randamoon.stages where id not in({}) ORDER BY RAND() LIMIT 1;".format(stages)
    
    cursor.execute(query)

    stage = cursor.fetchone()

    cnx.close()

    return stage