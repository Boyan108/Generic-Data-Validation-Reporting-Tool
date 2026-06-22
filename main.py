import csv

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def main():
    file_path = 'data/sample.csv'  
    data = read_csv(file_path)
    columns = data[0].keys() if data else []
    print("Columns: "," | ".join(columns)) 
    row_count = len(data)
    print(f"Total rows: {row_count}")
    print(" | ".join(columns))
    print("-" * 40)

    for row in data:
        print(" | ".join(row[col] for col in columns))

if __name__ == "__main__":
    main()