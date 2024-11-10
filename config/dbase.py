import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../db.sqlite'
sqlite_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), sqlite_file_name)

db_url = f'sqlite:///{sqlite_file_path}'

engine = create_engine(db_url, echo=True)
session = sessionmaker(bind=engine)
base = declarative_base()