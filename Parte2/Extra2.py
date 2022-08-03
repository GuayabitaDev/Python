# -------------------------
#        Imports
# -------------------------

import random

# -------------------------
#        Data
# -------------------------

digits = "ABCDEFGHIJKLMNOPRSTUVXYZabcdefghijklmnoprstuvxyz1234567890!#$%&()*+-\<=>?@[/]^_{}~"

# -------------------------
#        Code
# -------------------------

print("-------------------------------")
print("      PASSWORD GENERATOR       ")
print("-------------------------------")

security = input("How secure should the password be? (SMALL, MEDIUM, LARGE or EXTREME? \n")

if security == "SMALL":
    length = 8

elif security == "MEDIUM":
    length = 12

elif security == "LARGE":
    length = 16

elif security == "EXTREME":
    length = 20

else:
    print("Invalid input")
    exit()

password = "".join(random.sample(digits, length))
print(password)
    
