"""
This is a REST interface class exposing the different REST operations.
It will be specific to a single entity type i.e. Employee.
Hence all methods related to employee will be defined in this class.
"""

import requests
from Rest.base import Base


class EmployeeRestInterface(Base):

    def get_employees(self):
        """
        This method fetches all the employee info
        :return: A dictionary containing the employees info
        """
        self.do_nothing()
        print("Fetching data for all the employees")
        url = 'http://dummy.restapiexample.com/api/v1/employees'
        response = requests.get(url)
        if response.status_code != 200:
            print("The REST GET url for fetching all employees demp_idn't respond correctly !!!")
            return []
        else:
            print("The REST GET call for fetching employee details executed successfully")
            print("Returning only first 5 employees")
            return response.json()[:5]

    def get_employee(self, emp_id):
        """
        This method fetches the employee info based on its emp_id.
        :param emp_id: integer, emp_id of the employee for whom data is to be fetched
        :return: A dictionary containing info for an employee
        """
        self.do_nothing()
        emp_id = str(emp_id)
        print("Fetching data for an employee emp_id "+emp_id)
        url = 'http://dummy.restapiexample.com/api/v1/employee/'+emp_id
        response = requests.get(url)
        if response.status_code != 200:
            print("The REST GET url for fetching an employee info for ["+emp_id+"] demp_idn't respond correctly !!!")
            return {}
        else:
            print("The REST GET call for fetching an employee details executed successfully")
            print("Returning the info for employee emp_id ["+emp_id+"]")
            return response.json()

    def add_employee(self, name, salary, age):
        """
        This method add a new employee into the system
        :param name: string, name of the employee
        :param salary: str, salary of the employee
        :param age: int, age of the employee
        :return: A dictionary containing the info of the employee added
        """
        self.do_nothing()
        print("Adding a new employee into the database")
        data = {'name': name, 'salary': salary, 'age': age}
        url = 'http://dummy.restapiexample.com/api/v1/create'
        response = requests.post(url, json=data)
        if response.status_code != 200:
            print("The REST POST url for adding an employee demp_idn't respond correctly and employee is not added !!!")
            return {}
        else:
            print("The REST POST call for adding an employee executed successfully")
            print("Returning the info for employee added")
            return response.json()

    def update_employee(self, emp_id, name, salary, age):
        """
        This method add a new employee into the system
        :param emp_id: int, emp_id of the employee whose details to be updated
        :param name: string, name of the employee
        :param salary: str, salary of the employee
        :param age: int, age of the employee
        :return: A dictionary containing the info of the employee updated
        """
        self.do_nothing()
        emp_id = str(emp_id)
        print("Updating employee ["+emp_id+"] info into the database")
        data = {'name': name, 'salary': salary, 'age': age}
        url = 'http://dummy.restapiexample.com/api/v1/update/'+emp_id
        response = requests.put(url, json=data)
        if response.status_code != 200:
            print("The REST PUT url for updating an employee ["+emp_id+"] demp_idn't respond correctly !!!")
            return {}
        else:
            print("The REST PUT call for updating an employee ["+emp_id+"] executed successfully")
            print("Returning the info for employee updated")
            return response.json()

    def delete_employee(self, emp_id):
        """
        This method add a new employee into the system
        :param emp_id: int, emp_id of the employee to be deleted
        :return: Boolean, True is deleted otherwise False
        """
        self.do_nothing()
        emp_id = str(emp_id)
        print("Deleting employee ["+emp_id+"] info")
        url = 'http://dummy.restapiexample.com/api/v1/delete/'+emp_id
        response = requests.delete(url)
        if response.status_code != 200:
            print("The REST DELETE url for deleting an employee ["+emp_id+"] demp_idn't respond correctly !!!")
            return False
        else:
            print("The REST DELETE call for deleting an employee ["+emp_id+"] executed successfully")
            return True
