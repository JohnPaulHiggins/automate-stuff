def displayInventory(inventory):
    total_items = 0
	
	print("Inventory:")
    for k, v in inventory.items():
	    print(str(v) + " " + k)
		total_items += v
	
	print("Total number of items: " + str(total_items))

def addToInventory(inventory, addedItems):
    d = {}
	for item in addedItems:
	    d.setdefault(item, 0)
		d[item] += 1
	return d

