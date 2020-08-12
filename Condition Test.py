from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv('data2.csv')
ages=data['Age']
all=data['All_Devs']
py_dev=data['Python']
js_dev=data['JavaScript']
overall_median=57287
label=['All Developers','Python Developers','JavaScript Developers']
color=['#63c5da','#52b2bf','#0492c2']
plt.plot(ages,all,color='#444444',linestyle='--')
plt.plot(ages,py_dev,color='#52b2bf')
# plt.plot(ages,js_dev,color='#0492c2')
plt.legend(labels=label)

plt.fill_between(ages,py_dev,all,interpolate=True,
                 where=(py_dev > all),alpha=0.25,label="Above Avg")

plt.fill_between(ages,py_dev,all,interpolate=True,color='red',
                 where=(py_dev <= all),alpha=0.25,label="Below Avg")


plt.title('My stack plot')
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()