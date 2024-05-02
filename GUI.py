import tkinter as tk
import pickle

class EventManagementSystem:
    def __init__(self):
        self.events = []
        self.employees = []
        self.clients = []
        self.guests = []
        self.suppliers = []

    def load_data(self):
        try:
            with open("events.pkl", "rb") as f:
                self.events = pickle.load(f)
        except FileNotFoundError:
            pass

        try:
            with open("employees.pkl", "rb") as f:
                self.employees = pickle.load(f)
        except FileNotFoundError:
            pass

        try:
            with open("clients.pkl", "rb") as f:
                self.clients = pickle.load(f)
        except FileNotFoundError:
            pass

        try:
            with open("guests.pkl", "rb") as f:
                self.guests = pickle.load(f)
        except FileNotFoundError:
            pass

        try:
            with open("suppliers.pkl", "rb") as f:
                self.suppliers = pickle.load(f)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("events.pkl", "wb") as f:
            pickle.dump(self.events, f)

        with open("employees.pkl", "wb") as f:
            pickle.dump(self.employees, f)

        with open("clients.pkl", "wb") as f:
            pickle.dump(self.clients, f)

        with open("guests.pkl", "wb") as f:
            pickle.dump(self.guests, f)

        with open("suppliers.pkl", "wb") as f:
            pickle.dump(self.suppliers, f)

    def add_event(self, event):
        self.events.append(event)
        self.save_data()

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data()

    def add_client(self, client):
        self.clients.append(client)
        self.save_data()

    def add_guest(self, guest):
        self.guests.append(guest)
        self.save_data()

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
        self.save_data()

    def delete_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                self.events.remove(event)
                self.save_data()
                break

    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                self.save_data()
                break

    def delete_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                self.save_data()
                break

    def delete_guest(self, guest_id):
        for guest in self.guests:
            if guest.guest_id == guest_id:
                self.guests.remove(guest)
                self.save_data()
                break

    def delete_supplier(self, supplier_id):
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                self.suppliers.remove(supplier)
                self.save_data()
                break

    def display_events(self):
        for event in self.events:
            print(event)

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def display_clients(self):
        for client in self.clients:
            print(client)

    def display_guests(self):
        for guest in self.guests:
            print(guest)

    def display_suppliers(self):
        for supplier in self.suppliers:
            print(supplier)

class Event:
    def __init__(self, event_id, event_type, theme):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme

    def __str__(self):
        return f"Event ID: {self.event_id}, Type: {self.event_type}, Theme: {self.theme}"

class Employee:
    def __init__(self, employee_id, name, jobTitle):
        self.employee_id = employee_id
        self.name = name
        self.jobTitle = jobTitle

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Job Title: {self.jobTitle}"

class Client:
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}"

class Guest:
    def __init__(self, guest_id, name):
        self.guest_id = guest_id
        self.name = name

    def __str__(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}"

class Supplier:
    def __init__(self, supplier_id, service):
        self.supplier_id = supplier_id
        self.service = service

    def __str__(self):
        return f"Supplier ID: {self.supplier_id}, Service: {self.service}"

def add_event():
    event_id = event_id_entry.get()
    event_type = event_type_entry.get()
    theme = theme_entry.get()
    new_event = Event(event_id, event_type, theme)
    ems.add_event(new_event)
    event_info_label.config(text="Event added successfully.")

def add_employee():
    employee_id = employee_id_entry.get()
    name = name_entry.get()
    jobTitle = jobTitle_entry.get()
    new_employee = Employee(employee_id, name, jobTitle)
    ems.add_employee(new_employee)
    employee_info_label.config(text="Employee added successfully.")

def add_client():
    client_id = client_id_entry.get()
    name = client_name_entry.get()
    email = client_contact_entry.get()
    new_client = Client(client_id, name, email)
    ems.add_client(new_client)
    client_info_label.config(text="Client added successfully.")

def add_guest():
    guest_id = guest_id_entry.get()
    name = guest_name_entry.get()
    new_guest = Guest(guest_id, name)
    ems.add_guest(new_guest)
    guest_info_label.config(text="Guest added successfully.")

def add_supplier():
    supplier_id = supplier_id_entry.get()
    name = name_entry.get()
    service = service_entry.get()
    new_supplier = Supplier(supplier_id, name, service)
    ems.add_supplier(new_supplier)
    supplier_info_label.config(text="Supplier added successfully.")

