from pony.orm import Database

class PonyOrmDbClient:

    __db: Database

    def __init__(self, provider: str, user: str, password: str, host: str, database: str):
        self.__db = Database(provider=provider,
                             user=user,
                             password=password,
                             host=host,
                             database=database)
    @property
    def db(self) -> Database:
        return self.__db
