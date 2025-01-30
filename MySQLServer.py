# from mysql.connector import connect , Error
import mysql.connector
import os
try:
    
    MY_DB = mysql.connector.connect(
        host="localhost",
        user="Nada",
        # user = os.environ.get('DB_USER'),
        # passwod =  os.environ.get('DB_PASS'), 
        password="0752",
        database="alx_book_store"
    ) as MY_DB:
    # with connect(
    #     host="localhost",
    #     user="Nada",
    #     password="0752",
    #     database="alx_book_store"
    # ) as connection: 
    print(f'Database \'{MY_DB.database}\' created successfully!');

except mysql.connector.Error as e:
    print(e)

# MY_DB = mysql.connector.connect(
#     host="localhost",
#     user="Nada",
#     password="0752",
#     database="alx_book_store"
# );
# while MY_DB.get_server_info():
#     try:
#         print(f'Database \'{MY_DB.database}\' created successfully!')
#         break
#     except Exception as E:
#         print(E)
