from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    # csv to df
    data = pd.read_csv('./res/csv/government-2022-01-en-head.csv',
        encoding = 'utf-8')
    
    is_securities = data['main-type'] == '증권'
    securities = data[is_securities]
    print(securities)

    return {"data": "data"}