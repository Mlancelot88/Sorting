# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr

## Testing
my_arr = [2,5,9,7,4,1,3,8,6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 1
    while i < len(arr):
        current_num = arr[i]
        j = i-1
        while j >= 0 and arr[j] > current_num:
            arr[j+i] = arr[i]
            j -= 1

        arr[j+1]=current_num
        i += 1

    # First Attempt:
    for i in range(1, len(arr)):
        current_num = arr[i]
        index = i

        while index > 0 and arr[index-1] > current_num:
            arr[index] = arr[index-1]
            index -= 1

        arr[index] == current_num

    return arr

# Testing
arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = bubble_sort(arr)
print(arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr