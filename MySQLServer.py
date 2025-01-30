# from mysql.connector import connect , Error
import mysql.connector
try:
    
    with mysql.connector.connect(       
        host="localhost",
        user="Nada",
        password="0752",
        database="alx_book_store"
    ) as MY_DB:
    # with connect(
    #     host="localhost",
    #     user="Nada",
    #     password="0752",
    #     database="alx_book_store"
    # ) as connection: 
        # cursor = MY_DB.cursor()
        # print(f'Database \'{MY_DB.database}\' created successfully!')
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        with MY_DB.cursor() as cursor:
            cursor.execute(create_db_query)

except Exception as e:
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
