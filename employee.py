class Employee:
    """class to represent an employee"""
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, workingHours):
        self.__name = name
        self.__employeeID = employeeID
        self.__department = department
        self.__jobTitle = jobTitle
        self.__basicSalary = basicSalary
        self.__age = age
        self.__dateOfBirth = dateOfBirth
        self.__passportDetails = passportDetails
        self.__workingHours = workingHours

#setter and getter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

#setter and getter for employeeID
    def get_employeeID(self):
        return self.__employeeID

    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

#setter and getter for department
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

#setter and getter for jobTitle
    def get_jobTitle(self):
        return self.__jobTitle

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

#setter and getter for basicSalary
    def get_basicSalary(self):
        return self.__basicSalary

    def set_basicSalary(self, basicSalary):
        self.__basicSalary = basicSalary

#setter and getter for age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

#setter and getter for dateOfBirth
    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

#setter and getter for passportDetails
    def get_passportDetails(self):
        return self.__passportDetails

    def set_passportDetails(self, passportDetails):
        self.__passportDetails = passportDetails

#setter and getter for workingHours
    def get_workingHours(self):
        return self.__workingHours

    def set_workingHours(self, workingHours):
        self.__workingHours = workingHours