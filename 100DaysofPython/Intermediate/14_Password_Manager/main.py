from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(
    file="100DaysofPython\Intermediate\\14_Password_Manager\\1_PM_app\logo.png"
)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry  = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=None)
generate_pass_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36, command=None)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
