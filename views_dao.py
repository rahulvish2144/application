from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import aliased
import dask.bag as db
import pandas as pd


from connection import *
from model import *


class HRMSAppDAl:
    def __init__(self):
        """
        This is Data Access Layer, responsible for the interaction between
        the API layer & database layer.
        """
        self.__session = None

    def get_emp_list(self, filter = None):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        if filter is None:
            query = self.__session.query(
                emp
            ).all()

        elif filter is not None:
            query = self.__session.query(
                emp
            ).filter(
                emp.emp_id == filter
            ).one_or_none()

        self.__session.close()

        return query

    def insert_emp_list(self, request_body):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        query = self.__session.query(
            emp
        ).filter(
            emp.emp_id          == request_body.emp_id,
            emp.phone_number    == request_body.phone_number,
            emp.ssn             == request_body.ssn
        ).first()
        self.__session.close()

        if query is None:
            self.__session = postgres_connection()
            tbl_data = TblEmployee(
                emp_id                  = request_body.emp_id,
                name_prefix             = request_body.name_prefix,
                first_name              = request_body.first_name,
                middle_initial          = request_body.middle_initial,
                last_name               = request_body.last_name,
                gender                  = request_body.gender,
                email                   = request_body.email,
                father_name             = request_body.father_name,
                mother_name             = request_body.mother_name,
                maiden_name_mother      = request_body.maiden_name_mother,
                dob                     = request_body.dob,
                birth_time              = request_body.birth_time,
                age_in_years            = request_body.age_in_years,
                weight_in_kg            = request_body.weight_in_kg,
                joining_date            = request_body.joining_date,
                joining_quarter         = request_body.joining_quarter,
                joining_half            = request_body.joining_half,
                joining_year            = request_body.joining_year,
                joining_month           = request_body.joining_month,
                joining_month_name      = request_body.joining_month_name,
                short_month             = request_body.short_month,
                joining_day             = request_body.joining_day,
                joining_dow             = request_body.joining_dow,
                short_dow               = request_body.short_dow,
                company_age_in_years    = request_body.company_age_in_years,
                salary                  = request_body.salary,
                percentage_hike         = request_body.percentage_hike,
                ssn                     = request_body.ssn,
                phone_number            = request_body.phone_number,
                place_name              = request_body.place_name,
                country                 = request_body.country,
                city                    = request_body.city,
                state                   = request_body.state,
                zip                     = request_body.zip,
                region                  = request_body.region,
                user_name               = request_body.user_name,
                password                = request_body.password
            )
            self.__session.add(tbl_data)
            self.__session.commit()
            self.__session.close()

            return 'Details entered successfully'
        else:
            return 'Details already exists'

    def update_emp_list(self, request_body):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        query = self.__session.query(
            emp
        ).filter(
            emp.emp_id          == request_body.emp_id,
            emp.ssn             == request_body.ssn,
            emp.phone_number    == request_body.phone_number
        ).first()

        query.name_prefix             = request_body.name_prefix
        query.first_name              = request_body.first_name
        query.middle_initial          = request_body.middle_initial
        query.last_name               = request_body.last_name
        query.gender                  = request_body.gender
        query.email                   = request_body.email
        query.father_name             = request_body.father_name
        query.mother_name             = request_body.mother_name
        query.maiden_name_mother      = request_body.maiden_name_mother
        query.dob                     = request_body.dob
        query.birth_time              = request_body.birth_time
        query.age_in_years            = request_body.age_in_years
        query.weight_in_kg            = request_body.weight_in_kg
        query.joining_date            = request_body.joining_date
        query.joining_quarter         = request_body.joining_quarter
        query.joining_half            = request_body.joining_half
        query.joining_year            = request_body.joining_year
        query.joining_month           = request_body.joining_month
        query.joining_month_name      = request_body.joining_month_name
        query.short_month             = request_body.short_month
        query.joining_day             = request_body.joining_day
        query.joining_dow             = request_body.joining_dow
        query.short_dow               = request_body.short_dow
        query.company_age_in_years    = request_body.company_age_in_years
        query.salary                  = request_body.salary
        query.percentage_hike         = request_body.percentage_hike
        query.place_name              = request_body.place_name
        query.country                 = request_body.country
        query.city                    = request_body.city
        query.state                   = request_body.state
        query.zip                     = request_body.zip
        query.region                  = request_body.region
        query.user_name               = request_body.user_name
        query.password                = request_body.password
        self.__session.commit()
        self.__session.close()

        return 'Successfully updated'

    def delete_emp_list(self, request_body):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        query = self.__session.query(
            emp
        ).filter(
            emp.emp_id          == request_body.emp_id,
            emp.ssn             == request_body.ssn,
            emp.phone_number    == request_body.phone_number
        ).delete(synchronize_session = False)
        self.__session.commit()
        self.__session.close()

        if query != 0:
            return 'Record deleted successfully'
        else:
            return 'No record exists to be deleted'

    def update_hike(self, emp_id, hike):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        query = self.__session.query(
            emp
        ).filter(
            emp.emp_id == emp_id
        ).first()

        last_salary = jsonable_encoder(query)['salary']
        query.salary += last_salary * hike/ 100
        query.percentage_hike = hike
        self.__session.commit()
        self.__session.close()

        return 'Salary updated'

    def update_bonus(self, emp_id, hike):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        query = self.__session.query(
            emp
        ).filter(
            emp.emp_id == emp_id
        ).first()

        last_salary = jsonable_encoder(query)['salary']
        query.salary += last_salary * hike/ 100
        query.percentage_hike = hike
        self.__session.commit()
        self.__session.close()

        return 'Salary updated'

    def bulk_operations(self, data):
        emp = aliased(TblEmployee)

        self.__session = postgres_connection()
        data = db.from_delayed(data.map_partitions(pd.DataFrame.to_dict, orient = 'records').to_delayed())
        self.__session.bulk_insert_mappings(emp, data)
        self.__session.commit()
        self.__session.close()

        return 'Details entered successfully'
