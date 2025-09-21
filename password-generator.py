import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_generator():
    print('*** Welcome To Password Generator ***')
    n_s_letters = int(input('How many small letters you want in your password?\n'))
    n_c_letters = int(input('How many capital letters you want in your password?\n'))
    n_numbers = int(input('How many numbers you want in your password\n'))
    n_symbols = int(input('How many symbolss you want in your password\n'))

    password = []
    for i in range(1, n_s_letters + 1):
        char = random.choice(small_letters)
        password += char
    for i in range(1, n_c_letters + 1):
        char = random.choice(caps_letters)
        password += char
    for i in range(1, n_numbers + 1):
        char = random.choice(numbers)
        password += char
    for i in range(1, n_symbols + 1):
        char = random.choice(symbols)
        password += char
    random.shuffle(password)
    pass_string = ''
    for char in password:
        pass_string += char
    print(f"Your password is :{pass_string}")


pass_generator()

"""
Output:

*** Welcome To Password Generator ***
How many small letters you want in your password?
3
How many capital letters you want in your password?
3
How many numbers you want in your password
2
How many symbolss you want in your password
4
Your password is :!v2N#l$G#C9m

"""
