from datetime import datetime
from amoex.shares import HistoryShares
from amoex.base import securities

hs = HistoryShares()
d = datetime.strptime('2019-01-08', '%Y-%m-%d')

data = hs.get_securities_sync(d)
print(data['SBER'])
print(data['MTSS'])