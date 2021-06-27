from fastapi import FastAPI, Query, File
from typing import Optional
from fastapi_utils.cbv import cbv as class_based_views
from fastapi.responses import JSONResponse
from time import time as time
from fastapi import status
from fastapi.encoders import jsonable_encoder

from views_service import *
from response_model import *

app = FastAPI()


@class_based_views(app)
class HRMSAppController:
    @app.get('/hrms/lists')
    async def get_emp_list(self, filter: Optional[int] = Query(None)):
        """
        This API end point is for fetching the list of employee.
        For fetching any specific employee detail just pass the employee id
        otherwise just pass None.

        :param filter: Employee Id or None
        :return: List of all the employees or any specific employee detail
        """
        __service_response = HRMSAppService()
        response = jsonable_encoder(__service_response.get_emp_list(filter))

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : '',
            'data'      : response
        })

    @app.post('/hrms/add')
    async def insert_emp_list(self, request_body: EmployeeModel):
        """
        This API end point is for adding any employee record into the database

        :param request_body: Details of the employee to be saved
        :return: Message saying whether the details are saved into the  database or not
        """
        __service_response = HRMSAppService()
        response = __service_response.insert_emp_list(request_body)

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : response,
            'data'      : None
        })

    @app.put('/hrms/update')
    async def update_emp_list(self, request_body: EmployeeModel):
        """
        This API end point is for update any specific employee details

        :param request_body: Details to be updated
        :return: Message saying whether the update was successful or not
        """
        __service_response = HRMSAppService()
        response = __service_response.update_emp_list(request_body)

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : response,
            'data'      : None
        })

    @app.delete('/hrms/delete')
    async def delete_emp_list(self, request_body: EmployeeModel):
        """
        This API end point is for delete a employee record

        :param request_body: Must Contain have employee id, SSN, Phone Number
        :return: Message saying whether the deletion has been done or not
        """
        __service_response = HRMSAppService()
        response = __service_response.delete_emp_list(request_body)

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : response,
            'data'      : None
        })

    @app.get('/hrms/{calculator}')
    async def calculator(self, calculator: str, emp_id: int, rating: Optional[int] = Query(None)):
        """
        This API end point is for calculating the hike/ bonus of an employee
        and update the corresponding details into the database.

        :param calculator: Pass bonus/ hike
        :param emp_id: Id for which the calculation has to be made
        :param rating: Between 1 to 10
        :return: Message saying how much bonus/ hike an employee is getting
        """
        __service_response = HRMSAppService()
        response = __service_response.calculator(calculator, emp_id, rating)

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : response,
            'data'      : None
        })

    @app.post('/hrms/bulk-insert')
    async def bulk_insert(self, file: bytes = File(default = None)):
        """
        This API end point is for insert bulk employee details into the database

        :param file: File to be saved
        :return: Message saying whether the file records has been saved into the database or not
        """
        __service_response = HRMSAppService()
        response = __service_response.bulk_insert(file)

        return JSONResponse({
            'time_stamp': int(time() * 1000),
            'status'    : status.HTTP_200_OK,
            'message'   : response,
            'data'      : None
        })

