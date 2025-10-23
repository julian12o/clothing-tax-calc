price = input(float("Enter the price of the most recent clothing item you purchased (singular item, hundrenth place: "))
brand = input("Enter the brand of the most recent clothing item you purchased: ")
residence = input("Enter the location you bought or where you delivered it if you bought it online: ")
amountofclothing = input(int("Enter the amount of the most recent clothing item you purchased: "))
#Clothes with Tax
pta = price * amountofclothing 
awptt =  awp * 106.625
print ("the amount you are going to pay with tax is a: ", awptt, "the brand you purchased it from was ", brand, " and finally the location in which you bought it was ", residence)
