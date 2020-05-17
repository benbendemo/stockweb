#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provide 2 ways to create airflow user.

After enter into docker-airflow postgres container, you can easily
use below to connect to db

psql -U airflow -h 127.0.0.1 -p 5432 -d airflow
psql -U docker -h 127.0.0.1 -p 5432 -d docker
psql -U postgres -h 127.0.0.1 -p 5432 -d postgres
"""

import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DB_TYPE = os.getenv('DB_TYPE', 'postgresql')
DB_PORT = os.getenv('DB_PORT', 5432)
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'stockdata')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

engine = create_engine(f'{DB_TYPE}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{DB_PORT}/{POSTGRES_DB}', echo=True)
print("engine:",engine.url)

if not database_exists(engine.url):
    try:
        create_database(engine.url)
    except Exception as e:
        print('error type:', type(e))
        print('error value:', e)
    else:
        print('create engine.url successfully')
else:
    print('engine.url already exist')

