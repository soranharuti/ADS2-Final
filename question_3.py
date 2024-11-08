# function quicksort(array, low, high)
#     if low < high then
#         pivotIndex = partition(array, low, high)
#         quicksort(array, low, pivotIndex - 1)
#         quicksort(array, pivotIndex + 1, high)
#     end if
# end function
#
# function partition(array, low, high)
#     pivotIndex = (low + high) / 2
#     pivotValue = array[pivotIndex]
#     swap array[pivotIndex] with array[high]
#     storeIndex = low
#     for i from low to high - 1 do
#         if array[i] ≤ pivotValue then
#             swap array[i] with array[storeIndex]
#             storeIndex = storeIndex + 1
#         end if
#     end for
#     swap array[storeIndex] with array[high]
#     return storeIndex
# end function


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

def partition(array, low, high):
    # choosing middle element as pivot
    pivot_index = (low + high) // 2
    pivot_value = array[pivot_index]
    # moving pivot to end
    array[pivot_index], array[high] = array[high], array[pivot_index]
    store_index = low
    # comparing and swap
    for i in range(low, high):
        if array[i] <= pivot_value:
            array[i], array[store_index] = array[store_index], array[i]
            store_index += 1
    # moving pivot to its final place
    array[store_index], array[high] = array[high], array[store_index]
    return store_index

# Example
pokemon_names = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee", "Mewtwo"]
quicksort(pokemon_names, 0, len(pokemon_names) - 1)
print(pokemon_names)
