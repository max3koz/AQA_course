import logging
import pathlib
import subprocess

from logging import config
from lesson_20.psql_client import PSQLClient

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

# subprocess.run("sudo systemctl start postgresql", shell=True)

dbname_db = "postgres"
user = "postgres"
password = "12345678"
host = "127.0.0.1"
port = 5432

client_db = PSQLClient(dbname=dbname_db,
                    user=user,
                    password=password,
                    host=host,
                    port=port)

cursor_db = client_db.cursor

table_db = client_db.execute_data_db("CREATE DATABASE fish_shop;")

dbname = "fish_shop"
user = "mtrykoz"
# password = "12345678"
# host = "127.0.0.1"
# port = 5432

client = PSQLClient(dbname=dbname,
                    user=user,
                    password=password,
                    host=host,
                    port=port)

cursor = client.cursor

table1 = client.execute_data_db("CREATE TABLE categories (id SERIAL PRIMARY KEY, category_name VARCHAR(100));")
table2 = client.execute_data_db("CREATE TABLE products (id SERIAL PRIMARY KEY, category_id INT "
                                "REFERENCES categories(id), name VARCHAR(100), description VARCHAR(300), "
                                "price INTEGER);")

cat1 = client.execute_data_db("INSERT INTO categories (category_name) VALUES ('Fishing tackle');")
cat2 = client.execute_data_db("INSERT INTO categories (category_name) VALUES ('Fishing bait');")
cat3 = client.execute_data_db("INSERT INTO categories (category_name) VALUES ('Additional equipment');")

prod1 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('1', 'Rod 1000', 'Rod Super', '100');")
prod2 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('1', 'Rod 2000', 'Rod Super+', '200');")
prod3 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('2', 'Bait 1', 'Bait first fish', '2');")
prod4 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('2', 'Bait 2', 'Bait small fish', '3');")
prod5 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('2', 'Bait 3', 'Bait big fish', '30');")
prod6 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('3', 'Chair', 'Chair for fishing', '20');")
prod7 = client.execute_data_db("INSERT INTO products (category_id, name, description, price ) "
                                "VALUES ('3', 'Table', 'Table for fishing', '40');")

res = client.execute_data_db("SELECT category_name, name, price FROM products "
                             "JOIN categories ON products.category_id = categories.id;")
