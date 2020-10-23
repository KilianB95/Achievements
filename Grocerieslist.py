grocerylist = ["Milk", "Cheese", "Sausage"]
shoppingcart = ["Milk", "Cheese", "Sausage"]

 

for x, y in zip(grocerylist, shoppingcart):
    if x > y:
        print("Continue Shopping")
    if x==y:
        print("Done Shopping")
