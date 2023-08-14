import time
from art import logo

customer_order = {'water' : 0, 'milk' : 0, 'coffee' : 0, 'money' : 0}
customer_coins = {'quarters' : 0, 'dimes' : 0, 'nickles' : 0, 'pennies' : 0}
Total_amount = 0
update_change = 0
machine_capacity = {
    'water' : 1000,
    'milk' : 600,
    'coffee' : 800,
}
fixed_data = {
    "latte" : {
        'water' : 200,
        'milk' : 80,
        'coffee' : 40,
        'money' : 6,
    },
    "cappuccino" : {
        'water' : 100,
        'milk' : 60,
        'coffee' : 30,
        'money' : 4,
    },
    "espresso" : {
        'water' : 150,
        'milk' : 40,
        'coffee' : 60,
        'money' : 2.5,
    }
}

def sufficient_resources():
    if (customer_order['milk']<=machine_capacity['milk'] and customer_order['water']<=machine_capacity['water'] and customer_order['coffee']<=machine_capacity['coffee']):
    
        if (customer_order['milk']>machine_capacity['milk']):
            print("Sorry there is not enough milk.")
        if (customer_order['water']>machine_capacity['water']):
            print("Sorry there is not enough water.")
        if (customer_order['coffee']>machine_capacity['coffee']):
            print("Sorry there is not enough coffee.")
        return True
    else:
        return False
def update_report(choice):
    customer_order['water'] = fixed_data[choice]['water']
    customer_order['milk'] = fixed_data[choice]['milk']
    customer_order['coffee'] = fixed_data[choice]['coffee']
    customer_order['money'] = fixed_data[choice]['money']

def billing():
    machine_capacity['milk'] -= customer_order['milk']
    machine_capacity['water'] -= customer_order['water']
    machine_capacity['coffee'] -= customer_order['coffee']
    

def change_calculation(change):
    change = round(change,2)
    customer_coins['quarters'] = int(change / 0.25)
    change -= (customer_coins['quarters']*0.25)
    change = round(change,2)
    customer_coins['dimes'] = int(change / 0.1)
    change -= (customer_coins['dimes']*0.1)
    change = round(change,2)
    customer_coins['nickles'] = int(change / 0.05)
    change -= (customer_coins['nickles']*0.05)
    change = round(change,2)
    customer_coins['pennies'] = int(change / 0.01)
while True:

    print(logo)

    choice = input("What would you like? ").lower()

    if (choice == 'off'):
        exit()
    elif (choice == 'report'):
        print(f" Water : {customer_order['water']}ml \n Milk : {customer_order['milk']}ml \n Coffee : {customer_order['coffee']}g \n Money : ${customer_order['money']}")
    elif (choice == 'espresso'):
        update_report(choice)
        if (sufficient_resources()):
            print("Please insert coins")
            customer_coins['quarters'] = int(input("Quarters : "))
            customer_coins['dimes'] = int(input("Dimes : "))
            customer_coins['nickles'] = int(input("Nickels : "))
            customer_coins['pennies'] = int(input("Pennies = "))
            Total_amount = round((customer_coins['quarters'] * 0.25) + (customer_coins['dimes'] * 0.1) + (customer_coins['nickles'] * 0.05) + (customer_coins['pennies'] * 0.01),2)
            print(f"Total amount added by customer is : ${Total_amount}")
            if (Total_amount >= customer_order['money']):
                billing()
                if (Total_amount != 0):
                    change=round((float)(Total_amount - float(customer_order['money'])),3)
                    change_calculation(change)
                    print(f"Here is ${change} in change :\n Quarters = {customer_coins['quarters']} \n Dimes = {customer_coins['dimes']} \n Nickles = {customer_coins['nickles']} \n Pennies = {customer_coins['pennies']}")
                    time.sleep(2)
                    print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif (choice == 'latte'):
        update_report(choice)
        if (sufficient_resources()):
            print("Please insert coins")
            customer_coins['quarters'] = int(input("Quarters : "))
            customer_coins['dimes'] = int(input("Dimes : "))
            customer_coins['nickles'] = int(input("Nickels : "))
            customer_coins['pennies'] = int(input("Pennies = "))
            Total_amount = round((customer_coins['quarters'] * 0.25) + (customer_coins['dimes'] * 0.1) + (customer_coins['nickles'] * 0.05) + (customer_coins['pennies'] * 0.01),2)
            print(f"Total amount added by customer is : ${Total_amount}")
            if (Total_amount >= customer_order['money']):
                billing()
                if (Total_amount != 0):
                    change=round((float)(Total_amount - float(customer_order['money'])),3)
                    change_calculation(change)
                    print(f"Here is ${change} in change :\n Quarters = {customer_coins['quarters']} \n Dimes = {customer_coins['dimes']} \n Nickles = {customer_coins['nickles']} \n Pennies = {customer_coins['pennies']}")
                    time.sleep(2)
                    print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif (choice == 'cappuccino'):
        update_report(choice)
        if (sufficient_resources()):
            print("Please insert coins")
            customer_coins['quarters'] = int(input("Quarters : "))
            customer_coins['dimes'] = int(input("Dimes : "))
            customer_coins['nickles'] = int(input("Nickels : "))
            customer_coins['pennies'] = int(input("Pennies = "))
            Total_amount = round((customer_coins['quarters'] * 0.25) + (customer_coins['dimes'] * 0.1) + (customer_coins['nickles'] * 0.05) + (customer_coins['pennies'] * 0.01),2)
            print(f"Total amount added by customer is : ${Total_amount}")
            if (Total_amount >= customer_order['money']):
                billing()
                if (Total_amount != 0):
                    change=round((float)(Total_amount - float(customer_order['money'])),3)
                    change_calculation(change)
                    print(f"Here is ${change} in change :\n Quarters = {customer_coins['quarters']} \n Dimes = {customer_coins['dimes']} \n Nickles = {customer_coins['nickles']} \n Pennies = {customer_coins['pennies']}")
                    time.sleep(2)
                    print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        