class Client:
    """class to represent a client"""

    def __init__(self, clientID, name, address, contactDetails, budget, eventsOrganized):
        self.__clientID = clientID
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails
        self.__budget = budget
        self.__eventsOrganized = eventsOrganized

    # setter and getter for clientID
    def get_clientID(self):
        return self.__clientID

    def set_clientID(self, clientID):
        self.__clientID = clientID

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

    # setter and getter for budget
    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        self.__budget = budget

    # setter and getter for eventsOrganized
    def get_eventsOrganized(self):
        return self.__eventsOrganized

    def set_eventsOrganized(self, eventsOrganized):
        self.__eventsOrganized = eventsOrganized
