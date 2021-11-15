# A pizza restaurant would like you to create a program that works out the total cost for each pizza that they sell.

# Create a series of print statements and inputs that will allow the customer to type in their pizza requirements

#Make sure that a total_cost variable has been created for the total cost of the pizza 

#Create an if statement that will apply £10 if their pizza is thin and £8 if it is thick 

#Use a print statement to print the total_cost at the end of the code block so that you can test that the code is working 

#There are just two different costs for the size options. If the pizza is larger than 10 inches, then an additional charge of £2 is applied. Create an if statement that will apply this charge based on this condition.

#Use a print statement to print the total cost and test your code.

#If the cheese is not equal to yes, then a discount of 50 pence is applied to the total  cost. Create an if statement that will perform this calculation based on the condition. 

#There are three different pricing options for the pizza. The margherita pizza doesn't have an additional charge, so decide if this needs to be part of one of your conditions. 
#If the pizza is vegetable or vegan, then there is an additional charge of £1.
#If the pizza is Hawaiian or meat feast, then there is an additional charge of £2.
#Decide what if statements and conditions you will need to apply these costs.
#Test your code by using a print statement to print the total cost. Remember to test all possible inputs. 

#The voucher code can be applied when the customer purchases an 18-inch pizza and has typed in the correct code which is FunFriday. Create an if statement that checks that both conditions are true and then applies the £2 discount. 

#Repeat the order back to the customer and reveal the total cost of the pizza 

#Test your code by entering all of the different possible scenarios for ordering a pizza 
#Fix any errors that might occur
#Remember to use .lower() or .upper() where required 
pizzaPrice = 0.00
print("Thin or thick crust: ")
crust = input()
print("8, 10, 12, 14 or 18")
size = int(input())
print("Cheese or None: ")
cheese = input()
print("Margharita, Vegtable, Vegan, Hawaiian or Meatfeast  ")
typeOfPizza = input()
print("Do you have a voucher? (This is only reedemable for 18inch pizzas)")
voucherCode = input()
if crust == "thin":
  pizzaPrice = pizzaPrice + 10.00
else:
  pizzaPrice = pizzaPrice + 8.00
if size == 8 or 10:
  pizzaPrice = pizzaPrice + 0.00
else:
  pizzaPrice = pizzaPrice + 2.00
if cheese == "none":
  pizzaPrice = pizzaPrice - 0.50
else:
  pizzaPrice = pizzaPrice + 1.00
if typeOfPizza == "margharita":
  pizzaPrice = pizzaPrice + 0.0
elif typeOfPizza == "vegatable" or "vegan":
  pizzaPrice = pizzaPrice + 1.00
else:
  pizzaPrice = pizzaPrice + 2.00
if voucherCode == "FunFriday" + size == 18:
  pizzaPrice = pizzaPrice - 2.00
else:
  print("Sorry your voucher is invalid. ")
print()
print("The total price ypur pizza is £" + pizzaPrice)

#I have completed everything else but, I do not know how to do the voucher section of the code for it ot recognise that its a 18 inch pizza. I just get: Traceback (most recent call last):

#File "main.py", line 59, in <module>
    #if voucherCode == "FunFriday" + size == 18:
#TypeError: can only concatenate str (not "int") to str
