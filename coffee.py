# import tkinter as tk
# from tkinter import ttk
# import mysql.connector as connector

# connection = connector.connect(host="localhost", user="root", password="Password100$", database="coffeefactorydb")
# cursor = connection.cursor()

# window = tk.Tk()
# window.title('Coffee Management Pixel')
# window.geometry('1920x1080')

# # Title
# title_label = ttk.Label(master=window, text="Coffee Management System", font="Algerian 25 bold")
# title_label.pack()

# # Input field
# input_frame = ttk.Frame(master=window)
# farmer_button = ttk.Button(master=input_frame, text='Farmer')
# sales_button = ttk.Button(master=input_frame, text='Sales')
# employee_button = ttk.Button(master=input_frame, text="Employees")
# farmer_button.pack()
# sales_button.pack()
# employee_button.pack()
# input_frame.pack()


# def open_employees():
#     employee_window = tk.Toplevel(window)
#     employee_window.title("Employees")

#     # Prompt for employee ID
#     employee_label = ttk.Label(master=employee_window, text="Enter Employee ID:")
#     employee_label.pack()
#     employee_entry = ttk.Entry(master=employee_window)
#     employee_entry.pack()

#     def handle_employees():
#         employee_id = employee_entry.get()
#         query = "SELECT * FROM employee WHERE id = %s"
#         query2 = "INSERT INTO employee(name, address, position, salary) VALUES()"
#         cursor.execute(query, (employee_id,))
#         result = cursor.fetchone()

#         if result:
#             # Display employee details or prompt for specific actions
#             employee_data_label = ttk.Label(
#                 master=employee_window,
#                 text=f"Employee ID: {result[0]}\nName: {result[1]}\nAddress: {result[2]}\nPosition: {result[3]}\nSalary: {result[4]}"
#             )
#             employee_data_label.pack()
#         else:
#             employee_data_label = ttk.Label(master=employee_window, text="Employee not found.")
#             employee_data_label.pack()

#     submit_button = ttk.Button(master=employee_window, text="Submit", command=handle_employees)
#     submit_button.pack()

# def open_farmer_details():
#     farmer_window = tk.Toplevel(window)
#     farmer_window.title('Farmer Details')

#     # Prompt for farmer ID
#     farmer_label = ttk.Label(master=farmer_window, text="Enter Farmer ID:")
#     farmer_label.pack()
#     farmer_entry = ttk.Entry(master=farmer_window)
#     farmer_entry.pack()

#     def handle_farmers():
#         farmer_id = farmer_entry.get()
#         query = "SELECT * FROM farmer WHERE id = %s"
#         cursor.execute(query, (farmer_id,))
#         result = cursor.fetchone()

#         if result:
#             farmer_data_label = ttk.Label(
#                 master=farmer_window,
#                 text=f"Farmer ID: {result[0]}\nName: {result[1]}\nAddress: {result[2]}\nSex: {result[3]}\nCreated At: {result[4]}\nContact Number: {result[5]}\nFactory ID: {result[6]}"
#             )
#             farmer_data_label.pack()

#             # Buttons for actions
#             personal_details_button = ttk.Button(master=farmer_window, text="Personal Details", command=show_personal_details)
#             personal_details_button.pack()

#             inputs_button = ttk.Button(master=farmer_window, text="Farmer Inputs", command=show_farmer_inputs)
#             inputs_button.pack()

#             bank_details_button = ttk.Button(master=farmer_window, text="Bank Details")
#             bank_details_button.pack()

#         else:
#             farmer_data_label = ttk.Label(master=farmer_window, text="Farmer not found.")
#             farmer_data_label.pack()

#     farmer_button = ttk.Button(master=farmer_window, text="Submit", command=handle_farmers)
#     farmer_button.pack()

#     def show_personal_details():
#         personal_details_window = tk.Toplevel(farmer_window)
#         personal_details_window.title("Personal Details")

#         # Add or delete personal details functionality here
#         add_query = "INSERT INTO farmer(name, address, sex, concact_number, factory_id), VALUES()"
#         delete_query = "DELETE FROM farmer WHERE id= '%s"


#     def show_farmer_inputs():
#         farmer_inputs_window = tk.Toplevel(farmer_window)
#         farmer_inputs_window.title("Farmer Inputs")

#         # Add or delete farmer inputs functionality here
#         add_query = "INSERT INTO farmer_inputs(farmer_id, input_description, amount_charged) VALUES()"
#         delete_query = "DELETE FROM farmer_inputs WHERE farmer_id = '%s'"
#         bank_details_window = tk.Toplevel(farmer_window)
#         bank_details_window.title("Bank Details")
         
#         add_bank_query = "INSERT INTO farmer_bank(bank_name, account_number, amount_to_be_paid, farmer_id)"
#         delete_bank_query = "DELETE FROM farmer_bank WHERE "
#         # Add or delete bank details functionality here

# farmer_button.configure(command=open_farmer_details)
# employee_button.configure(command=open_employees)

