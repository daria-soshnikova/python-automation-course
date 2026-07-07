class TestResult:
    def __init__(self, test_name, expected, actual):
        self.test_name = test_name
        self.expected = expected
        self.actual = actual

    def check(self):
        return self.expected == self.actual

    def print_result(self):
        status = "ПРОЙДЕН" if self.check() else "ПРОВАЛЕН"
        print(f"[{status}] {self.test_name}")


test1 = TestResult('Тест1', 'Тестовый кейс', 'Тест-кейс')
test1.print_result()

test2 = TestResult('Тест2', 'успешный вход', 'успешный вход')
test2.print_result()

test3 = TestResult('Тест3', 200, 404)
test3.print_result()


class RegistrationForm:
    forms_created = 0

    def __init__(self, min_age=18):
        self.min_age = min_age
        RegistrationForm.forms_created += 1

    def fill_form(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email

    def validate(self):
        return len(self.username) > 3 and self.age >= self.min_age and '@' in self.email

    def show_validation_errors(self):
        if len(self.username) <= 3:
            print(f"Ошибка: имя пользователя слишком короткое ({self.username})")
        if self.age < self.min_age:
            print(f"Ошибка: возраст {self.age} меньше минимального ({self.min_age})")
        if '@' not in self.email:
            print(f"Ошибка: email некорректен ({self.email})")

form1 = RegistrationForm()
form1.fill_form(username="ivan_petrov", age=25, email="ivan@test.com")
print(form1.validate())

form2 = RegistrationForm()
form2.fill_form(username="ai", age=15, email="badmail")
print(form2.validate())
form2.show_validation_errors()

form3 = RegistrationForm(min_age=21)
form3.fill_form(username="anna_k", age=19, email="anna@test.com")
print(form3.validate())
form3.show_validation_errors()

print(RegistrationForm.forms_created)
