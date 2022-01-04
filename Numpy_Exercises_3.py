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


# exercise_3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Method3: ",exercise_3.reshape(4,3))  # 4 rows, 3 columns

exercise_3 = np.arange(4).reshape(2,-1)
print("The original array:\n", exercise_3, "\n")
print("Method 1: \n", exercise_3 + np.full((2,2),202), "\n")
print("Method 2: \n", exercise_3 + 202*np.ones((2,2)))


# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)

# a = np.array([1,2,3,4,5,6])
# b = np.array([[1,2,3,4],[5,6,7,8], [9,10,11,12]])
# print(a[0])
# print(b[1])
# print(np.zeros(3))
# print(np.ones(2))
# print(np.empty(3))
# print(np.arange(4))
# print(np.linspace(0,10, num=5))
#
# x = np.ones(2, dtype=np.int64)
# print(x)

#Adding, removing, and sorting elements

arr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arr))

#argsort
# x = np.array([3,1,2])
# print(np.argsort(x))
#
# print(np.array([[0,3], [2,2]]))

# ind = np.argsort(x, axis=0)
# print(ind)
# print(np.take_along_axis(x, ind, axis=0))

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
#
# c = np.concatenate(a,b)
# print(c)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

z = np.concatenate((x, y), axis=0)
print(z)

array_example = np.array([[[0, 1 ,2, 3],
                           [4, 5, 6, 7]],
                          [[0, 1, 2, 3],
                           [4, 5, 6,7]],
                          [[0, 1, 2, 3],
                           [4, 5 ,6 ,7]]])

print(array_example)

print(array_example.ndim)
print(array_example.size)
print(array_example.shape)















