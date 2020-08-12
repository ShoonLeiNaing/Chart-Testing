from matplotlib import pyplot as plt
plt.style.use('ggplot')

ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x,dev_y,color='#444444',linestyle='--')

py_dev_y=[45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y,color='#5a7d9a' ,marker='.',linewidth='2')

js_dev_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y,color='#adad3b',linewidth='2')


plt.legend(['All Developers','Python Developers','JavaScript Developers'])
plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()