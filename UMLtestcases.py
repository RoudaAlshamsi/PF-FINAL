from employee import Employee
from client import Client
from guest import Guest
from event import Event
from venue import Venue

def main():

    #create an employee
    employee = Employee("Omar", "EMP001", "Sales", "SalesPerson", 50000, 30, "11-12-1999", "AB12345", 40)
    print("Employee:", employee.get_name())

    #create a client
    client = Client("CL001", "Fatima", "Main Street", "0501234567", 10000, "Wedding")
    print("Client:", client.get_name())

    #create a guest
    guest = Guest("GUEST001", "Ahmed", "456 Street", "0551223908", "Birthday Party")
    print("Guest:", guest.get_name())

    #create an event
    event = Event("EVT001", "Wedding", "Red Roses", "2-5-2024", "18:00", "4 hours", "Park Avenue", client.get_clientID(), [guest], "AbuDhabi Catering", "BestClean", "Parties101", "4Fun", "Ceremony 1 for Furniture", "Invoice with terms and conditions", 75000)
    event.confirm_event()
    print("Event type:", event.get_type())

    #create a venue
    venue = Venue("VEN001", "Grand Ballroom", "Park Avenue", "0504738926", "Full menu", 50, 200, 100)
    print("Venue name:", venue.get_name())

if __name__ == "__main__":
    main()