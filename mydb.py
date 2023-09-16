import mysql.connector

dataBase =mysql.connector.connect(
    host ='localhost',
    user ='root',
    password = ''

)

cursorObject =dataBase.cursor()


cursorObject.execute("Create Database CRM")

print('ALL Done!')