from sqlalchemy import Column, Integer, Float, Text, text, VARCHAR, Boolean, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class TblEmployee(Base):
    __tablename__ = "tbl_employee"

    seq                     = Column(
        Integer,
        primary_key = True,
        server_default = text("nextval('tbl_employee_seq_seq'::regclass)")
    )
    emp_id                  = Column(Integer)
    name_prefix             = Column(Text)
    first_name              = Column(Text)
    middle_initial          = Column(Text)
    last_name               = Column(Text)
    gender                  = Column(Text)
    email                   = Column(Text)
    father_name             = Column(Text)
    mother_name             = Column(Text)
    maiden_name_mother      = Column(Text)
    dob                     = Column(Text)
    birth_time              = Column(Text)
    age_in_years            = Column(Float)
    weight_in_kg            = Column(Integer)
    joining_date            = Column(Text)
    joining_quarter         = Column(Text)
    joining_half            = Column(Text)
    joining_year            = Column(Integer)
    joining_month           = Column(Integer)
    joining_month_name      = Column(Text)
    short_month             = Column(Text)
    joining_day             = Column(Integer)
    joining_dow             = Column(Text)
    short_dow               = Column(Text)
    company_age_in_years    = Column(Float)
    salary                  = Column(Integer)
    percentage_hike         = Column(Integer)
    ssn                     = Column(Text)
    phone_number            = Column(Text)
    place_name              = Column(Text)
    country                 = Column(Text)
    city                    = Column(Text)
    state                   = Column(Text)
    zip                     = Column(Integer)
    region                  = Column(Text)
    user_name               = Column(Text)
    password                = Column(Text)
    created_date            = Column(DateTime(timezone = False), default = datetime.now())
