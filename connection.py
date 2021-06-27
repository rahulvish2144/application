import sqlalchemy, sqlalchemy.orm
from sqlalchemy import create_engine
from psycopg2 import DatabaseError
import app_settings as settings


def postgres_connection():
    """
    This function established the connection
    between api layer and Postgres database.

    :return: Session object
    """
    dialect  = settings.POSTGRES['dialect']
    driver   = settings.POSTGRES['driver']
    database = settings.POSTGRES['database']
    username = settings.POSTGRES['username']
    password = settings.POSTGRES['password']
    server   = settings.POSTGRES['host']
    port     = settings.POSTGRES['port']

    url = dialect + '+' + driver + '://' + username + ':' + password + '@' + server + ':' + port + '/' + database
    try:
        engine  = create_engine(url)
        session = sqlalchemy.orm.sessionmaker(bind= engine)
        session = session()

        return session
    except DatabaseError as connection_error:
        raise connection_error("Could not establish connection")
