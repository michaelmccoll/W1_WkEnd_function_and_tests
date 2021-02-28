# WRITE YOUR FUNCTIONS HERE

# Test 1 (test_pet_shop_name)

def get_pet_shop_name(list):
    return list["name"]

# # Test 2 (test_total_cash)

def get_total_cash(list):
    return list["admin"]["total_cash"]

# # Test 3 (test_add_or_remove_cash__add)
# # Test 4 (test_add_or_remove_cash__remove)

def add_or_remove_cash(list,amount):
    list["admin"]["total_cash"] += amount

# # Test 5 (test_pets_sold)

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

# # Test 6 (test_increase_pets_sold)

def increase_pets_sold(list,add_sold):
    list["admin"]["pets_sold"] += add_sold

# # Test 7 (test_stock_count)

def get_stock_count(list):
    return len(list["pets"])

# # Test 8 (test_all_pets_by_breed__found) !!!NOT WORKING!!!
# # Test 9 (test_all_pets_by_breed__not_found)  !!!NOT WORKING!!!


# # Test 10 (test_find_pet_by_name__returns_pet)  !!!NOT WORKING!!!
# # Test 11 (test_find_pet_by_name__returns_None)  !!!NOT WORKING!!!


# # Test 12 (test_remove_pet_by_name)  !!!NOT WORKING!!!


# # Test 13 (test_add_pet_to_stock)

def add_pet_to_stock(list,add_new_pet_to_list):
    list["pets"].append(add_new_pet_to_list)

# # Test 14 (test_customer_cash)

def get_customer_cash(cust_list):
    return cust_list["cash"]

# # Test 15 (test_remove_customer_cash)

def remove_customer_cash(customer_list,amount):
    customer_list["cash"] -= amount

# # Test 16 (test_customer_pet_count)


# # Test 17 (test_add_pet_to_customer)


# OPTIONAL TESTS
# Test 18, 19, 20
def customer_can_afford_pet(cust_name, new_pet):
    if cust_name["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# INTEGRATION TESTS
# Need to get other functions to work first


# 13 Tests working: 1, 2, 3, 4, 5, 6, 7, 13, 14, 15, 18, 19, 20
# 10 Tests not working: 8, 9, 10, 11, 12, 16, 17, 21, 22, 23