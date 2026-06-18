# '''statistics for AIML'''
# import numpy as np 
# import pandas as pd 
# import matplotlib.pyplot as plt 
# from scipy import stats 

# #employee salaries (in thousands rs.)
# salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

# #central tendency - where is the 'centre' of data ?
# mean =np.mean(salaries) #average
# median=np.median(salaries) #middle value when sorted
# mode=stats.mode(salaries,keepdims=True).mode[0] #most frequent

# print(f'mean (average):Rs.{mean:.1f}k')
# print(f'median  (middle value):Rs.{median}k')
# print(f'mode  (most common): Rs.{mode}k')

# ''''spread - how varied is data ?'''
# std = np.std(salaries)
# var = np.var(salaries)
# rng = max(salaries)-min(salaries)
# q1 = np.percentile(salaries,25)
# q3 = np.percentile(salaries,75)
# iqr = q3 - q1

# print(f'std Deviation: {std:.2f}K (most important spread measure)')
# print (f'IQR: {iqr}K (Q1={q1}, Q3={q3})')

# #qutline detection using IQR (interquartile Range)
# lower = q1 - 1.5*iqr
# upper = q3 + 1.5*iqr
# outliers = [x for x in salaries if x < lower or x > upper]
# print(f'Outliers: {outliers}')

# import numpy as np
# import seaborn as sns 
# import pandas as pd 
# import matplotlib.pyplot as plt

# data
# np.random.seed(42)
# study = np.random.uniform(2, 10, 60)
# marks = study * 8 + np.random.normal(0, 10, 60)
# marks = np.clip(marks, 30, 100)
# absent = 10 - study + np.random.normal(0, 1, 60)

# df = pd.DataFrame({'Study_Hours':study,'Marks':marks,'Absences':absent})

# corr_matrix = df.corr()
# print(corr_matrix.round(3))

# plt.figure(figsize=(6,4))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
# plt.title('Correlation Matrix'); plt.show()

# #pearson correlation
# r, p_value = stats.pearsonr(study, marks)
# print(f'Study-Marks correlation: r={r:.3f}, p={p_value:.4f}')
# print('Interpretation:', 'strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

mean_h, std_h = 165, 7

prob = 1 - norm.cdf(175, mean_h, std_h)
print(f'P(heigh > 175cm) = {prob:.4f} = {prob*100:.1f}%')

print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')