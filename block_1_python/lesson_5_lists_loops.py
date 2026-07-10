#1
test_results = [
    {"name": "Тест логина", "passed": True},
    {"name": "Тест регистрации", "passed": False},
    {"name": "Тест поиска", "passed": True},
    {"name": "Тест оформления заказа", "passed": False},
    {"name": "Тест выхода из системы", "passed": True},
]

for test in test_results:
    if test["passed"]:
        print(f'[ПРОЙДЕН] {test["name"]}')
    else:
        print(f'[ПРОВАЛЕН] {test["name"]}')

failed_tests = [test["name"] for test in test_results if not test["passed"]]

print(f"Провалено тестов: {len(failed_tests)}")
print("Провалившиеся тесты:", failed_tests)

print(all(test['passed'] for test in test_results))

#2
users = [
    {"username": "ivan_petrov", "age": 25, "email": "ivan@test.com"},
    {"username": "an", "age": 17, "email": "annatest.com"},
    {"username": "petr_smirnov", "age": 16, "email": "petr@test.com"},
    {"username": "maria_k", "age": 30, "email": "maria@test.com"},
]

def filter_valid_users(users, min_age=18):
    users_list = []
    for user in users:
        if user["age"] >= min_age and len(user["username"]) >= 3 and '@' in user["email"]:
            users_list.append(user['username'])
    return users_list

print(filter_valid_users(users))

#3
def retry_connection(max_attempts=5):
    count = 0
    connected = False
    while count < max_attempts:
        count += 1
        print(f'Попытка №{count}...')
        if count == 3:
            connected = True
            print(f'Подключено с попытки {count}')
            break

    if not connected:
        print(f'Не удалось подключиться после {max_attempts} попыток')

retry_connection(max_attempts=5)
retry_connection(max_attempts=2)


#4
expected_titles = ["Главная страница", "Каталог", "Корзина", "Профиль"]
actual_titles = ["Главная страница", "Каталог товаров", "Корзина", "Профиль"]

for expect, actual in zip(expected_titles, actual_titles):
    if expect != actual:
        print(f'[ПРОВАЛЕН] Ожидалось: {expect}, получено: {actual}')
    else:
        print(f'[ПРОЙДЕН] Ожидалось: {expect}, получено: {actual}')