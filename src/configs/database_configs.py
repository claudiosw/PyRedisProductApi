import os

database_infos = {
    "TYPE": os.getenv("DATABASE_TYPE"),
    "DB_NAME": os.getenv("DATABASE_DB_NAME")
}
