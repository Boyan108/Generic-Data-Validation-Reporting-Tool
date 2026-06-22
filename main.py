import pandas as pd


def read_csv(file_path):
    return pd.read_csv(file_path)

def main():
    file_path = "data/sample.csv"
    df = read_csv(file_path)
    rows, columns = df.shape
    print(f"Number of rows: {rows}")
    print(f"Number of columns: {columns}")
    print("Columns:", list(df.columns))
    print("First 5 rows of the DataFrame:\n", df.head())
    print("\nData types of each column:", df.dtypes)

if __name__ == "__main__":
    main()