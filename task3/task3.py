import json
import sys


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def update_values(test_data, values_dict):
    if "id" in test_data and test_data["id"] in values_dict:
        test_data["value"] = values_dict[test_data["id"]]

    if "values" in test_data:
        for sub_test in test_data["values"]:
            update_values(sub_test, values_dict)


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <values.json> <tests.json> <report.json>"
        )
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    # Convert values list to dictionary for easy access by id
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Write values to test structure
    for test in tests_data["tests"]:
        update_values(test, values_dict)

    # Save structure to report.json
    save_json(tests_data, report_path)


if __name__ == "__main__":
    main()
