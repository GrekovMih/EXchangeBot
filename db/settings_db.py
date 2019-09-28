# -*- encoding: utf-8 -*-
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER_PORT = 9003

DB_USER_NAME = 'postgres'
DB_USER_PASSWORD = '45091847'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'cracc'
DB_URL = 'postgres://{}:{}@{}:{}/{}'.format(DB_USER_NAME, DB_USER_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

db = create_engine(DB_URL)
Session = sessionmaker(bind=db)
session = Session()
