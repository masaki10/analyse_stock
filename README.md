## System analysing stock
develop this system to studing fintech, and twitter bot(@tweet_stockinfo) analysing result tweet

### Setup

create virtual env and install lib
```
python -m venv stock
source stock/bin/activate
pip install -r requirements.txt
```

add config.py to ./

`config.py`

```
import datetime

API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

TODAY_DATE = datetime.date.today()  
```

run system below cmd

```
python main.py
```

### implimented analysing method

- moving average
- golden/dead cross

### analysing method implemented in the future
- deviation rate