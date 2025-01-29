import mysql.connector

MY_DB = mysql.connector.connect(
    host="localhost",
    user="Nada",
    password="0752",
    database="alx_book_store"
);
while MY_DB.get_server_info():
    try:
        print(f'Database \'{MY_DB.database}\' created successfully!')
        break
    except Exception as E:
        print(E)
