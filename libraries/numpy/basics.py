# import numpy as np

# arr1d = np.array([1, 2, 3, 4, 5])
# arr2d = np.array([[85, 90, 78], [72, 88, 95], [91, 76, 83]])
                 
# print(arr2d.shape)  # Output: (3, 3)
# print(arr2d.ndim)   # Output: 2
# print(arr2d.dtype)   # Output: int64

# zeros = np.zeros((3, 4))
# print(zeros)
# ones = np.ones((2, 5))
# print(ones)
# rng = np.arange(0, 50, 5)
# print(rng)

# lin = np.linspace(0, 1, 11)
# print(lin)

# random = np.random.randint(40, 100, (5, 3))
# print(random)

'''array functions'''


# arr = np.array([10,20,30,40,50])

# print(arr * 2)  # Output: [20 40 60 80 100]
# print(arr + 5)  # Output: [15 25 35 45 55]
# print(arr ** 2)  # Output: [100 400 900 1600 2500] 

'''statistics functions'''

# marks2d = np.array([[85, 90, 78], [72, 88, 95], [91, 76, 83]])
# print(np.mean(marks2d))  # Output: 84.33333333333333
# print(np.mean(marks2d, axis=0))  # Output: [82.66666667 88.         88.        ]
# print(np.mean(marks2d, axis=1))  # Output: [84.33333333 85.         83.33333333]
# print(np.max(marks2d))  # Output: 95
# print(np.std(marks2d))  # Output: 6.236095644623236

'''boolean indexing'''

# arr = np.array([55, 82, 43, 91, 67, 78, 35, 88])
# print(arr[arr > 70])


# import pandas as pd

# data = {

# 'Name': ['Rahul','Monish','Naman','Aman','Baman'],
# 'Age': [22,21,44,55,54],
# 'Marks': [45,67,87,88,45],
# 'City': ['Bhopal','Indore','Bhopal','Sehore','Indore'],
# }

# df = pd.DataFrame(data)
# # print(df)

# # print(df.shape)
# # print(df.head(3))
# # print(df.dtypes)
# # print(df.describe())


# # print("df['Name']: \n",df['Name']) #using sq braket because it say pass rhe list and then pass the key 

# # print(df[['Name','Marks']])

# # print(df[df['Marks']>= 85])
# # print(df[df['City'] == 'Bhopal'])
# # print(df[(df['Marks']>=22) & (df['City'] == 'Indore')])



# # def get_grade(x):
# #     if x >= 90:
# #         return 'A'
# #     elif x>= 75:
# #         return 'B'
# #     else:
# #         return 'c'
    
# # df['Grade'] = df['Marks'].apply(get_grade)
# # print(df['Grade'])
# # print("-----------")
# # print(df)


# #groupby - like excel pivot
# # city_avg = df.groupby('City')['Marks'].mean()
# # print(city_avg)
# '''cleaning csv file, using split/strip/replace'''

# df2 =pd.read_csv('student.csv')
# print(df2)

# #.str. ->vectorization string operation

# # df2 ['Name'] = df2['Name'].str.split() #strip convert each string into list of string
# # print(df2)



# # df2 ['First'] = df2['Name'].str.split().str[0]#for getting 1st last name   
# # print(df2,'\n')                               #for getting 1st last name      
# # df2["Last"] = df2['Name'].str.split().str[1]  #for getting 1st last name 
# # print('/n',df2)

# df2['Name'] = df2['Name'].str.strip()
# print(df2)

# df2['Marks'] = df2['Marks'].str.strip('#')
# print(df2)


# df2['Grade'] = df2['Grade'].str.strip('@')
# df2['Grade'] = df2['Grade'].str.strip('*')
# print(df2)


# df2['City'] = df2['City'].str.replace('dict','')
# df2['City'] = df2['City'].str.replace('City','')
# print(df2)

# df2.to_csv('clean_output.csv', index=False)