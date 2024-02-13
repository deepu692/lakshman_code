name = input('Enter your lovely name: ')

coffee_list = ['coffee', 'cold coffee', 'brownie', 'smoothie', 'black coffee', 'cappuccino']

choice = input(f"Hi {name}!!! Enter your choice from the list: {coffee_list}: ")

cost_of_coffee = {'coffee': 12, 'cold coffee': 24, 'brownie': 65, 'smoothie': 78, 'black coffee': 89, 'cappuccino': 100}

personalization = input("do you have any requirements, if so please tell us to serve you better")

if choice in coffee_list:
    print(f"Your order of {choice} will be delivered. The cost is: ${cost_of_coffee[choice]}")
else:
    print('Sorry, that is not a valid order.')
