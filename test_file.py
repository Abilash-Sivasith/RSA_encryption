import main

# TESTING - prime_checker function

def creates_list_from_zero_to_hundred():
    '''creates a list from 0 to 100'''
    list_of_nums_to_check = []
    [list_of_nums_to_check.append(i) for i in range(101)]
    return list_of_nums_to_check

def list_of_primes_less_than_100():
    '''creates a list of primes less than 100'''

    list_of_nums_to_check = creates_list_from_zero_to_hundred()
    list_of_primes_less_than_100 = []
    for num in list_of_nums_to_check:
        is_prime = main.prime_checker(num)
        if is_prime == True:
            list_of_primes_less_than_100.append(num)
        is_prime = False
    
    return list_of_primes_less_than_100

list_of_primes_less_than_100 = list_of_primes_less_than_100()
print(list_of_primes_less_than_100) # should return a list
print(len(list_of_primes_less_than_100)) # should return 25


# TESTING - eulers_toilent_calculator function
# print(eulers_toilent_calculator(5, 7)) # will print 24


# TESTING - gcd_finder function
#print(main.gcd_finder(14,49)) # will print 7

# TESTING - is_gcd_eqaul_to_one function 
#print(main.is_gcd_equal_to_one(7, 15)) # True
#print(main.is_gcd_equal_to_one(4, 8)) # False
    
# TESTING - public_e_finder function
#print(main.public_e_finder(3, 5))

# TESTING - linear_combination function 
# print(main.linear_combination(7, 5)) # 1 = 7(-2) + 5(3)
# print(main.linear_combination(13,5)) # 1 = 13(3) + 5(-5)