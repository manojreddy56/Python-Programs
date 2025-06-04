import random
import string

pass_len = 12
char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(char_values)
    
print("your random password is: ",password)