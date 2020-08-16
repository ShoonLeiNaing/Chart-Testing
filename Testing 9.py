from matplotlib import pyplot as plt
import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


x_vals=[]
y_vals=[]

index=count()
def animate(i):
    data = pd.read_csv('data.csv')
    x=data['x_value']
    y1=data['total_1']
    y2=data['total_2']

    plt.cla()
    plt.plot(x,y1,label="Channel 1")
    plt.plot(x,y2,label="Channel 2")
    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(),animate,interval=1000)


plt.plot(x_vals,y_vals)
plt.tight_layout()
plt.show()