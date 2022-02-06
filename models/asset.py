from modules.db import Base
from sqlalchemy import Column, Integer, String, Date

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    belong = Column(String)
    job_title = Column(String)
    name = Column(String, index=True)
    main_type = Column(String)
    owner = Column(String)
    sub_type = Column(String)
    details = Column(String)
    value = Column(Integer)
    actual_price = Column(Integer)
    remarks = Column(String)
    date = Column(Date)