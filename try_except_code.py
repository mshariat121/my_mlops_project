import pandas as pd
import logging

logging.basicConfig(
    filename="./result.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("SUCCESS: There are {} rows in the dataset".format(df.shape[0]))
        logging.info("SUCCESS: Your data was successfully read in")
        return df
    except (FileNotFoundError, IsADirectoryError):
        logging.error("ERROR: We were not able to find your file")


if __name__ == "__main__":
    df = read_data(
        "/Users/mohammadshariatmadari/MLOps/my_mlops_project/data/server.csv"
    )
    print(df)
    df1 = read_data(".")
    print(df1)
