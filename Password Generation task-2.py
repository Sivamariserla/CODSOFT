# Creating the User defined length and Password GUI Application
import tkinter as tk
import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    pswd = ''
    for _ in range(length):
        pswd += random.choice(char)
    return pswd

def generate():
    l = length_entry.get()
    if l.isdigit() and int(l) > 1:
        pswd = generate_password(int(l))
        final_label.config(text=f"Password: {pswd}")
    else:
        final_label.config(text="Enter a valid number greater than 1.")
        

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")  # Set the title of the window
root.geometry("300x200")           # Set the size of the window

# Create and place  in the window
length_label = tk.Label(root, text="Length:")
length_label.pack(pady=5) # places the label in the window with 5 pixels of vertical padding

# Define the user input
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=10)

final_label = tk.Label(root, text="")
final_label.pack(pady=10)

# Start the GUI
root.mainloop()
