def is_password_strong(password, min_length=8):
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= min_length and has_digit

def calculate_discount(price, discount_percent=0):
    return price * (1 - 0.01 * discount_percent)

