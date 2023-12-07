menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
sub_menu = [
            {"Item_name": "Cookie", "Price": 0.99, "Quantity": 1},
            {"Item_name": "Banana", "Price": 0.69, "Quantity": 1},
            {"Item_name": "Apple", "Price": 0.49, "Quantity": 1},
            {"Item_name": "Granola bar", "Price": 1.99, "Quantity": 1},
            {"Item_name": "Burrito", "Price": 4.49, "Quantity": 1},
            {"Item_name": "Teriyaki Chicken", "Price": 9.99, "Quantity": 1},
            {"Item_name": "Sushi", "Price": 7.49, "Quantity": 1},
            {"Item_name": "Pad Thai", "Price": 6.99, "Quantity": 1},
            {"Item_name": "Pizza", "Cheese": {"Price": 8.99, "Quantity": 1},
                                    "Pepperoni": {"Price": 10.99, "Quantity": 1},
                                    "Vegetarian": {"Price": 9.99, "Quantity": 1}},
            {"Item_name": "Burger", "Chicken": {"Price": 7.49, "Quantity": 1},
                                    "Beef": {"Price": 8.49, "Quantity": 1}},
            {"Item_name": "Drinks", "Soda": {"Small": {"Price": 1.99, "Quantity": 1},
                                              "Medium": {"Price": 2.49, "Quantity": 1},
                                              "Large": {"Price": 2.99, "Quantity": 1}}},
            {"Item_name": "Tea", "Green": {"Price": 2.49, "Quantity": 1},
                                  "Thai iced": {"Price": 3.99, "Quantity": 1},
                                  "Irish breakfast": {"Price": 2.49, "Quantity": 1}},
            {"Item_name": "Coffee", "Espresso": {"Price": 2.99, "Quantity": 1},
                "Flat white": {"Price": 2.99, "Quantity": 1},
                "Iced": {"Price": 3.49, "Quantity": 1}},
            {"Item_name": "Dessert", "Chocolate lava cake": {"Price": 10.99, "Quantity": 1},
                "Cheesecake": {"New York": {"Price": 4.99, "Quantity": 1},
                               "Strawberry": {"Price": 6.49, "Quantity": 1}},
                "Australian Pavlova": {"Price": 9.99, "Quantity": 1},
                "Rice pudding": {"Price": 4.99, "Quantity": 1},
                "Fried banana": {"Price": 4.49, "Quantity": 1}}
        ]

print(sub_menu)

menu_selection = input("Welcome to the variety food truck, hit the enter key to continue and select from the menu.")
print(menu_selection)

place_order = True
while place_order:
    print("From which menu would you like to order? ")

    i = 1
    menu_items = {}

    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
               
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            
            menu_selection = input("Please select a menu item number: ")
            if not menu_selection.isdigit():
                print("Error: Please select a menu item number.")

            if menu_selection.isdigit():  
                menu_selection = int(menu_selection)

                if menu_selection in menu_items.keys():
                    order = []
                else:
                    print(f"{menu_selection} was not a menu option.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")
    
    place_order = True
    
    while place_order:
        keep_ordering = input("Would you like to keep ordering? (y)es or (n)o ")  
        match keep_ordering.lower():
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                break
            case _:
                print("Invalid input, please enter 'y' or 'n' to continue.")
                continue                         

    print("This is what we are preparing for you.\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

order = []

for items in order:
    item_name = items["Item name"]
    price = items["Price"]        
    quantity = items["Quantity"]

    item_name_spaces = 24 - len(menu_items["Item name"])
    price_spaces = 8 - len(str(menu_items["Price"]))
    quantity_spaces = 10 - len(str(menu_items["Quantity"]))
    
    item_name_space = " " * item_name_spaces
    price_space = " " * price_spaces
    quantity_space = " " * quantity_spaces

    print(f"{item_name}{item_name_space}| ${price:.2f}{price_space}| {quantity}{quantity_space}")

total_cost_menu_items = sum(item["Price"] * item["Quantity"] for item in order)

print(f"Total cost of menu items selected: ${total_cost_menu_items: .2f}")       
            
