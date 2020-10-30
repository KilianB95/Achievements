grocerylist = ["Milk", "Cheese", "Sausage"]
shoppingcart = ["Milk", "Cheese", "Sausage"]


for x, y in zip(grocerylist, shoppingcart):
    if len(grocerylist) == len(shoppingcart):
        if x == y:
            print("Done Shopping")
    else:
        print("Continue Shopping")
