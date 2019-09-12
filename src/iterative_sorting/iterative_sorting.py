import random
# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # 0, 7
        smallest_index = i
        for j in range(smallest_index + 1, len(arr)):
        # TO-DO: find next smallest element
        # a. Loop through elements on right-hand-side of current index and find the smallest element
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        #b. Swap the element at current index with the smallest element found in above loop
        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # python array swap syntax

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range (0, len(arr) - 1): # same setup as selection sort
        for j in range(0, len(arr) - 1 - i): #apparently using i and j as variables for nested loops is conventional
            if arr[j] > arr[j+1]: # j+1 grabs the element to the right of j
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap the values
    return arr # refer back to lecture video and make sure to understand why using the while loop is superior to this method


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



# a = [1,2,3,4,5,6,7,8, 9, 10, 11, 12, 13,14,15]
# random.shuffle(a)
# for i in range(0, len(a) - 1): 
#     """ 
#     realization - by using the range function, you're providing the for loop the array of indices, e.g [0, 1, 2, 3, 4, 5, 6]
#     You cut off the last number by making it the length of the array - 1. Before this, I thought the i was the value in the array
#     """
#     minIndex = i
#     print(f"This is minIndex before entering the second loop: {minIndex}")
#     print(f"This is I, AKA the current index in the loop: {i}")
#     for j in range(i + 1, len(a)):
#         """
#         Tried using range(a[i:]), didn't work.
#         """
#         print(f"This is J, AKA the index of the next number in the array to the right of I: {j}")
#         if a[j] < a[minIndex]:
#             minIndex = j
#             print(f"This is minIndex after running through the if clause: {minIndex}")
    
#     if minIndex != i:
#         a[i], a[minIndex] = a[minIndex], a[i]

# print(a)

# random.shuffle(a)
# # i = 1
# # print(a[i + 1:])

# print(selection_sort(a))