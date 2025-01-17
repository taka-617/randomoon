from . import conn

def selectWeaponRandom():
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select main.id as main_id, sub.id as sub_id, main.weapon_name as main_weapon_name, sub.weapon_name as sub_weapon_name"\
    " from randamoon.weapons as main"\
    " inner join randamoon.weapons as sub on main.weapon_minor_kind_id = sub.weapon_minor_kind_id"\
    " and main.id != sub.id"\
    " ORDER BY RAND() LIMIT 1;"
    
    cursor.execute(query)

    weapon = cursor.fetchone()

    cnx.close()

    return {"main_id": weapon[0], "sub_id": weapon[1], "main_weapon": weapon[2], "sub_weapon": weapon[3]}

def selectWeaponRandomUnique(participant_id):
    cnx = conn.connect()

    cursor = cnx.cursor()

    query = "select main.id as main_id, sub.id as sub_id, main.weapon_name as main_weapon_name, sub.weapon_name as sub_weapon_name"\
    " from randamoon.weapons as main"\
    " inner join randamoon.weapons as sub on main.weapon_minor_kind_id = sub.weapon_minor_kind_id"\
    " and main.id != sub.id"\
    " where not exists("\
    " select weapon_id "\
    " from randamoon.weapon_histories as w_h"\
    " where w_h.participant_id = '{}'"\
    " and main.id = w_h.weapon_id)"\
    " ORDER BY RAND() LIMIT 1;".format(participant_id)
    
    cursor.execute(query)

    weapon = cursor.fetchone()

    cnx.close()

    return {"main_id": weapon[0], "sub_id": weapon[1], "main_weapon": weapon[2], "sub_weapon": weapon[3]}