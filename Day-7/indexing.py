gros = {"Rice": 60, "Wheat": 70, "Wheat flour": 70, "Eggs": 60, "tomatoes": 35, "Bread": 45, "Butter": 80, "Milk": 50, "Cheese": 90, "Yogurt": 40}
for i in gros:
    print(f"{i} {gros[i]}")
emp_list = list(map(int, input("Enter space-separated numbers: ").split()))
print("Entered list:", emp_list)

# Assuming the numbers are indices (0-based) for the grocery items
keys = list(gros.keys())
for idx in emp_list:
    if 0 <= idx < len(keys):
        print(f"Selected item: {keys[idx]} - {gros[keys[idx]]}")
    else:
        print(f"Invalid index: {idx}")
