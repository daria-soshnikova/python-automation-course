class TestScenario:
    total_scenarios_created = 0

    def __init__(self, name, steps_results):
        self.name = name
        self.steps_results = steps_results
        TestScenario.total_scenarios_created += 1

    def get_status(self):
        return "ПРОЙДЕН" if all(self.steps_results) else "ПРОВАЛЕН"

    def get_failed_steps_count(self):
        return len([result for result in self.steps_results if not result])

    def get_total_steps_count(self):
        return len(self.steps_results)

    def is_passed(self):
        return all(self.steps_results)