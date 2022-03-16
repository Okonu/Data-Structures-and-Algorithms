
def BubbleSort(array):

    # Loop to access each array element
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            # Replace > with < for descending order
            if array[j] > array[j+1]:

                #Swapping elements if elements are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
    