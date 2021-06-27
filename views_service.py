from fastapi.encoders import jsonable_encoder
from datetime import date
from dask import dataframe as dask_df


from views_dao import *


class HRMSAppService:
    def get_emp_list(self, filter):
        __dao_response = HRMSAppDAl()

        if filter is None:
            response = __dao_response.get_emp_list()
        elif filter is not None:
            response = __dao_response.get_emp_list(filter)

        return response

    def insert_emp_list(self, request_body):
        __dao_response  = HRMSAppDAl()
        response        = __dao_response.insert_emp_list(request_body)

        return response

    def update_emp_list(self, request_body):
        __dao_response  = HRMSAppDAl()
        response        = __dao_response.update_emp_list(request_body)

        return response

    def delete_emp_list(self, request_body):
        __dao_response  = HRMSAppDAl()
        response        = __dao_response.delete_emp_list(request_body)

        return response

    def calculator(self, calculator, emp_id, rating):
        __dao_response  = HRMSAppDAl()
        if calculator.upper() == 'hike'.upper() and rating is not None:
            message, hike = self.hike_calcuator(emp_id, rating)
            if rating >= 5 and hike is not None:
                __dao_response.update_hike(emp_id, hike)
        elif calculator.upper() == 'bonus'.upper() and rating is None:
            message = self.bonus_calculator(__dao_response, emp_id)

        return message

    def hike_calcuator(self, emp_id, rating):
        hike_meta_data = {
            '5' : '5%',
            '6' : '10%',
            '7' : '20%',
            '8' : '50%',
            '9' : '50%',
            '10': '75%'
        }
        message = ''
        if 1 <= rating <= 10:
            if str(rating) in hike_meta_data.keys():
                if hike_meta_data[str(rating)]:
                    message = '{} is eligible for '.format(emp_id) + '{}'.format(hike_meta_data[str(rating)]) + ' hike.'
                    hike = int(hike_meta_data[str(rating)].split('%')[0])
            else:
                message = '{} is terminated'.format(emp_id)
                hike = None
        else:
            message = 'Rating range should be in between (1, 10)'
            hike = None

        return message, hike

    def bonus_calculator(self, __dao_response, emp_id):
        result = jsonable_encoder(__dao_response.get_emp_list(emp_id))
        print(result['joining_year'], date.today().year)
        if (date.today().year - result['joining_year']) <= 5:
            bonus = 10
            message = '{} has been given {}% bonus'.format(emp_id, bonus)
        elif 6 <= (date.today().year - result['joining_year']) < 10:
            bonus = 20
            message = '{} has been given {}% bonus'.format(emp_id, bonus)
        elif 10 <= (date.today().year - result['joining_year']) < 20:
            bonus = 30
            message = '{} has been given {}% bonus'.format(emp_id, bonus)
        else:
            bonus = 50
            message = '{} has been given {}% bonus'.format(emp_id, bonus)

        return message

    def bulk_insert(self, file):
        data = dask_df.read_csv('resources/1000 Records.csv')
        __dao_response = HRMSAppDAl()
        response = __dao_response.bulk_operations(data)

        return response
