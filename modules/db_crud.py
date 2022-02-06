from sqlalchemy.orm import Session
from models import asset


def get_asset(db: Session, idx: int):
    return db.query(asset.Asset).filter(asset.Asset.id == idx).first()