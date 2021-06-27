------------------
 Introduction
------------------

This repository houses the minimal functionality of the HRMS(Employees Management System) with basic CRUD operation.

------------------
 Pre-requisites
------------------
The application needs the following requirements:
1. Python 3.x
2. FastAPI rest framework
3. PostgreSQL 9.6

------------------
 Setup Instruction
------------------

For setting up the application locally please follow the below steps:

> pip install -r requirements.txt

The above will install all the dependencies to run the application.

> uvicorn views:app --reload

To see all the api end points list goto
> host:port/docs

In the above command , please mention the host & port details based on how you configure application
to start.

The above command will run the application. For more usage of uvicorn
> uvicorn --help

------------------
 Author
------------------
Rahul Vishwakarma