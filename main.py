# sorting two arrays in python 
def sort(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        print(arr1[i], arr2[i])
print(sort([1,2,5,7,12,6],[1,2,3,4,5,6,7,8,9,10]))

