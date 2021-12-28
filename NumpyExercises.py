import numpy as np
print(np.__version__)

firstArray = np.empty([4,2], dtype=np.uint16)
print("Printing Array")
print(firstArray)
print("Printing numpy array Attributes")
print("1> Array Shape is: ", firstArray.shape)
print("2>. Array dimensions are ", firstArray.ndim)
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)

print("Creating 5X2 array using numpy .arrange")
sampleArray = np.arange(100,200,10)
sampleArray = sampleArray.reshape(5,2)
print(sampleArray)

sampleArray_1 = np.array([[11,22,33],[44,55,66],[77,88,99]])
print("Printing input array: ")
print(sampleArray_1)
print("\n Printing array of items in the third column from all rows")
newArray = sampleArray_1[...,2]
print(newArray)


sampleArray_2 = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("Printing Input Array")
print(sampleArray_2)
print("\n Printing array of odd rows and even columns")
newArray_2 = sampleArray_2[::2,1::2]
print(newArray_2)

arrayOne = np.array([[5, 6, 9], [21,18, 27]])
arrayTwo = np.array([[15,33, 24], [4,7, 1]])

resultArray = arrayOne + arrayTwo
print("addition of two arrays is \n:")
print(resultArray)

for num in  np.nditer(resultArray, op_flags=['readwrite']):
    num[...] = num*num
    print("\nResult array after calculating the square root of all elements\n")
    print(resultArray)

 # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

print("Creating 8X3 array using numpy.arange")




