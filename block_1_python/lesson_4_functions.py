def is_password_strong(password, min_length=8):
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= min_length and has_digit

def is_username_available(username, taken_usernames):
    return username not in taken_usernames

def calculate_discount(price, discount_percent=0):
    return price * (1 - 0.01 * discount_percent)


taken_usernames = ["ivan", "anna", "qwerty123"]

print(is_password_strong('qwerty', 8))
print(is_password_strong('qwerty123', 8))
print(is_username_available('petr', taken_usernames))
print(is_username_available('qwerty123', taken_usernames))
print(calculate_discount(1200, 15))
print(calculate_discount(1200, 120))


def build_test_summary(test_name, passed, details=""):
    status = "PASSED" if passed else "FAILED"
    summary = f"[{status}] {test_name}"
    if details:
        summary += f" - {details}"
    return summary

print(build_test_summary('test1', is_username_available('qwerty123', taken_usernames)))
print(build_test_summary('test2', is_password_strong('qwerty123', 8)))


def run_test_suite(*test_results):
    passed_tests = test_results.count(True)
    count_tests = len(test_results)
    summary = f'Пройден {passed_tests} из {count_tests} тестов'
    return summary

print(run_test_suite(True, False, True, False, True, True))


def apply_discount(price, discount):
    price = price - (price * discount / 100)
    return price

final_price = apply_discount(1000, 10)
print(final_price)