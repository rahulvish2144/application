from fastapi_utils.api_model import APIModel
from pydantic import EmailStr


class EmployeeModel(APIModel):
    emp_id              : int
    name_prefix         : str
    first_name          : str
    middle_initial      : str
    last_name           : str
    gender              : str
    email               : EmailStr
    father_name         : str
    mother_name         : str
    maiden_name_mother  : str
    dob                 : str
    birth_time          : str
    age_in_years        : float
    weight_in_kg        : int
    joining_date        : str
    joining_quarter     : str
    joining_half        : str
    joining_year        : int
    joining_month       : int
    joining_month_name  : str
    short_month         : str
    joining_day         : int
    joining_dow         : str
    short_dow           : str
    company_age_in_years: float
    salary              : int
    percentage_hike     : int
    ssn                 : str
    phone_number        : str
    place_name          : str
    country             : str
    city                : str
    state               : str
    zip                 : int
    region              : str
    user_name           : str
    password            : str
