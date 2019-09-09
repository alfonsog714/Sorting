import random
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i 
        smallest_index = cur_index
        print(cur_index)
        print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # a. Loop through elements on right-hand-side of current index and find the smallest element
        #b. Swap the element at current index with the smallest element found in above loop




        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



a = [1,2,3,4,5,6,7,8]
random.shuffle(a)
# i = 1
# print(a[i + 1:])

print(selection_sort(a))