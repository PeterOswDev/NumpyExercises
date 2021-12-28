import numpy as np

print("Creating 8X3 array using numpy.arange")
sampleArray = np.arange(10,34,1)
sampleArray = sampleArray.reshape(8,3)
print(sampleArray)
print("\nDividing 8X3 array into 4 sub array\n")
subArrays = np.split(sampleArray, 4)
print(subArrays)

print("Printing original array")
sampleArray_2 = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray_2)

sortArrayByRow = sampleArray_2[:,sampleArray_2[1,:].argsort()]
print("Sorting Original array by second row")
print(sortArrayByRow)

print("Sorting Original array by second column")
sortArrayByColumn = sampleArray_2[sampleArray_2[:,1].argsort()]
print(sortArrayByColumn)



print("Printing Original array")
sampleArray_3 = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray_3)

minOfAxisOne = np.amin(sampleArray_3, 1)
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = np.amax(sampleArray_3, 0)
print("Printing amax Of Axis 0")
print(maxOfAxisOne)

#Delete the second column from a given array and insert the following new column in its place.

print("Printing original array")
sampleArray_4 = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray_4)

print("Array after deleting column 2 on axis 1")
sampleArray_4 = np.delete(sampleArray_4, 1, axis=1)
print(sampleArray_4)

arr = np.array([[10,10,10]])
print("Array after inserting column 2 on axis 1")
sampleArray_4 = np.insert(sampleArray_4, 1, arr,axis=1)
print(sampleArray_4)