# window.mainloop()
import tkinter as tk
from tkinter import ttk
import mysql.connector as connector

connection = connector.connect(host="localhost", user="root", password="Password100$", database="coffeefactorydb")
cursor = connection.cursor()

window = tk.Tk()
window.title('Coffee Management Pixel')
window.geometry('1920x1080')

# Title
title_label = ttk.Label(master=window, text="Coffee Management System", font="Algerian 25 bold")
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
farmer_button = ttk.Button(master=input_frame, text='Farmer')
sales_button = ttk.Button(master=input_frame, text='Sales')
employee_button = ttk.Button(master=input_frame, text="Employees")
farmer_button.pack()
sales_button.pack()
employee_button.pack()
input_frame.pack()


def open_employees():
    employee_window = tk.Toplevel(window)
    employee_window.title("Employees")

    # Prompt for employee ID
    employee_label = ttk.Label(master=employee_window, text="Enter Employee ID:")
    employee_label.pack()
    employee_entry = ttk.Entry(master=employee_window)
    employee_entry.pack()

    def handle_employees():
        employee_id = employee_entry.get()
        query = "SELECT * FROM employee WHERE id = %s"
        query2 = "INSERT INTO employee(name, address, position, salary) VALUES()"
        cursor.execute(query, (employee_id,))
        result = cursor.fetchone()

        if result:
            # Display employee details or prompt for specific actions
            employee_data_label = ttk.Label(
                master=employee_window,
                text=f"Employee ID: {result[0]}\nName: {result[1]}\nAddress: {result[2]}\nPosition: {result[3]}\nSalary: {result[4]}"
            )
            employee_data_label.pack()
        else:
            employee_data_label = ttk.Label(master=employee_window, text="Employee not found.")
            employee_data_label.pack()

    submit_button = ttk.Button(master=employee_window, text="Submit", command=handle_employees)
    submit_button.pack()


def open_farmer_details():
    farmer_window = tk.Toplevel(window)
    farmer_window.title('Farmer Details')

    # Prompt for farmer ID
    farmer_label = ttk.Label(master=farmer_window, text="Enter Farmer ID:")
    farmer_label.pack()
    farmer_entry = ttk.Entry(master=farmer_window)
    farmer_entry.pack()

    def handle_farmers():
        farmer_id = farmer_entry.get()
        query = "SELECT * FROM farmer WHERE id = %s"
        cursor.execute(query, (farmer_id,))
        result = cursor.fetchone()

        if result:
            farmer_data_label = ttk.Label(
                master=farmer_window,
                text=f"Farmer ID: {result[0]}\nName: {result[1]}\nAddress: {result[2]}\nSex: {result[3]}\nCreated At: {result[4]}\nContact Number: {result[5]}\nFactory ID: {result[6]}"
            )
            farmer_data_label.pack()

            # Buttons for actions
            personal_details_button = ttk.Button(master=farmer_window, text="Personal Details",
                                                 command=lambda: show_personal_details(result[0]))
            personal_details_button.pack()

            inputs_button = ttk.Button(master=farmer_window, text="Farmer Inputs",
                                       command=lambda: show_farmer_inputs(result[0]))
            inputs_button.pack()

            bank_details_button = ttk.Button(master=farmer_window, text="Bank Details",
                                             command=lambda: show_bank_details(result[0]))
            bank_details_button.pack()

        else:
            farmer_data_label = ttk.Label(master=farmer_window, text="Farmer not found.")
            farmer_data_label.pack()

    farmer_button = ttk.Button(master=farmer_window, text="Submit", command=handle_farmers)
    farmer_button.pack()


def show_personal_details(farmer_id):
    personal_details_window = tk.Toplevel()
    personal_details_window.title("Personal Details")

    # Prompt for personal details
    name_label = ttk.Label(master=personal_details_window, text="Name:")
    name_label.pack()
    name_entry = ttk.Entry(master=personal_details_window)
    name_entry.pack()

    address_label = ttk.Label(master=personal_details_window, text="Address:")
    address_label.pack()
    address_entry = ttk.Entry(master=personal_details_window)
    address_entry.pack()

    sex_label = ttk.Label(master=personal_details_window, text="Sex:")
    sex_label.pack()
    sex_entry = ttk.Entry(master=personal_details_window)
    sex_entry.pack()

    contact_label = ttk.Label(master=personal_details_window, text="Contact Number:")
    contact_label.pack()
    contact_entry = ttk.Entry(master=personal_details_window)
    contact_entry.pack()

    factory_label = ttk.Label(master=personal_details_window, text="Factory ID:")
    factory_label.pack()
    factory_entry = ttk.Entry(master=personal_details_window)
    factory_entry.pack()

    # Function to handle adding personal details
    def add_personal_details():
        name = name_entry.get()
        address = address_entry.get()
        sex = sex_entry.get()
        contact_number = contact_entry.get()
        factory_id = factory_entry.get()

        query = "INSERT INTO farmer(name, address, sex, contact_number, factory_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, address, sex, contact_number, factory_id))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=personal_details_window, text="Personal details added successfully.")
        success_label.pack()

    # Function to handle deleting personal details
    def delete_personal_details():
        query = "DELETE FROM farmer WHERE id = %s"
        cursor.execute(query, (farmer_id,))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=personal_details_window, text="Personal details deleted successfully.")
        success_label.pack()

    # Function to handle updating personal details
    def update_personal_details():
        name = name_entry.get()
        address = address_entry.get()
        sex = sex_entry.get()
        contact_number = contact_entry.get()
        factory_id = factory_entry.get()

        query = "UPDATE farmer SET name = %s, address = %s, sex = %s, contact_number = %s, factory_id = %s WHERE id = %s"
        cursor.execute(query, (name, address, sex, contact_number, factory_id, farmer_id))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=personal_details_window, text="Personal details updated successfully.")
        success_label.pack()

    add_button = ttk.Button(master=personal_details_window, text="Add Details", command=add_personal_details)
    add_button.pack()

    delete_button = ttk.Button(master=personal_details_window, text="Delete Details", command=delete_personal_details)
    delete_button.pack()

    update_button = ttk.Button(master=personal_details_window, text="Update Details", command=update_personal_details)
    update_button.pack()


