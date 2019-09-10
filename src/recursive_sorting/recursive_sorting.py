# TO-DO: complete the helper function below to merge 2 sorted arrays

#Example arrays: 
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB ) # In the case of using the lists above, this would return 10, coming from 5 + 5.
    merged_arr = [0] * elements # returns an array filled with 10 0's because the result from above was 10.
    
    # track the index of arrA
    arrAIndex = 0
    # start the index of arrB at the end of arrA
    arrBIndex = len(arrA)
    for n in arrA:
        merged_arr[arrAIndex] = n
        arrAIndex += 1

    for n in arrB:
        merged_arr[arrBIndex] = n
        arrBIndex += 1

    return merged_arr

print(merge(a, b))
# print(a + b)
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
