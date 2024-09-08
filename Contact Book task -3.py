import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    contact_number = number_entry.get()
    if name and contact_number:
        contacts[name] = contact_number
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter both name and contact number.")

# Function to show contact
def show_contacts():
    contacts_list = ""
    for name, number in contacts.items():
        contacts_list += f"{name}\t\t{number}\n"
    if contacts_list:
        messagebox.showinfo("Contacts", f"Name\t\tContact Number\n{contacts_list}")
    else:
        messagebox.showinfo("Contacts", "No contacts is available.")

# Function to search a  contact
def search_contact():
    search_term = search_entry.get()
    if search_term in contacts:
        messagebox.showinfo("Search Result", f"Name: {search_term}, Phone Number: {contacts[search_term]}")
    else:
        messagebox.showwarning("Search Result", "No records are not found.")

# Function to delete a contact
def delete_contact():
    search_term = search_entry.get()
    if search_term in contacts:
        del contacts[search_term]
        messagebox.showinfo("Delete Contact", f"Contact '{search_term}' deleted successfully!")
    else:
        messagebox.showwarning("Delete Contact", "No records are not found.")
def update_contact():
    name = search_entry.get()         # Get the contact name to search
    new_number = number_entry.get()   # Get the new contact number

    if name in contacts:
        if new_number:
            contacts[name] = new_number
            messagebox.showinfo("Update Contact", f"Contact '{name}' updated successfully!")
            number_entry.delete(0, tk.END)  # Clear the input field
        else:
            messagebox.showwarning("Error", "Please enter a new contact number.")
    else:
        messagebox.showwarning("Update Contact", "No records found.")


# Main window setup
root = tk.Tk()
root.title("Contact Book")

# Layout setup
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Contact Number:").grid(row=1, column=0, padx=10, pady=5)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Contacts", command=show_contacts).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Search/Update/Delete:").grid(row=4, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
