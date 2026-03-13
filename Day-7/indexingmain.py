#gros = {"Rice": 60, "Wheat": 70, "Wheat flour": 70, "Eggs": 60, "tomatoes": 35, "Bread": 45, "Butter": 80, "Milk": 50, "Cheese": 90, "Yogurt": 40}
products = ["Rice", "Wheat", "Wheat flour", "Eggs", "tomatoes", "Bread", "Butter", "Milk", "Cheese", "Yogurt"]
prices = [60, 70, 70, 60, 35, 45, 80, 50, 90, 40]
print('Index'.ljust(6) + 'Item'.ljust(10) + 'Price'.ljust(10))
for i in range(len(products)):
    print(str(i+1).ljust(6) + products[i].ljust(10) + str(prices[i]).ljust(10))
item = list(map(int, input("Enter the indexes: ").split()))
print("Selected items:")
total_amount = 0
for item in item:
    print(f"{products[item-1]}, {prices[item-1]}")
    total_amount += prices[item-1]
print(f"Total amount: {total_amount}")