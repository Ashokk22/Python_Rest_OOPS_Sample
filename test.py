"""
Test Cases. You can see its working on command prompt with good comments.
"""

from admin import Admin

# Creating an Admin object
a = Admin()


# To fetch all the details of employees from an open source dummy url.
# Here we are printing first 5 employees info as a dictionary which can be used in further operations as per design.
print("\n\n---------- Fetching all available employees in the system ----------------")
employees = a.interface.get_employees()
print(employees)


# To add 1 employee using REST. Let that employee have name= 'Clark', salary='20000', age=50
print("\n\n------------- Adding one new employee -----------------")
emp_added = a.interface.add_employee(name='Steven', salary='20000', age=50)
# showing info of the employee added.
print(emp_added)


# To fetch one employee using its id. Lets fetch the employee we added in last step
print("\n\n--------- Fetching the newly added employee using its emp id ----------")
emp = a.interface.get_employee(emp_id=emp_added['id'])
print(emp)


# Lets update the newly created employee to its new info
print("\n\n--------- Updating the newly added employee with new info -------------")
emp_updated = a.interface.update_employee(emp_id=emp_added['id'], name='Damon', salary='50000', age=30)
print(emp_updated)


# To fetch one employee using its id. Lets fetch the employee we updated in last step to see if it updated in backend
print("\n\n---------------Fetching the newly added updated employee info ----------------")
emp_up = a.interface.get_employee(emp_id=emp_added['id'])
print(emp_up)


# To detele the above newly created employee
print("\n\n-------------- Deleting the newly added employee using its emp id ------------------")
delete_emp = a.interface.delete_employee(emp_id=emp_added['id'])
if delete_emp:
    print("The employee is deleted successfully")


# Lets again try to fetch the employee we deleted just now in last step.
print("\n\n---------------Trying to fetch the deleted employee --------------------- ")
emp = a.interface.get_employee(emp_id=emp_added['id'])
if not emp:
    print("The employee is not available in the system")

