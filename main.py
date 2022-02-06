from fastapi import Depends, FastAPI
from modules import db, db_crud
from modules.db import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
@app.on_event("startup")
async def startup_event():
    db.init_db(Depends(get_db))
'''

@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown\n")


@app.get("/")
async def root():
    return {"request": "success"}


@app.get("/official/{idx}")
async def official(idx: int, db: Session = Depends(get_db)):
    return {"request": db_crud.get_asset(db=db, idx=idx)}