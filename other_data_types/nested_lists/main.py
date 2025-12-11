vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
print(f"Updated Vegetable Inventory: {vegetables}")

if "carrots" not in vegetables:
    vegetables.append("carrots")
    print(f"Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    print(f"Cucumbers are already in the list.")

vegetables.sort()
    
