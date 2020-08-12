from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')
width=0.25
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
x_indexes=np.arange(len(ages_x))
plt.bar(x_indexes-width,dev_y,width=width,color='#444444',linestyle='--')

py_dev_y=[45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes,py_dev_y,width=width,color='#5a7d9a',linewidth='2')

js_dev_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes+width,js_dev_y,width=width,color='#adad3b',linewidth='2')

plt.xticks(ticks=x_indexes,labels=ages_x)
plt.legend(['All Developers','Python Developers','JavaScript Developers'])
plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()