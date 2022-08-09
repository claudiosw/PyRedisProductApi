# About the project
This is a project to practice Redis, testing, design patterns and clean code/architecture principles

# Preparing / Installing

### Clone the PyRedisProductApi repository
```
git clone https://github.com/claudiosw/PyRedisProductApi.git
```

### Access the project directory:
```
cd PyRedisProductApi
```

### Create the virtual environment:
```
python -m venv venv

```

### Run the virtual environment:
```
venv\Scripts\activate

```

### Install the required Python packages:
```
pip install -r requirements.txt
pre-commit install
```

### Create the database and the database structure:
```
python
>>> from src.infra.db.settings import *
>>> from src.infra.db.entities import *
>>> db_connection_handler.connect_to_db()
>>> engine = db_connection_handler.get_engine()
>>> Base.metadata.create_all(engine)
```