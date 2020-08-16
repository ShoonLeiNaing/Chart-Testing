from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data=pd.read_csv('data2.csv')
all=data['All_Devs']
ages=data['Age']
py_salaries=data['Python']
js_salaries=data['JavaScript']

fig, (ax1,ax2)=plt.subplots(nrows=2,ncols=1)




ax1.plot(ages,all,label="All Devs")
ax2.plot(ages,py_salaries,label="Python")
ax2.plot(ages,js_salaries,label="JavaScript")
ax1.legend()
ax1.set_title("Median Salary by Age")
ax1.set_ylabel("Median Salary")

ax2.legend()
ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary")

plt.tight_layout()
plt.show()