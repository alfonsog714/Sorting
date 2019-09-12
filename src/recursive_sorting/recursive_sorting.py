# TO-DO: complete the helper function below to merge 2 sorted arrays

#arrA and arrB must be sorted! Expect already sorted arrays.
def brady_merge( arrA, arrB ):
    print(f"MERGE: {arrA} - {arrB}")
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
    a_i = 0 # tracker for item from arrA
    b_i = 0 # tracker for item from arrB
    # for each index in the merged array `elements`...
    for i in range(num_elements):
        # Find the smallest first-item between arrA and arrB
        # Add that to `elements` at the given index
        # Increment the a/b counter
        # Cases --- ORDER OF CONDITIONALS MATTERS
        # 1. Array A is empty, B is not empty
        if a_i >= len(arrA):
            merged_arr[i] = arrB[b_i]
            b_i += 1
        # 2. Array B is empty, A is not empty
        elif b_i >= len(arrB):
            merged_arr[i] = arrA[a_i]
            a_i += 1
        # 3. A has the smaller element
        elif arrA[a_i] < arrB[b_i]:
            merged_arr[i] = arrA[a_i]
            a_i += 1
        # 4. B has the smaller element
        else: # arrA[a_i] >= arrB[b_i]
            merged_arr[i] = arrB[b_i]
            b_i += 1
        
    print(f"**MERGED - {merged_arr}**")
    return merged_arr


# def my_merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB ) # In the case of using the lists above, this would return 10, coming from 5 + 5.
#     merged_arr = [0] * elements # returns an array filled with 10 0's because the result from above was 10.
    
#     # track the index of arrA
#     arrAIndex = 0
#     # start the index of arrB at the end of arrA
#     arrBIndex = len(arrA)
#     for n in arrA:
#         merged_arr[arrAIndex] = n
#         arrAIndex += 1

#     for n in arrB:
#         merged_arr[arrBIndex] = n
#         arrBIndex += 1

#     return merged_arr

# print(merge(a, b))
# print(a + b)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    print(f"MERGE: {arr}")
    # 1. While your data set contains more than one item, split in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element
    #       (a single element cannot be "out of order")
    if len(arr) > 1:
        #Split
        midway_point = len(arr) // 2
        left_arr = arr[:midway_point]
        right_arr = arr[midway_point:]
        #Sort each of the splitted arrays
        sorted_left = merge_sort(left_arr) # These two lines is where the recursion is happening! It's restarting this function because it's calling itself
        sorted_right = merge_sort(right_arr)
        #Merge the sorted arrays
        arr = brady_merge(sorted_left, sorted_right)

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
