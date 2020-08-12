from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use('ggplot')

data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang=data['LanguagesWorkedWith']
languages=Counter()
for i in lang:
    languages.update(i.split(';'))

language=[]
popularity=[]
for item in languages.most_common(15):
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()
plt.barh(language,popularity)

plt.title('Most popular languages')
plt.xlabel('Number of people who use')
plt.tight_layout()
plt.show()