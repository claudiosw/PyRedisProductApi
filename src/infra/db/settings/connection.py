from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.configs.database_configs import database_infos


class __DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}:///{}".format(
            database_infos["TYPE"],
            database_infos["DB_NAME"]
        )
        self.engine = None
        self.session = None

    def connect_to_db(self):
        self.engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = __DBConnectionHandler()
