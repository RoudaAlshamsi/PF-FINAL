class Guest:
    """class to represent a guest"""

    def __init__(self, guestID, name, address, contactDetails, eventsAttended):
        self.__clientID = guestID
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails
        self.__eventsAttended = eventsAttended

    # setter and getter for guestID
    def get_guestID(self):
        return self.__guestID

    def set_guestID(self, guestID):
        self.__guestID = guestID

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

    # setter and getter for eventsAttended
    def get_eventsAttended(self):
        return self.__eventsAttended

    def set_eventsAttended(self, eventsAttended):
        self.__eventsAttended = eventsAttended