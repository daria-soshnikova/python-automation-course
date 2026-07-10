from test_scenario import TestScenario
from report_builder import build_full_report, save_report_to_file
from site_checker import check_site_availability


def create_sample_scenarios():
    """Создаёт набор тестовых сценариев для демонстрации"""
    return [
        TestScenario("Тест авторизации", [True, True, True]),
        TestScenario("Тест оформления заказа", [True, False, True, True]),
        TestScenario("Тест поиска товара", [True, True]),
        TestScenario("Тест удаления аккаунта", [False, False, True]),
        TestScenario("Тест восстановления пароля", [True, True, True, True]),
    ]


def main():
    print("Запуск трекера тестовых сценариев...\n")

    scenarios = create_sample_scenarios()

    report = build_full_report(scenarios)
    print(report)

    save_report_to_file(report)

    print(f"\nВсего сценариев создано за всё время: {TestScenario.total_scenarios_created}")

    print("\nПроверка доступности демонстрационного сайта...")
    result = check_site_availability("https://api.github.com")
    if result["is_available"]:
        print(f"Сайт {result['url']} доступен (статус {result['status_code']})")
    else:
        print(f"Сайт {result['url']} недоступен")


if __name__ == "__main__":
    main()