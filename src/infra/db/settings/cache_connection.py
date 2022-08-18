from redis import Redis
from src.configs.cache_configs import cache_infos


class __CacheConnectionHandler:

    def __init__(self) -> None:
        self.__cache_host = cache_infos["CACHE_SERVER_HOST"]
        self.__cache_port = cache_infos["CACHE_SERVER_PORT"]
        self.connection = None

    def connect_to_cache(self):
        self.connection = Redis(host=self.__cache_host, port=self.__cache_port, db=0, decode_responses=True)

    def get_connection(self):
        return self.connection


cache_connection_handler = __CacheConnectionHandler()
