from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')

data=pd.read_csv('data3.csv')
ages=data['Age']
id=data['Responder_id']
bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins=bins,edgecolor='black')
plt.legend(['All Developers','Python Developers','JavaScript Developers'])
plt.title('Ages of Respondants')
plt.xlabel('Ages')
plt.ylabel('Responses')
plt.tight_layout()
plt.show()