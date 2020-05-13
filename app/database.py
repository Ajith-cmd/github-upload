from sqlalchemy import create_engine
from sqlalchemy.sql.schema import Column,Sequence
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine=create_engine("sqlite:///todo.db",echo=True)
Session=sessionmaker(bind=engine)

Base=declarative_base()

