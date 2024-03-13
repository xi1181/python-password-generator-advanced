import tkinter as tk

window = tk.Tk()
window.title("Password Generator")
window.mainloop()

tk.Label(window,text="website:").pack()
website_entry = tk.Entry(window)
website_entry.pack(padx=20)
