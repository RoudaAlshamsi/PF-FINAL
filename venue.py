class Venue:
    """class to represent a venue"""

    def __init__(self, venueID, name, address, contact, menu, minimumNumberOfGuests, maximumNumberOfGuests, pricePerGuest):
        self.__venueID = venueID
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__menu = menu
        self.__minimumNumberOfGuests = minimumNumberOfGuests
        self.__maximumNumberOfGuests = maximumNumberOfGuests
        self.__pricePerGuest = pricePerGuest

    # setter and getter for venueID
    def get_venueID(self):
        return self.__clientID

    def set_venueID(self, venueID):
        self.__venueID = venueID

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

    # setter and getter for contact
    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

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

    # setter and getter for pricePerGuest
    def get_pricePerGuest(self):
        return self.__pricePerGuest

    def set_pricePerGuest(self, pricePerGuest):
        self.__pricePerGuest = pricePerGuest
