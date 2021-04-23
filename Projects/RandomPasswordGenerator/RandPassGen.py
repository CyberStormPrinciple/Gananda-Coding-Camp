import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

def generate_password(length):
    """Generates a random password for given length"""
    password = ''
    cur = 0
    while cur != length:
        password += random.choice(chars)
        cur += 1
    print(password)


if __name__ == "__main__":
    user_input = int(input("Password length: "))
    generate_password(user_input)
