import mysql.connector as connector

connection = connector.connect(user="root", password="Password100$")

cursor = connection.cursor()

create_database_query = """CREATE DATABASE little_lemon"""

cursor.execute(create_database_query)

use_database_query = """USE little_lemon"""

cursor.execute(use_database_query)

create_menuitem_table ="""
CREATE TABLE MenuItems(
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY(ItemID)
)

cursor.execute(create_menuitem_table)


"""