import random
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # 0, 7
        cur_index = i 
        smallest_index = cur_index
        
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
for i in range(0, len(a) - 1): 
    """ 
    realization - by using the range function, you're providing the for loop the array of indices, e.g [0, 1, 2, 3, 4, 5, 6]
    You cut off the last number by making it the length of the array - 1. Before this, I thought the i was the value in the array
    """
    minIndex = i
    print(f"This is minIndex before entering the second loop: {minIndex}")
    print(f"This is I, AKA the current index in the loop: {i}")
    for j in range(i + 1, len(a)):
        """
        Tried using range(a[i:]), didn't work.
        """
        print(f"This is J, AKA the index of the next number in the array to the right of I: {j}")
        if a[j] < a[minIndex]:
            minIndex = j
            print(f"This is minIndex after running through the if clause: {minIndex}")

# random.shuffle(a)
# # i = 1
# # print(a[i + 1:])

# print(selection_sort(a))