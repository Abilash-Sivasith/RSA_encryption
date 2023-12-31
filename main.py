"""Implement RSA encrpytion to encrypt the privided plain-text"""

import math
import random
ALPABET_MAPPING = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}
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

def eulers_toilent_calculator(p, q):
    '''finds eulers toilent'''
    eulers_tiolnet = (p - 1) * (q - 1)
    return eulers_tiolnet

def public_e_finder(p, q):
    '''find the publically used 'e' needed for encrypted messages to be sent'''
    e_to_test = random.randrange(1, 10000000)
    gcd_of_e_and_euler_toilent = is_gcd_equal_to_one(e_to_test, eulers_toilent_calculator(p ,q))
    if gcd_of_e_and_euler_toilent is True:
        return e_to_test
    else:
        return public_e_finder(p, q)

def gcd_finder(a, b):
    '''finds the greatest common divisors'''
    if a == 0 :
        return b
    elif b == 0:
        return a
    else:
        gcd = gcd_finder(b % a , a)
        return gcd
    
def is_gcd_equal_to_one(a, b):
    '''return true if gcd == 1'''
    gcd = gcd_finder(a, b)
    if gcd == 1:
        return True
    return False

def linear_combination(a, b):
    """finds the linear combination of a and b given that gcd(a,b) == 1"""
    gcd_of_a_and_b = is_gcd_equal_to_one(a,b)
    if gcd_of_a_and_b is True:
        if a == 0:
            return 0 , 1
        elif b == 0 :
            return 1, 0
        else:
            x_lots_of_b, x_lots_of_a = linear_combination(b % a, a)
            gcd = gcd_finder(a,b)
            return (x_lots_of_a - (b // a) * x_lots_of_b ), x_lots_of_b

def private_d_and_public_e_finder(p, q):
    '''find the private key 'd' were d = e^-1 mod(phi(n)) and returns both'''
    public_e = public_e_finder(p, q)
    euler_toilent_p_q = eulers_toilent_calculator(p, q)
    private_d, other = linear_combination(public_e,euler_toilent_p_q)
    return private_d, public_e

def RSA_encryption(plain_text, p , q):
    '''encrpyts provided plain text and encrpyts text with the RSA system, p and q are choosn primes'''
    private_d, public_e = private_d_and_public_e_finder(p, q)
    list_of_letters_to_encode = []
    encoded_list = []
    for letter in plain_text.lower():
        if letter.isalnum():
            list_of_letters_to_encode.append(letter)
    for letter in list_of_letters_to_encode:
        letter_as_num = ALPABET_MAPPING[letter]
        encoded_list.append((letter_as_num ** public_e) % 24)
    return encoded_list



def RSA_decryption():
    '''decrypts given cipher text that has been encrypted using the RSA system'''
    pass

