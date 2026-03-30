total_items = int(input("How many items: "))
items = []

# Using 'current_item' instead of 'count' or 'stuff'
current_item = 1

while current_item <= total_items:
    # item_value is more descriptive than num1
    item_value = int(input(f"Item {current_item}: "))
    items.append(item_value)
    current_item += 1

print(items)
