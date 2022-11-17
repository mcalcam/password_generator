import random

letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
                            "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                            "T", "U", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8",
                            "9", "!", "?"]
    
def generate_passowrd():
    i = 0
    password = ''
    while i < 15:
        if i % 5 == 0 and i != 0:
            password += '-'
        password += letter_bank[random.randint(0, 62)]
        i += 1
    return password
