SELECT COLUMN_NAME, COLUMN_TYPE
from INFORMATION_SCHEMA.COLUMNS
where TABLE_SCHEMA = alx_book_store , TABLE_NAME = Books