def display_events():
    event_info_label.config(text="Events:")
    for event in ems.events:
        event_info_label.config(text=event_info_label.cget("text") + f"\n{event}")

def display_employees():
    employee_info_label.config(text="Employees:")
    for employee in ems.employees:
        employee_info_label.config(text=employee_info_label.cget("text") + f"\n{employee}")

def display_clients():
    client_info_label.config(text="Clients:")
    for client in ems.clients:
        client_info_label.config(text=client_info_label.cget("text") + f"\n{client}")

def display_guests():
    guest_info_label.config(text="Guests:")
    for guest in ems.guests:
        guest_info_label.config(text=guest_info_label.cget("text") + f"\n{guest}")

def display_suppliers():
    supplier_info_label.config(text="Suppliers:")
    for supplier in ems.suppliers:
        supplier_info_label.config(text=supplier_info_label.cget("text") + f"\n{supplier}")

def modify_event():
    event_id = event_id_entry.get()
    event_type = event_type_entry.get()
    theme = theme_entry.get()
    # Here you would implement the modification logic for the event
    event_info_label.config(text="Event modified successfully.")

def modify_employee():
    employee_id = employee_id_entry.get()
    name = name_entry.get()
    jobTitle = jobTitle_entry.get()
    #implement the modification logic for the employee
    employee_info_label.config(text="Employee modified successfully.")

def modify_client():
    client_id = client_id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    #implement the modification logic for the client
    client_info_label.config(text="Client modified successfully.")

def modify_guest():
    guest_id = guest_id_entry.get()
    name = name_entry.get()
    event_id = event_id_entry.get()
    #implement the modification logic for the guest
    guest_info_label.config(text="Guest modified successfully.")

def modify_supplier():
    supplier_id = supplier_id_entry.get()
    name = name_entry.get()
    service = service_entry.get()
    #implement the modification logic for the supplier
    supplier_info_label.config(text="Supplier modified successfully.")

def delete_event():
    event_id = event_id_entry.get()
    ems.delete_event(event_id)
    event_info_label.config(text="Event deleted successfully.")

def delete_employee():
    employee_id = employee_id_entry.get()
    ems.delete_employee(employee_id)
    employee_info_label.config(text="Employee deleted successfully.")

def delete_client():
    client_id = client_id_entry.get()
    ems.delete_client(client_id)
    client_info_label.config(text="Client deleted successfully.")

def delete_guest():
    guest_id = guest_id_entry.get()
    ems.delete_guest(guest_id)
    guest_info_label.config(text="Guest deleted successfully.")

def delete_supplier():
    supplier_id = supplier_id_entry.get()
    ems.delete_supplier(supplier_id)
    supplier_info_label.config(text="Supplier deleted successfully.")

#create an instance of EventManagementSystem
ems = EventManagementSystem()
ems.load_data()

#GUI
root = tk.Tk()
root.title("Event Management System")

#Event Entry
event_id_label = tk.Label(root, text="Event ID:")
event_id_label.grid(row=0, column=0)
event_id_entry = tk.Entry(root)
event_id_entry.grid(row=0, column=1)

event_type_label = tk.Label(root, text="Event Type:")
event_type_label.grid(row=1, column=0)
event_type_entry = tk.Entry(root)
event_type_entry.grid(row=1, column=1)

theme_label = tk.Label(root, text="Theme:")
theme_label.grid(row=2, column=0)
theme_entry = tk.Entry(root)
theme_entry.grid(row=2, column=1)

add_event_button = tk.Button(root, text="Add Event", command=add_event)
add_event_button.grid(row=3, column=0)

display_event_button = tk.Button(root, text="Display Events", command=display_events)
display_event_button.grid(row=3, column=1)

modify_event_button = tk.Button(root, text="Modify Event", command=modify_event)
modify_event_button.grid(row=4, column=1)

delete_event_button = tk.Button(root, text="Delete Event", command=delete_event)
delete_event_button.grid(row=4, column=0)

event_info_label = tk.Label(root, text="")
event_info_label.grid(row=4, column=0, columnspan=2)

#Employee Entry
employee_id_label = tk.Label(root, text="Employee ID:")
employee_id_label.grid(row=5, column=0)
employee_id_entry = tk.Entry(root)
employee_id_entry.grid(row=5, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=6, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=6, column=1)

