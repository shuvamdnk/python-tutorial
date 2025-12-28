MENU = {
    "espresso": {
        "ingredients": {
            "water": 500,    
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,   
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

COFFEE_TYPES = ["espresso", "latte", "cappuccino"]
COFFEE_MACHINE = 'ON'

# CHECK IF THE RESOURCES ARE SUFFICIENT
def is_resource_sufficient(menu_details):
    """Returns True when order can be made, False if ingredients are insufficient."""
    
    for r in resources:
        if r in menu_details["ingredients"] and menu_details["ingredients"][r] >= resources[r]:
            return {"enough":False, "resource": r}
        
    return {"enough":True, "resource": ""}    
    
def is_amount_sufficient(quarters, dimes, nickles, pennies, menu_details):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    total_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    
    if menu_details["cost"] > total_value:
        return {"sufficient":False, "change" : 0}
    else:
        change = total_value - menu_details["cost"];
        return {"sufficient":True, "change" : round(change, 2)}
    
while COFFEE_MACHINE == 'ON':

    menu_item = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if menu_item == "report":
        for r in resources:
            print(f"{r.capitalize()}: {resources[r]}")
        continue

    if menu_item == "off":
        COFFEE_MACHINE = 'OFF'
        continue

    menu_details = MENU[menu_item]

    if not is_resource_sufficient(menu_details)["enough"]:
        print(f"Sorry there is not enough {is_resource_sufficient(menu_details)['resource']}.")
        continue
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))       
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    if not is_amount_sufficient(quarters, dimes, nickles, pennies, menu_details)["sufficient"]:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        change = is_amount_sufficient(quarters, dimes, nickles, pennies, menu_details)["change"]
        if change > 0:
            print(f"Here is ${change} in change.")
        
        for r in resources:
            if r in menu_details["ingredients"]:
                resources[r] -= menu_details["ingredients"][r]
        
        resources["money"] += menu_details["cost"]
        
        print(f"Here is your {menu_item} ☕️. Enjoy!")
    
