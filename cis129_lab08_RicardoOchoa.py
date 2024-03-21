print("Palindrome code")

from string import digits,ascii_lowercase

chars = digits + ascii_lowercase

def is_palindrome(pal_str):
    ##Convert all the letters to lowercase
    pal_str_low=[c for c in pal_str.lower() if c in chars]
    ##Reverse the string and compare with original string
    return pal_str_low[::-1] == pal_str_low != []

print(is_palindrome("madam "))
