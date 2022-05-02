from pandas_datareader import data
import csv
import datetime
from moving_average import MovingAverage
from twitter_util import TwitterUtil
import config as cf
import math

if __name__ == "__main__":
    gcs = []
    dcs = []

    with open("./stock_code.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            mv_avg = MovingAverage([5, 25], row[0])
            # mv_avg = MovingAverage([5, 25], "1413")
            mv_avg.calc_cross()
            if mv_avg.get_golden_cross():
                row.append(mv_avg.end_price)
                gcs.append(row)
            if mv_avg.get_dead_cross():
                row.append(mv_avg.end_price)
                dcs.append(row)
    
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