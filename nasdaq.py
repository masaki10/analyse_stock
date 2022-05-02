from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from moving_average import MovingAverage
import math
from twitter_util import TwitterUtil
import config as cf

if __name__ == "__main__":
    print("hello")
    df_symbols = get_nasdaq_symbols()
    symbols = df_symbols["NASDAQ Symbol"].tolist()
    names = df_symbols["Security Name"].tolist()
    codes = df_symbols.index.tolist()

    gcs = []
    dcs = []

    for symbol, name, code in zip(symbols, names, codes):
        print(code)
        mv_avg = MovingAverage([5, 25], code)
        mv_avg.calc_cross()
        if mv_avg.get_golden_cross():
            gcs.append([symbol, name, mv_avg.end_price])
        if mv_avg.get_dead_cross():
            dcs.append([symbol, name, mv_avg.end_price])

    tw_util = TwitterUtil()
    cnt = 0
    page = 1
    pages = math.ceil(len(gcs)/10)
    content = f"{cf.TODAY_DATE} golden cross stock({page}/{pages})\n"
    for gc in gcs:
        ctt = f"{gc[1]}({gc[0]}) : {gc[2]}円"
        content += ctt
        cnt += 1
        if cnt == 10:
            tw_util.tweet(content)
            cnt = 0
            page += 1
            content = f"{cf.TODAY_DATE} golden cross stock({page}/{pages})\n"

    cnt = 0
    page = 1
    pages = math.ceil(len(dcs)/10)
    content = f"{cf.TODAY_DATE} dead cross stock({page}/{pages})\n"
    for dc in dcs:
        ctt = f"{dc[1]}({dc[0]}) : {dc[2]}円"
        content += ctt
        cnt += 1
        if cnt == 10:
            tw_util.tweet(content)
            cnt = 0
            page += 1
            content = f"{cf.TODAY_DATE} golden cross stock({page}/{pages})\n"