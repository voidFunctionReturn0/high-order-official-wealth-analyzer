from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine
from res.contants import SQLALCHEMY_DATABASE_URL
import logging

app = FastAPI()

@app.get("/")
async def root():
    # csv to df
    df = pd.read_csv('./res/csv/government-2022-01-en-head.csv',
        encoding = 'utf-8')


    # csv -> postgres
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    df.to_sql('asset', con = engine, if_exists='append')
    print(engine.execute("SELECT * FROM asset").fetchone())


    return {"data": "data"}