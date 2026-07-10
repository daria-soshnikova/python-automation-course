def build_scenario_line(scenario):
    """Формирует одну строку отчёта для одного сценария"""
    status = scenario.get_status()
    failed = scenario.get_failed_steps_count()
    total = scenario.get_total_steps_count()
    return f"[{status}] {scenario.name} (провалено шагов: {failed} из {total})"


def build_summary(scenarios):
    """Формирует итоговую сводку по всем сценариям"""
    total_scenarios = len(scenarios)
    passed_scenarios = len([s for s in scenarios if s.is_passed()])
    failed_scenarios = total_scenarios - passed_scenarios
    success_rate = (passed_scenarios / total_scenarios * 100) if total_scenarios > 0 else 0

    summary_lines = [
        "=" * 40,
        "ИТОГОВАЯ СВОДКА",
        "=" * 40,
        f"Всего сценариев: {total_scenarios}",
        f"Пройдено: {passed_scenarios}",
        f"Провалено: {failed_scenarios}",
        f"Успешность: {success_rate:.1f}%",
    ]
    return "\n".join(summary_lines)


def build_full_report(scenarios):
    """Собирает полный отчёт: строки по каждому сценарию + итоговая сводка"""
    lines = [build_scenario_line(scenario) for scenario in scenarios]
    lines.append("")
    lines.append(build_summary(scenarios))
    return "\n".join(lines)


def save_report_to_file(report_text, filepath="report.txt"):
    """Сохраняет отчёт в текстовый файл"""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(report_text)
    print(f"Отчёт сохранён в файл: {filepath}")