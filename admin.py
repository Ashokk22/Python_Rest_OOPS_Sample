"""
It is an Admin class which is a driver class for the operations.
Admin has an ability to fetch/alter the details of employee(s).
The access to employee methods are saved in its 'interface' variable.
"""

from Rest.rest_interface import EmployeeRestInterface
from Rest.base import Base


class Admin(Base):

    def __init__(self):
        """
        This is an Admin object constructor
        """
        # Storing the REST interface object in a variable.
        #  The interface methods will be exposed to Admin through this variable.
        self.interface = EmployeeRestInterface()
