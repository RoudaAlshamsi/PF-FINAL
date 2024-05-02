class Person:
    """class to represent a person"""

    def __init__(self, name, address, contactDetails):
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails

    # setter and getter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # setter and getter for address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # setter and getter for contactDetails
    def get_contactDetails(self):
        return self.__contactDetails

    def set_contactDetails(self, contactDetails):
        self.__contactDetails = contactDetails
