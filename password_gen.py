import random
import string

pass_length = 9
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(pass_length)])
 
print("Your pw generated is: ", password)
