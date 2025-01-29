CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE Authors (
author_id INT,
PRIMARY Key (author_id),
author_name VARCHAR(215) 
);

CREATE TABLE Books (
book_id INT,
author_id INT,
title VARCHAR(130),
price DOUBLE,
publication_date DATE,
PRIMARY Key (book_id),
Foreign Key (author_id) REFERENCES Authors (author_id)
);


CREATE TABLE Customers (
customer_id INT,
PRIMARY Key (customer_id ),
customer_name VARCHAR(215),
email VARCHAR(215),
address TEXT
);

CREATE TABLE Orders (
Order_id INT,
customer_id INT,
PRIMARY Key (Order_id ),
Foreign Key (customer_id) REFERENCES Customers (customer_id),
order_date DATE
);

CREATE TABLE Order_Details (
detail_id INT,
Order_id INT,
book_id INT,
PRIMARY Key (detail_id),
Foreign Key (Order_id) REFERENCES Orders (Order_id),
Foreign Key (book_id) REFERENCES Books (book_id),
quantity DOUBLE
);
