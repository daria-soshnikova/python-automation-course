#1
def check_order_status(order):
    if not order["is_paid"]:
        return "Заказ не оплачен"

    if not order["is_shipped"]:
        return "Заказ оплачен, ожидает отправки"

    if not order["is_delivered"]:
        return "Заказ в пути"

    return "Заказ доставлен"

print(check_order_status({"is_paid": False, "is_shipped": False, "is_delivered": False}))
print(check_order_status({"is_paid": True, "is_shipped": False, "is_delivered": False}))
print(check_order_status({"is_paid": True, "is_shipped": True, "is_delivered": False}))
print(check_order_status({"is_paid": True, "is_shipped": True, "is_delivered": True}))


#2
def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append('длина меньше 8 символов')

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        errors.append('нет заглавной буквы')

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        errors.append('нет цифры')

    if ' ' in password:
        errors.append('содержит пробел')

    return errors


#3
class TestScenario:
    def __init__(self, name: str, steps_results: list):
        # steps_results — список bool значений, результат каждого шага теста
        self.name = name
        self.steps_results = steps_results

    def get_status(self):
        if all(self.steps_results):
            return 'ПРОЙДЕН'
        else:
            return 'ПРОВАЛЕН'

    def get_failed_steps_count(self):
        N = 0
        for result in self.steps_results:
            if result == False:
                N += 1
        return N

    def print_report(self):
        status = self.get_status()
        failed = self.get_failed_steps_count()
        total = len(self.steps_results)
        print(f'[{status}] {self.name} (провалено шагов: {failed} из {total})')

test1 = TestScenario('Тест оформления заказа', [True, True, False, True, False, False])
test1.print_report()

test2 = TestScenario('Тест входа в систему', [True, True, True])
test2.print_report()

test3 = TestScenario('Тест удаления аккаунта', [False, False, False])
test3.print_report()
