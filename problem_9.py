import random

def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    upper_c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
               "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

    n_letters = random.randint(6, 8)
    n_upper_c = random.randint(3, 4)
    n_numbers = random.randint(2, 4)
    n_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0, n_letters - 1)] 
    password_numbers = [random.choice(numbers) for _ in range(0, n_numbers - 1)]
    password_symbols = [random.choice(symbols) for _ in range(0, n_symbols - 1)]
    password_upper_c = [random.choice(upper_c) for _ in range(0, n_upper_c - 1)]

    password_list = password_letters + password_upper_c + password_numbers + password_symbols

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    return generated_password

print(generate_password())