def insertionSort(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        j = i -1

        #compare key with each element on the left of it until an element
        #smaller than it is found
        # for descendig order, change key<Array[j] to Key>Array[j].
        while j >= 0 and key < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = key
    return Array
if __name__ == '__main__':
    Array = [-2, -3, -1, 11, 9, 12, 4, -5, -12, 6, 19, 20]
    print(insertionSort(Array))
