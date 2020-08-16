from matplotlib import pyplot as plt
from datetime import datetime,timedelta
from matplotlib import dates as mpl_dates
import pandas as pd

plt.style.use('seaborn')

data=pd.read_csv('data5.csv')
date=data['Date']
price=data['Close']

data['Date']=pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)

# date_format=mpl_dates.DateFormatter('%b, %d %Y')
#
# plt.gcf().autofmt_xdate()
# plt.gca().xaxis.set_major_formatter(date_format)

plt.plot_date(date,price,linestyle='solid')
plt.tight_layout()
plt.title('Bitcoin Prices')
plt.xlabel('Dates')
plt.ylabel('Closing Price')
plt.show()