class Event:
    """class to represent an event"""
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, guestList, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice, totalCost):
        self.__eventID = eventID
        self.__type = type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientID = clientID
        self.__guestList = guestList
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice
        self.__totalCost = totalCost

#setter and getter for eventID
    def get_eventID(self):
        return self.__eventID

    def set_eventID(self, eventID):
        self.__eventID = __eventID

#setter and getter for type
    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

#setter and getter for theme
    def get_theme(self):
        return self.__theme

    def set_theme(self, theme):
        self.__theme = theme

#setter and getter for date
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

#setter and getter for time
    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

#setter and getter for duration
    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

#setter and getter for venueAddress
    def get_venueAddress(self):
        return self.__venueAddress

    def set_venueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

#setter and getter for clientID
    def get_clientID(self):
        return self.__clientID

    def set_clientID(self, clientID):
        self.__clientID = clientID

#setter and getter for guestList
    def get_guestList(self):
        return self.__guestList

    def set_guestList(self, guestList):
        self.__guestList = guestList

#setter and getter for cateringCompany
    def get_cateringCompany(self):
        return self.__cateringCompany

    def set_cateringCompany(self, cateringCompany):
        self.__cateringCompany = cateringCompany

#setter and getter for cleaningCompany
    def get_cleaningCompany(self):
        return self.__cleaningCompany

    def set_cleaningCompany(self, cleaningCompany):
        self.__cleaningCompany = cleaningCompany

#setter and getter for decorationsCompany
    def get_decorationsCompany(self):
        return self.__decorationsCompany

    def set_decorationsCompany(self, decorationsCompany):
        self.__decorationsCompany = decorationsCompany

#setter and getter for entertainmentCompany
    def get_entertainmentCompany(self):
        return self.__entertainmentCompany

    def set_entertainmentCompany(self, type):
        self.__entertainmentCompany = entertainmentCompany

#setter and getter for furnitureSupplyCompany
    def get_furnitureSupplyCompany(self):
        return self.__furnitureSupplyCompany

    def set_furnitureSupplyCompany(self, furnitureSupplyCompany):
        self.__furnitureSupplyCompany = furnitureSupplyCompany

#setter and getter for invoice
    def get_invoice(self):
        return self.__invoice

    def set_invoice(self, invoice):
        self.__invoicee = invoice

#setter and getter for totalCost
    def get_totalCost(self):
        return self.__totalCost

    def set_totalCost(self, totalCost):
        self.__totalCost = totalCost

    def confirm_event(self):
        print("Event confirmed.")

    def cancel_event(self):
        print("Event canceled.")
