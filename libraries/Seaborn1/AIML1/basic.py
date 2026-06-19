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


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm 

# mean_h, std_h = 165, 7

# prob = 1 - norm.cdf(175, mean_h, std_h)
# print(f'P(heigh > 175cm) = {prob:.4f} = {prob*100:.1f}%')

# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')


# from sklearn.model_selection import train_test_split, cross_val_score
# import numpy as np
# np.random.seed(42)
# x = np.random.randn(500, 5) 
# y = np.random.randint(0,2,500)

# X_train,X_test,y_train,y_test = train_test_split(
#     x, y, test_size=0.2, random_state=42, stratify=y
# )
# print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=50, random_state=42)
# cv_scores = cross_val_score(model,x,y, cv=5, scoring='accuracy')
# print('f CV Scores each fold: {cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f} +_ {cv_scores.std():.4f}') 

# import numpy as np
# from   scipy import stats
# import matplotlib.pyplot as plt

# n_A, conv_A = 1000, 52
# n_B, conv_B = 1000,68
# rate_A = conv_A / n_A
# rate_B = conv_B / n_B

# print(f'Version A conversion rate: {rate_A*100:.1f}%')
# print(f'Version B conversion rate: {rate_B*100:.1f}%')
# print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# table = [[conv_A, n_A-conv_A],[conv_B, n_B-conv_B]]
# chi2, p_value, dof, expected = stats.chi2_contingency(table)

# print(f'Chi-square: {chi2:.4f}')
# print(f'P-value: {p_value:.4f}')
# print('Result:', 'SIGNIFICANT - B is better!' if p_value<0.05 else 'NOT singnificant - could be random')
  
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#study hours vs exam marks
study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5] 
marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]

x = np.array(study).reshape(-1,1)
y = np.array(marks)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

print(f'Slope: {model.coef_[0]:.2f}(marks increase per study hour)')
print(f'Intercept: {model.intercept_:.2f}(marks at 0 study hours)')

Y_pred = model.predict(x_test)
print(f'R^2 score: {r2_score(y_test,Y_pred):.4f} (1.0 = perfect)')
print(f'RMSE: {mean_squared_error(y_test,Y_pred)**0.5: .2f}')

new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks:{new_pred:.1f}')

#plot
plt.figure(figsize=(9,5))
plt.scatter(x,y,color = 'steelblue', s=100,alpha=0.8, label ='Actual')
plt.plot(x,model.predict(x),color='red',linewidth=2, label='predicted line')
plt.xlabel('study hours/day'); plt.ylabel('exam marks')
plt.title('linear regression - study hour vs marks')
plt.legend(); plt.grid(True,alpha=0.3); plt.show()