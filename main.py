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

# TESTING - eulers_toilent_calculator function
# print(eulers_toilent_calculator(5, 7)) # will print 24

def public_e_finder():
    '''find the publically used 'e' needed for encrypted messages to be sent'''
    pass

def gcd_finder(a, b):
    '''finds the greatest common divisors'''
    if a == 0 :
        return b
    elif b == 0:
        return a
    else:
        gcd = gcd_finder(b % a , a)
        return gcd

def private_d_finder():
    '''find the private key 'd' were d = e^-1 mod(phi(n))'''
    pass

def RSA_encryption():
    '''encrpyts provided plain text and encrpyts text with the RSA system'''
    pass

def RSA_decryption():
    '''decrypts given cipher text that has been encrypted using the RSA system'''
    pass

