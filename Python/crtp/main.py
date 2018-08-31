import requests
import ast

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }
r = requests.get('https://www.cryptopia.co.nz/api/GetMarkets', headers=headers)
text = r.text

start_index_hush_btc = text.index('{"TradePairId":4405')
end_index_hush_btc = text.index('{"TradePairId":4408')

text_hush_btc = text[start_index_hush_btc:end_index_hush_btc-1]
text_hush_btc = text_hush_btc.replace('\"', '\'')

#ttt = ""AskPrice":0.00003631,"BidPrice":0.00003162,"Low":0.00002837,"High":0.00003800,"
dct=ast.literal_eval("{'AskPrice' : 0.00003631, 'BidPrice':0.00003162,'Low':0.00002837,'High':0.00003800}")
dct1=ast.literal_eval(text_hush_btc)



index_hush = text.index('HUSH/BTC')

print(dct1.get('AskPrice'))