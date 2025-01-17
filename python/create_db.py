import mysql.connector

#python3 create_db.py

# connect mysql
cnx = mysql.connector.connect(
    host='192.168.2.2',
    port='3306',
    user='docker',
    password='docker',
    database='randamoon'
)
cursor = cnx.cursor()

#create new table
query1 = "create table if not exists participants (id int auto_increment PRIMARY KEY, user_id varchar(40) UNIQUE KEY);"
cursor.execute(query1)

query2 = "create table if not exists stages (id int auto_increment PRIMARY KEY, stage_name varchar(255));"
cursor.execute(query2)

query3 = "create table if not exists weapons (id int auto_increment PRIMARY KEY, weapon_name varchar(40) not null, weapon_major_kind_id int not null, weapon_minor_kind_id int not null);"
cursor.execute(query3)

query4 = "create table if not exists weapon_major_kinds (id int auto_increment PRIMARY KEY, weapon_major_kind_name varchar(40) not null);"
cursor.execute(query4)

query5 = "create table if not exists weapon_minor_kinds (id int auto_increment PRIMARY KEY, weapon_minor_kind_name varchar(40) not null, weapon_major_kind_id int not null);"
cursor.execute(query5)

query6 = "create table if not exists stage_histories (id int auto_increment PRIMARY KEY, stage_id int not null);"
cursor.execute(query6)

query7 = "create table if not exists weapon_histories (id int auto_increment PRIMARY KEY, weapon_id int not null, participant_id varchar(40) not null);"
cursor.execute(query7)

query8 = "create table if not exists insider_themes (id int auto_increment PRIMARY KEY, theme varchar(100) not null);"
cursor.execute(query8)

#check table
query3 = "SHOW TABLES;"
cursor.execute(query3)
print(cursor.fetchall())