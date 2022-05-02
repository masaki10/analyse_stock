import datetime
from pandas_datareader import data
import numpy as np

class MovingAverage:
    def __init__(self, days, code):
        self.days = sorted(days)
        self.code = code
    
    def _get_stock_price(self):
        end = datetime.date.today()
        start = end + datetime.timedelta(days=365)
        self.df = data.DataReader(f"{self.code}.T", "yahoo", start, end)

    def calc_moving_avgs(self):
        self._get_stock_price()
        for day in self.days:
            self.df[f"MA{str(day)}"] =  self.df["Close"].rolling(window=day).mean()

    def calc_cross(self):
        diff = self.df[f"MA{str(self.days[0])}"] - self.df[f"MA{str(self.days[0])}"]
        self.df["Cross"] = np.where(np.sign(diff) - np.sign(diff.shift(1)) == 2, "GC", np.where(np.sign(diff) - np.sign(diff.shift(1)) == -2, "DC", np.nan))

    def get_golden_cross(self):
        if self.df.loc[datetime.date.today()]["GC"] == np.nan:
            return False
        return True

    def get_dead_cross(self):
        if self.df.loc[datetime.date.today()]["DC"] == np.nan:
            return False
        return True

    def calc_deviation_rate(self):
        pass