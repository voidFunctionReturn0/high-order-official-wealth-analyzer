import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from res.contants import SQLALCHEMY_DATABASE_URL
#from models import asset
#from sqlalchemy.orm import Session


# csv -> df
df = pd.read_csv(
    './res/csv/goverment-2022-01-en-head.csv',
    encoding = 'utf-8')

# df -> postgres
Engine = create_engine(SQLALCHEMY_DATABASE_URL)


df.to_sql(
    name = 'assets',
    con = Engine,
    if_exists = 'replace',
    index = True,
    index_label = 'id',
    dtype = {
        'id': sqlalchemy.types.INTEGER(),
        'belong': sqlalchemy.types.VARCHAR(100),
        'job_title': sqlalchemy.types.VARCHAR(100),
        'name': sqlalchemy.types.VARCHAR(100),
        'main_type': sqlalchemy.types.VARCHAR(100),
        'owner': sqlalchemy.types.VARCHAR(100),
        'sub_type': sqlalchemy.types.VARCHAR(100),
        'details': sqlalchemy.types.TEXT(),
        'value': sqlalchemy.types.INTEGER(),
        'actual_price': sqlalchemy.types.INTEGER(),
        'remarks': sqlalchemy.types.VARCHAR(100),
        'date': sqlalchemy.types.Date()
    })

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = Engine)


Base = declarative_base()