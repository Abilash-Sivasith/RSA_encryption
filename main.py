"""Implement RSA encrpytion to encrypt the privided plain-text"""

import math

def prime_checker(number):
    '''returns true if the number passed through is a prime'''
    sqrt_of_num = int(math.sqrt(number))
    range_to_check = sqrt_of_num + 1    
    i = 2
    if number == 0 or number == 1:
        return False
    while i < range_to_check:
        if (number % i) == 0:
            return False
        i += 1
    
    return True

# TESTING - prime_checker function
list_of_nums_to_check = []
[list_of_nums_to_check.append(i) for i in range(101)]
list_of_primes_less_than_100 = []
for num in list_of_nums_to_check:
    is_prime = prime_checker(num)
    if is_prime == True:
        list_of_primes_less_than_100.append(num)
    is_prime = False

#print(list_of_primes_less_than_100) # should return a list of 25 nums
#print(len(list_of_primes_less_than_100)) # should return 25
    
def eulers_toilent_calculator(p, q):
    '''finds eulers toilent'''
    eulers_tiolnet = (p - 1) * (q - 1)
    return eulers_tiolnet

# print(eulers_toilent_calculator(5, 7)) # will print 24

# function to create; 
#   - Public 'e' function
#   - gcd finder
#   - private key finder
#   - Encryption and Decryption function
