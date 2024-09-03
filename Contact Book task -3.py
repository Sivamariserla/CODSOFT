# Initialize lists to store names and contact numbers
contacts = {}

# Get the number of contacts to save
num = int(input("Enter the total number of contacts you want to save: "))

# Collect contact information
for _ in range(num):
    name = input("Name: ")
    contact_number = input("Contact Number: ")
    contacts[name] = contact_number

# Display the contacts
print("\nName\t\tContact Number")
for name, number in contacts.items():
    print(f"{name}\t\t{number}")

# Search for a contact by name
search_term = input("\nEnter search term: ")
if search_term in contacts:
    print(f"Name: {search_term}, Phone Number: {contacts[search_term]}")
else:
    print("No records found.")
