import sys
import json


def fill_report(tests, values):
    """
  Заполняет файл report.json значениями из values.json.

  Args:
    tests: данные из tests.json.
    values: данные из values.json.
  """
    for test in tests:
        for val in values:
            if test['id'] == val['id']:
                test['value'] = val['value']
                break
        if 'values' in test:
            fill_report(test['values'], values)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Ошибка: требуется три аргумента: values.json, tests.json, report.json.")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        with open(values_file, 'r') as f:
            values_data = json.load(f)['values']

        with open(tests_file, 'r') as f:
            tests_data = json.load(f)['tests']

        fill_report(tests_data, values_data)

        with open(report_file, 'w') as f:
            json.dump({"tests": tests_data}, f, indent=2)

    except FileNotFoundError:
        print("Ошибка: один или несколько файлов не найдены.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Ошибка: некорректный формат JSON в одном из файлов.")
        sys.exit(1)
