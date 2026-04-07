# def make_pizza(size, *toppings):
#     print(f"Making a {size} inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#     print(toppings)

# # You can pass 1 topping, 3 toppings, or none!
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# def build_profile(first, last, **user_info):
#     profile = {'first_name': first, 'last_name': last}
    
#     # Add any other key-value pairs to the dictionary
#     for key, value in user_info.items():
#         profile[key] = value
        
#     return profile

# user = build_profile('Albert', 'Einstein', location='Princeton', field='Physics')
# print(user)


def generate_receipt(customer_name, *item_prices, **extra_info):
    print(f"customer name: {customer_name}")

    sum = 0
    for i in item_prices:
        sum += i
    print(f"total amount: {sum}")

    print(f"additional info:")
    for i, j in extra_info.items():
        print(f"{i}: {j}")

generate_receipt("lance", 10, 20, 15, date = "3/26/26", store = "main")

