class Caterer:
    """class to represent a caterer"""

    def __init__(self, catererID, name, address, contactDetails, menu, minimumNumberOfGuests, maximumNumberOfGuests):
        self.__catererID = catererID
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails
        self.__menu = menu
        self.__minimumNumberOfGuests = minimumNumberOfGuests
        self.__maximumNumberOfGuests = maximumNumberOfGuests

    # setter and getter for catererID
    def get_catererID(self):
        return self.__catererID

    def set_catererID(self, catererID):
        self.__catererID = catererID

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

    # setter and getter for menu
    def get_menu(self):
        return self.__menu

    def set_menu(self, menu):
        self.__menu = menu

    # setter and getter for minimumNumberOfGuests
    def get_minimumNumberOfGuests(self):
        return self.__minimumNumberOfGuests

    def set_minimumNumberOfGuests(self, minimumNumberOfGuests):
        self.__minimumNumberOfGuests = minimumNumberOfGuests

    # setter and getter for maximumNumberOfGuests
    def get_maximumNumberOfGuests(self):
        return self.__maximumNumberOfGuests

    def set_maximumNumberOfGuests(self, maximumNumberOfGuests):
        self.__maximumNumberOfGuests = maximumNumberOfGuests
