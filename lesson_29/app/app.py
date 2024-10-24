import os
import time

import psycopg2
import docker
from psycopg2 import OperationalError


def connect():
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                database="testdb",
                user="postgres",
                password="yourpassword",
                host="db",
                port="5432"
            )
            return conn
        except OperationalError:
            print("Don`t possible to connect to DB? try again!!!")
            time.sleep(5)


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(100));")
    conn.commit()
    conn.close()


def insert_record(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def update_record(record_id, new_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE test SET name = %s WHERE id = %s;", (new_name, record_id))
    conn.commit()
    conn.close()


def delete_record(record_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test WHERE id = %s;", (record_id,))
    conn.commit()
    conn.close()


def select_records():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test;")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Функція для отримання Volumes з конфігурації контейнера
def get_container_volumes(container):
    container_config = container.image_config.get('ContainerConfig', {})
    volumes = container_config.get('Volumes', {})
    return volumes


# Приклад використання:
if __name__ == "__main__":
    client = docker.from_env()
    container = client.containers.run("postgres", detach=True)

    volumes = get_container_volumes(container)
    print(volumes)
