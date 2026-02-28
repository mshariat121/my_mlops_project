import pandas as pd


def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(df.head())
        return df
    except (FileNotFoundError,IsADirectoryError):
        print("We were not able to find your file")


if __name__ == "__main__":
    df = read_data('some_file')
    print(df)
    df1 = read_data('.')
    print(df1)
