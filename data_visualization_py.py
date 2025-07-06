# -*- coding: utf-8 -*-
"""Data Visualization.py

Original file is located at
    https://colab.research.google.com/drive/1wx9QBOPYr52y5St13uX48_aj4IlFafOm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset = pd.read_csv('/content/Students Social Media Addiction.csv')

dataset.head()

dataset.shape

dataset.info()

x = dataset['Age']
y = dataset['Avg_Daily_Usage_Hours']

print(x)

print(y)

plt.bar(x, y)
plt.title('BAR PLOT')
plt.xlabel('Age')
plt.ylabel('Avg_Daily_Usage_Hours')
plt.show()

plt.plot(x, y)
plt.title('LINE CHART')
plt.xlabel('Age')
plt.ylabel('Avg_Daily_Usage_Hours')
plt.grid(True)
plt.show()

sns.histplot(x=x, y=y)
plt.title('HISTOGRAM')
plt.xlabel('Age')
plt.ylabel('Avg_Daily_Usage_Hours')
plt.show()

sns.scatterplot(x=x, y=y)
plt.title('SCATTER PLOT')
plt.xlabel('Age')
plt.ylabel('Avg_Daily_Usage_Hours')
plt.show()

numerical_data = dataset[['Age', 'Avg_Daily_Usage_Hours']]

correlation_matrix = numerical_data.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Age and Avg_Daily_Usage_Hours')
plt.show()

plt.pie(x, data = y)
plt.title('PIE PLOT')
#plt.axis('equal')
plt.show()
