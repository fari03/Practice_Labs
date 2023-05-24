import tkinter as tk
from tkinter import messagebox

def submit():
    # Get the values entered in the fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()
    login_id = entry_login_id.get()
    password = entry_password.get()
    agreed = agree_var.get()

    # Validate if all fields are filled
    if not (first_name and last_name and dob and phone_number and email and login_id and password):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Check if the terms and conditions checkbox is checked
    if not agreed:
        messagebox.showerror("Error", "Please agree to the terms and conditions")
        return

    # Print the values entered
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Date of Birth:", dob)
    print("Phone Number:", phone_number)
    print("Email:", email)
    print("Login ID:", login_id)
    print("Password:", password)
    print("Terms and Conditions agreed:", agreed)

# Create the Tkinter window
window = tk.Tk()
window.title("Login Page")

# Create labels for the fields
label_first_name = tk.Label(window, text="First Name:")
label_last_name = tk.Label(window, text="Last Name:")
label_dob = tk.Label(window, text="Date of Birth:")
label_phone_number = tk.Label(window, text="Phone Number:")
label_email = tk.Label(window, text="Email:")
label_login_id = tk.Label(window, text="Login ID:")
label_password = tk.Label(window, text="Password:")

# Create entry fields for the user input
entry_first_name = tk.Entry(window)
entry_last_name = tk.Entry(window)
entry_dob = tk.Entry(window)
entry_phone_number = tk.Entry(window)
entry_email = tk.Entry(window)
entry_login_id = tk.Entry(window)
entry_password = tk.Entry(window, show="*")

# Create checkbox for terms and conditions agreement
agree_var = tk.BooleanVar()
checkbox_agree = tk.Checkbutton(window, text="Agree to Terms and Conditions", variable=agree_var)

# Create submit button
button_submit = tk.Button(window, text="Submit", command=submit)

# Grid layout for placing the widgets
label_first_name.grid(row=0, column=0)
entry_first_name.grid(row=0, column=1)
label_last_name.grid(row=1, column=0)
entry_last_name.grid(row=1, column=1)
label_dob.grid(row=2, column=0)
entry_dob.grid(row=2, column=1)
label_phone_number.grid(row=3, column=0)
entry_phone_number.grid(row=3, column=1)
label_email.grid(row=4, column=0)
entry_email.grid(row=4, column=1)
label_login_id.grid(row=5, column=0)
entry_login_id.grid(row=5, column=1)
label_password.grid(row=6, column=0)
entry_password.grid(row=6, column=1)
checkbox_agree.grid(row=7, columnspan=2)
button_submit.grid(row=8, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
