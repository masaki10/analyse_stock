from pandas_datareader import data
import csv
import datetime



if __name__ == "__main__":
    print("hello")
    code = "7203"

    df = data.DataReader(f"{code}.T", "yahoo", "2022-04-01", "2022-04-30")
    print(df.index)
    # print(df[["GC"]])
    print(df.loc["2022-04-28"]["High"])

    dt_today = datetime.date.today()
    print(dt_today + datetime.timedelta(days=1))