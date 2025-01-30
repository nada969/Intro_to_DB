from mysql.connector import connect , Error

try:
    with connect(
        host="localhost",
        user="Nada",
        password="0752",
        database="alx_book_store"
    ) as connection: 
        print(f'Database \'{connection.database}\' created successfully!');

except Error as e:
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
