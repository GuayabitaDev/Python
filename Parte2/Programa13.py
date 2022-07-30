#-------------------------
#        Imports
#-------------------------



#-------------------------
#        Data
#-------------------------

#Customer Data
Name = ""
Change = ""
cBudget = 25

#CoffeShop Data
Menu = "A) Espresso Americano \nB) Latte Macchiato \nC) Mocha Blanco"
EAprice = 10
LMprice = 15
MBprice = 35

#Messages Data
Success = "Thank you for your purchase here is your {}$ of change"
NoMoney = "You don't have enough money to purchase that product!"

#-------------------------
#        Code
#-------------------------

Name = input("Welcome to the Coffee Shop, which is your name? \n")
Cart = input("Welcome " + Name + " what would you like to order? \n \n" + Menu  + "\n \n")

if Cart == "A":
    Change = cBudget - EAprice
    if EAprice > cBudget:
        print(NoMoney)
    print(Success.format(Change))

if Cart == "B":
    Change = cBudget - LMprice
    if LMprice > cBudget:
        print(NoMoney)
    print(Success.format(Change))

if Cart == "C":
    if MBprice > cBudget:
        print(NoMoney)
    print(Success.format(Change))