def show_farmer_inputs(farmer_id):
    farmer_inputs_window = tk.Toplevel()
    farmer_inputs_window.title("Farmer Inputs")

    # Prompt for input details
    description_label = ttk.Label(master=farmer_inputs_window, text="Input Description:")
    description_label.pack()
    description_entry = ttk.Entry(master=farmer_inputs_window)
    description_entry.pack()

    amount_label = ttk.Label(master=farmer_inputs_window, text="Amount Charged:")
    amount_label.pack()
    amount_entry = ttk.Entry(master=farmer_inputs_window)
    amount_entry.pack()

    # Function to handle adding farmer inputs
    def add_farmer_inputs():
        input_description = description_entry.get()
        amount_charged = amount_entry.get()

        query = "INSERT INTO farmer_inputs(farmer_id, input_description, amount_charged) VALUES (%s, %s, %s)"
        cursor.execute(query, (farmer_id, input_description, amount_charged))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=farmer_inputs_window, text="Farmer inputs added successfully.")
        success_label.pack()

    # Function to handle deleting farmer inputs
    def delete_farmer_inputs():
        query = "DELETE FROM farmer_inputs WHERE farmer_id = %s"
        cursor.execute(query, (farmer_id,))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=farmer_inputs_window, text="Farmer inputs deleted successfully.")
        success_label.pack()

    add_button = ttk.Button(master=farmer_inputs_window, text="Add Inputs", command=add_farmer_inputs)
    add_button.pack()

    delete_button = ttk.Button(master=farmer_inputs_window, text="Delete Inputs", command=delete_farmer_inputs)
    delete_button.pack()


def show_bank_details(farmer_id):
    bank_details_window = tk.Toplevel()
    bank_details_window.title("Bank Details")

    # Prompt for bank details
    bank_name_label = ttk.Label(master=bank_details_window, text="Bank Name:")
    bank_name_label.pack()
    bank_name_entry = ttk.Entry(master=bank_details_window)
    bank_name_entry.pack()

    account_number_label = ttk.Label(master=bank_details_window, text="Account Number:")
    account_number_label.pack()
    account_number_entry = ttk.Entry(master=bank_details_window)
    account_number_entry.pack()

    amount_to_be_paid_label = ttk.Label(master=bank_details_window, text="Amount to be Paid:")
    amount_to_be_paid_label.pack()
    amount_to_be_paid_entry = ttk.Entry(master=bank_details_window)
    amount_to_be_paid_entry.pack()

    # Function to handle adding bank details
    def add_bank_details():
        bank_name = bank_name_entry.get()
        account_number = account_number_entry.get()
        amount_to_be_paid = amount_to_be_paid_entry.get()

        query = "INSERT INTO farmer_bank(bank_name, account_number, amount_to_be_paid, farmer_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (bank_name, account_number, amount_to_be_paid, farmer_id))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=bank_details_window, text="Bank details added successfully.")
        success_label.pack()

    # Function to handle deleting bank details
    def delete_bank_details():
        query = "DELETE FROM farmer_bank WHERE farmer_id = %s"
        cursor.execute(query, (farmer_id,))
        connection.commit()

        # Show success message
        success_label = ttk.Label(master=bank_details_window, text="Bank details deleted successfully.")
        success_label.pack()

    add_button = ttk.Button(master=bank_details_window, text="Add Details", command=add_bank_details)
    add_button.pack()

    delete_button = ttk.Button(master=bank_details_window, text="Delete Details", command=delete_bank_details)
    delete_button.pack()


# Event handlers for buttons
employee_button.config(command=open_employees)
farmer_button.config(command=open_farmer_details)

window.mainloop()
