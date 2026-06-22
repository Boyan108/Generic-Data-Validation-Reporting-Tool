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

def validate_no_missing(df, columns):
    missing_values = {col: df[col].isnull().sum() for col in columns if col in df.columns}
    passed = all(count == 0 for count in missing_values.values())
    return passed, missing_values

def validate_ranges(df, ranges):
    range_issues = {}
    for col, limits in ranges.items():
        if col in df.columns:
            min_val = limits.get("min", float("-inf"))
            max_val = limits.get("max", float("inf"))
            valid = df[col].dropna()
            too_low = valid < min_val
            too_high = valid > max_val
            out_of_range_count = (too_low | too_high).sum()
            if out_of_range_count > 0:
                range_issues[col] = out_of_range_count
    passed = len(range_issues) == 0
    return passed, range_issues

def main():
    file_path = "data/sample.csv"
    df = read_csv(file_path)
    row_count, col_count = df.shape
    print(f"Number of rows: {row_count}")
    print(f"Number of columns: {col_count}")
    print("Columns:", list(df.columns))
    config_path = "config/rules.json"
    rules = load_rules(config_path)
    print("\nValidation: required columns")

    passed, missing = validate_columns(df, rules.get("required_columns", []))
    if passed:
        print("PASS: All required columns present")
    else:
        print(f"FAIL: Missing columns: {sorted(missing)}")

    print("\nValidation: no missing values in specified columns")
    passed, missing_values = validate_no_missing(df, rules.get("no_missing_in", []))
    if passed:
        print("PASS: No missing values in specified columns")
    else:
        for col, count in missing_values.items():
            if count > 0:
                print(f"FAIL: Column '{col}' has {count} missing values")

    print("\nValidation: value ranges")
    passed, range_issues = validate_ranges(df, rules.get("ranges", {}))
    if passed:
        print("PASS: All values within specified ranges")
    else:
        for col, count in range_issues.items():
            print(f"FAIL: Column '{col}' has {count} values out of specified range")
    
    extra = [col for col in df.columns if col not in rules["required_columns"]]
    if extra:
        print(f"Info: Extra columns: {extra}")

if __name__ == "__main__":
    main()