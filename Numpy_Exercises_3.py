import numpy as np
#Replace all odd numbers in the given array with -1
exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
exercise_1[exercise_1 % 2 == 1] = -1
print(exercise_1)

#Convert a 1-D array into a 2-D array with 3 rows

exercise_2 = np.array([0,1,2,3,4,5,6,7,8])
print("The original array:\n",exercise_2, "\n")
print("Method 1: \n",exercise_2.reshape(3,-1), "\n")
print("Method_2: \n",exercise_2.reshape(3,3))


exercise_3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Method3: ",exercise_3.reshape(4,3))  # 4 rows, 3 columns















