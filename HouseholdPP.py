import json
file_name = "inventory.json"
def load_data():
    try:
        file = open(file_name, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []


def save_data(data):
    file = open(file_name, "w")
    json.dump(data, file, indent=4)
    file.close()

def add_item(data):
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    item = {
        "name": name,
        "quantity": qty,
        "price": price
    }

    data.append(item)
    save_data(data)
    print("Item Added Successfully")

def view_items(data):
    if len(data) == 0:
        print("No Items Available")
    else:
        for i in data:
            print("-------------------")
            print("Name :", i["name"])
            print("Quantity :", i["quantity"])
            print("Price :", i["price"])


def search_item(data):
    name = input("Enter item name to search: ")

    found = False

    for i in data:
        if i["name"].lower() == name.lower():
            print("Item Found")
            print(i)
            found = True

    if found == False:
        print("Item Not Found")


def delete_item(data):
    name = input("Enter item name to delete: ")

    for i in data:
        if i["name"].lower() == name.lower():
            data.remove(i)
            save_data(data)
            print("Item Deleted")
            return

    print("Item Not Found")

def total_cost(data):
    total = 0

    for i in data:
        total = total + (i["quantity"] * i["price"])

    print("Total Inventory Cost =", total)

def main():
    data = load_data()

    while True:
        print("\n--- HI-CAS MENU ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Delete Item")
        print("5. Total Cost")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_item(data)

        elif ch == "2":
            view_items(data)

        elif ch == "3":
            search_item(data)

        elif ch == "4":
            delete_item(data)

        elif ch == "5":
            total_cost(data)

        elif ch == "6":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
main()