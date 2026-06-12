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