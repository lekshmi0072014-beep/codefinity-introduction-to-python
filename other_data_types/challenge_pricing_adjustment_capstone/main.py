#Create the Dictionary


grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}



# Check and Update Price
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        eggs_price - 1,
        grocery_inventory["Eggs"][2],
    )
    
else:
    print(f"The price of Eggs is reasonable.")

#Add a New Item

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#Manage Stock
Milk_stock = grocery_inventory.get("Milk")
if Milk_stock[2] < 10:
    print(f"Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 28)})

else:
    print("Milk has sufficient stock.")

#Remove Item Based on Price

apple_price = grocery_inventory.get("Apples")

if apple_price[1] > 2:
    grocery_inventory.remove("Apples")
    print("Apples removed from inventory due to high price.")

#Final Print

print(f"Updated inventory: {grocery_inventory}")


