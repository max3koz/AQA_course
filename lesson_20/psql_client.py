import logging
import psycopg2
from psycopg2._psycopg import connection, cursor
from psycopg2 import extensions


class PSQLClient:
    __connection: connection
    __cursor: cursor

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.__init__connection(self.dbname, self.user, self.password, self.host, self.port)
        self.__cursor = self.__connection.cursor()

    def __init__connection(self, dbname: str, user: str, password: str, host: str, port: int) -> None:
        try:
            auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            self.__connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            self.__connection.set_isolation_level(auto_commit)
        except (Exception, psycopg2.errors) as error:
            logging.error("Error in connection PostgreSQL progress")

    @property
    def connection(self) -> connection:
        return self.__connection

    @property
    def cursor(self) -> cursor:
        return self.__cursor

    def execute_data_db(self, query: str) -> list:
        self.__cursor.execute(query)
        #return self.__cursor.fetchall()

    def close_connection(self):
        self.__cursor.close()
        self.__connection.close()
