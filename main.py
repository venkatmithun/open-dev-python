from utils.api_helpers import fetch_data
import pandas as pd


def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)
    df = pd.DataFrame(data)
    print(df.head())


if __name__ == "__main__":
    main()
