import tkinter as tk

window = tk.Tk()
window.title("Password Generator")

tk.Label(window,text="website:").pack()
website_entry = tk.Entry(window)
website_entry.pack(padx=20)

tk.Label(window,text="Login ID:").pack()
loginid_entry = tk.Entry(window)
loginid_entry.pack(padx=20)

numbers_var= tk.BooleanVar()
check_button = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
check_button.pack()

uppercase_var= tk.BooleanVar()
check_button = tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var)
check_button.pack()

lowercase_var= tk.BooleanVar()
check_button = tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var)
check_button.pack()

specialchar_var= tk.BooleanVar()
check_button = tk.Checkbutton(window, text="Include Special Characters", variable=specialchar_var)
check_button.pack()

tk.Label(window,text="Password Length:").pack()
passlen_var =tk.IntVar()
slider = tk.Scale(window, variable = passlen_var, from_ = 8, to = 32, orient =tk.HORIZONTAL)
slider.pack()

def on_button_clicked():
    website = website_entry.get()
    login_id = loginid_entry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_specialchar = specialchar_var.get()
    include_numbers= numbers_var.get()
    passlen = passlen_var.get()

generate_button = tk.Button(window, text= "Generate Password", command = on_button_clicked)
generate_button.pack()

# website_entry = tk.Entry(window)
# website_entry.pack(padx=20)

window.mainloop()
