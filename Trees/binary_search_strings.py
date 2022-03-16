import sys
# ffrom load import load_strings

# names = load_strings(sys.argv[1])

names = ["kerubo", "atieno", "mark", "john", "wanja", "cheptoo", "doro"]
search_names = ["mark", "wanja", "doro"]

def binary_search(collection, target):
    first = 0
    last = len(collection) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midppoint] , target:
            first = midpoint + 1
        else:
            last = midpoint - 1
        return None

    for n in search_names:
        index = binary_search(names, n)
        print(index)
        