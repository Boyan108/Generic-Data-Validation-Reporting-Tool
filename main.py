import pandas as pd
import json


def read_csv(file_path):
    return pd.read_csv(file_path)

def load_rules(config_path):
    with open(config_path, encoding="utf-8") as file:
        rules = json.load(file)
    return rules

def validate_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    passed = len(missing_columns) == 0
    return passed, missing_columns

def main():
    file_path = "data/sample.csv"
    df = read_csv(file_path)
    row_count, col_count = df.shape
    print(f"Number of rows: {row_count}")
    print(f"Number of columns: {col_count}")
    print("Columns:", list(df.columns))
    print("\nValidation: required columns")
    config_path = "config/rules.json"
    rules = load_rules(config_path)
    passed, missing = validate_columns(df, rules["required_columns"])
    if passed:
        print("PASS: All required columns present")
    else:
        print(f"FAIL: Missing columns: {sorted(missing)}")

    extra = [col for col in df.columns if col not in rules["required_columns"]]
    if extra:
        print(f"Info: Extra columns: {extra}")

if __name__ == "__main__":
    main()