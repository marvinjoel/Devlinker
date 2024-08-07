import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://%s:%s@%s:%d/%s' % (
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_HOST'),
    int(os.getenv('POSTGRES_PORT')),
    os.getenv('POSTGRES_DB')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
Session_all = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def db_session():
    return Session_all()