import csv

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# Displays the inventory.
def display_inventory(inventory):
    print('Inventory:')
    for name, coin in inventory.items():
        print('{:2d} {}'.format(coin, name))
    print('Total number of items: ', sum(inventory.values()))
    pass


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for additem in added_items:  # itt type errort adott, ha használtam zárójelet, miért?
        if inventory.get(additem, 0) == 0:
            inventory[additem] = 1
        else:
            inventory[additem] += 1
    return inventory
    pass


# Takes your inventory and displays it in a well-organized table 
def print_table(inventory, order=None):

    if order == 'count,asc':
        from collections import OrderedDict
        inv_sorted_by_value = OrderedDict(sorted(inventory.items(), key=lambda x: x[1]))

    elif order == 'count,desc':
        from collections import OrderedDict
        inv_sorted_by_value = OrderedDict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))

    print('''
Inventory:

  count           item name
-------------------------------
''')
    for name, coin in inv_sorted_by_value.items():
        print('{:5}             {:>}'.format(coin, name))  # nem rendezi jobbra a namet
    print('''
-------------------------------
  Total number of items: ''', sum(inventory.values()))
    pass


# Imports new inventory items from a file
    # import os ------ nem találta import_inventory.csv-t a mappában,
    # b ki kellett másolni a főmappába

    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)
    # print("Files in '%s': %s" % (cwd, files))
def import_inventory(inventory, filename="import_inventory.csv"):
    impinv = []
    with open("import_inventory.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            impinv.extend(row)
    return impinv      
    pass


# Exports the inventory into a .csv file.
def export_inventory(inventory, filename="export_inventory.csv"):
    with open('export_inventory.csv', 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for name, coin in inventory.items():
            writeCSV.writerow([name] * coin)    # új sorba írja
    pass


display_inventory(inv)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

importinventory = import_inventory(inv, 'import_inventory.csv')
inv = add_to_inventory(inv, importinventory)
inv = add_to_inventory(inv, import_inventory(inv, 'import_inventory.csv'))
print_table(inv, 'count,desc')
export_inventory(inv)