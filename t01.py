# -*- coding: utf-8 -*-
import pandas as pd

cash_div_history = pd.DataFrame()

url='http://www.wantgoo.com/stock/report/basic_dp?StockNo=2317'
url1='http://www.wantgoo.com/stock/twstock/threebuysellrank?type=%E5%A4%96%E8%B3%87' #外資買賣超排行榜

cash_div_history = pd.read_html(url)
         
cash_db = cash_div_history[0]
print cash_db

print cash_db.iloc[0:5, 0]


