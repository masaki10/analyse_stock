import datetime
from pandas_datareader import data
import numpy as np

TODAY_DATE = datetime.date.today()

class MovingAverage:
    def __init__(self, days, code):
        self.days = sorted(days)
        self.code = code
    
    def _get_stock_price(self):
        end = TODAY_DATE
        start = end - datetime.timedelta(days=365)
        try:
            self.df = data.DataReader(f"{self.code}", "yahoo", start, end)
            self.is_data = True
        except:
            self.is_data = False

    def _calc_moving_avgs(self):
        self._get_stock_price()
        if self.is_data:
            for day in self.days:
                self.df[f"MA{str(day)}"] =  self.df["Close"].rolling(window=day).mean()

    def calc_cross(self):
        self._calc_moving_avgs()
        if self.is_data:
            diff = self.df[f"MA{str(self.days[0])}"] - self.df[f"MA{str(self.days[0])}"]
            self.df["Cross"] = np.where(np.sign(diff) - np.sign(diff.shift(1)) == 2, "GC", np.where(np.sign(diff) - np.sign(diff.shift(1)) == -2, "DC", np.nan))

    def get_golden_cross(self):
        if not self.is_data:
            return False
        print(self.df.tail(5))
        try:
            self.end_price = self.df.loc[TODAY_DATE.strftime("%Y-%m-%d")]["Close"]
            if self.df.loc[TODAY_DATE.strftime("%Y-%m-%d")]["Cross"] == "GC":
                return True
            return False
        except:
            return False

    def get_dead_cross(self):
        if not self.is_data:
            return False
        try:
            self.end_price = self.df.loc[TODAY_DATE.strftime("%Y-%m-%d")]["Close"]
            if self.df.loc[TODAY_DATE.strftime("%Y-%m-%d")]["Cross"] == "DC":
                return True
            return False
        except:
            return False

    def calc_deviation_rate(self):
        pass