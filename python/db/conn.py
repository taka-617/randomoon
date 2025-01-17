import mysql.connector

def connect():
    return mysql.connector.connect(
        host='192.168.2.2',
        port='3306',
        user='docker',
        password='docker',
        database='randamoon'
    )