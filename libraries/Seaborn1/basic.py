# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd 
# import numpy as np

# np.random.seed(42)
# Data
# df = pd.DataFrame({
#     'marks':       np.random.randint(40,100,100),
#     'Study_hours': np.random.uniform(2,10,100),
#     'city':        np.random.choice(['Bhopal','Indore','Jabalpur'],100),
#     'gender':      np.random.choice(['Male','Female'],100)})
# # #histogram with kde - see the distribution 
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'], bins=20, kde=True, color='steelblue')
# plt.title('Distribution of Student Marks')
# plt.show()

'''box plot'''
# sns.boxplot(data=df,x='city',y='marks',palette='Set2')
# plt.title('marks distribution by city')
# plt.show()

'''correlation heatmap - critical in data science'''
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks', 'Study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
# plt.title('Correlation Matrix')
# plt.show()

'''Pair plot all relation at once '''
# sns.pairplot(df[['marks', 'Study_hours']],diag_kind='kde')
# plt.show()
