from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')
data=pd.read_csv('data4.csv')
views=data['view_count']
likes=data['likes']
ratio=data['ratio']

plt.scatter(views,likes,c=ratio,cmap='summer',linewidths=1,edgecolors='black',alpha=0.75)
cbar = plt.colorbar()
cbar.set_label('Likes/Dislikes ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('Views count')
plt.ylabel('Total Likes')
plt.tight_layout()
plt.show()