jobTitle_label = tk.Label(root, text="Job Title:")
jobTitle_label.grid(row=7, column=0)
jobTitle_entry = tk.Entry(root)
jobTitle_entry.grid(row=7, column=1)

add_employee_button = tk.Button(root, text="Add Employee", command=add_employee)
add_employee_button.grid(row=8, column=0)

display_employee_button = tk.Button(root, text="Display Employees", command=display_employees)
display_employee_button.grid(row=8, column=1)

modify_employee_button = tk.Button(root, text="Modify Employee", command=modify_employee)
modify_employee_button.grid(row=9, column=1)

delete_employee_button = tk.Button(root, text="Delete Employee", command=delete_employee)
delete_employee_button.grid(row=9, column=0)

employee_info_label = tk.Label(root, text="")
employee_info_label.grid(row=9, column=0, columnspan=2)

#Client Entry
client_id_label = tk.Label(root, text="Client ID:")
client_id_label.grid(row=10, column=0)
client_id_entry = tk.Entry(root)
client_id_entry.grid(row=10, column=1)

client_name_label = tk.Label(root, text="Client Name:")
client_name_label.grid(row=11, column=0)
client_name_entry = tk.Entry(root)
client_name_entry.grid(row=11, column=1)

client_contact_label = tk.Label(root, text="Client Contact:")
client_contact_label.grid(row=12, column=0)
client_contact_entry = tk.Entry(root)
client_contact_entry.grid(row=12, column=1)

add_client_button = tk.Button(root, text="Add Client", command=add_client)
add_client_button.grid(row=13, column=0)

display_client_button = tk.Button(root, text="Display Clients", command=display_clients)
display_client_button.grid(row=13, column=1)

modify_client_button = tk.Button(root, text="Modify Client", command=modify_client)
modify_client_button.grid(row=14, column=1)

delete_client_button = tk.Button(root, text="Delete Client", command=delete_client)
delete_client_button.grid(row=14, column=0)

client_info_label = tk.Label(root, text="")
client_info_label.grid(row=14, column=0, columnspan=2)

#Guest Entry
guest_id_label = tk.Label(root, text="Guest ID:")
guest_id_label.grid(row=15, column=0)
guest_id_entry = tk.Entry(root)
guest_id_entry.grid(row=15, column=1)

guest_name_label = tk.Label(root, text="Guest Name:")
guest_name_label.grid(row=16, column=0)
guest_name_entry = tk.Entry(root)
guest_name_entry.grid(row=16, column=1)

add_guest_button = tk.Button(root, text="Add Guest", command=add_guest)
add_guest_button.grid(row=17, column=0)

display_guest_button = tk.Button(root, text="Display Guests", command=display_guests)
display_guest_button.grid(row=17, column=1)

modify_guest_button = tk.Button(root, text="Modify Guest", command=modify_guest)
modify_guest_button.grid(row=18, column=1)

delete_guest_button = tk.Button(root, text="Delete Guest", command=delete_guest)
delete_guest_button.grid(row=18, column=0)

guest_info_label = tk.Label(root, text="")
guest_info_label.grid(row=18, column=0, columnspan=2)

#Supplier Entry
supplier_id_label = tk.Label(root, text="Supplier ID:")
supplier_id_label.grid(row=19, column=0)
supplier_id_entry = tk.Entry(root)
supplier_id_entry.grid(row=19, column=1)

service_label = tk.Label(root, text="Service:")
service_label.grid(row=20, column=0)
service_entry = tk.Entry(root)
service_entry.grid(row=20, column=1)

add_supplier_button = tk.Button(root, text="Add Supplier", command=add_supplier)
add_supplier_button.grid(row=21, column=0)

display_supplier_button = tk.Button(root, text="Display Suppliers", command=display_suppliers)
display_supplier_button.grid(row=21, column=1)

modify_supplier_button = tk.Button(root, text="Modify Supplier", command=modify_supplier)
modify_supplier_button.grid(row=22, column=1)

delete_supplier_button = tk.Button(root, text="Delete Supplier", command=delete_supplier)
delete_supplier_button.grid(row=22, column=0)

supplier_info_label = tk.Label(root, text="")
supplier_info_label.grid(row=22, column=0, columnspan=2)

root.mainloop()