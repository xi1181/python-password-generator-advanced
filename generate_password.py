import random
import string
from tkinter import messagebox

pun = string.punctuation
letters = string.ascii_letters
num = string.digits
combine = pun + letters + num
def generate_password(len:int):
    pw = ""
    for char in range(len):
        pw += random.choice(combine)
    return pw

password1 = generate_password(5)
print(password1)


def gui_generate_password(web, id, incl_u, incl_l, incl_sc, incl_n, password_len):
    char = ""
    if incl_u:
        char += string.ascii_uppercase
    if incl_l:
        char += string.ascii_lowercase
    if incl_sc:
        char += string.punctuation
    if incl_n:
        char += string.digits
    if not char:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    pwd = ""
    for i in range (password_len):
        pwd += random.choice(char)
    with open("passwords.txt", "a") as file:
        file.write(f"Website:{web}, Login ID: {id}, Password: {pwd}\n")
                   
    messagebox.showinfo("Generated Password", f"Your Password: {pwd}")