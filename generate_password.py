import random
import string

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