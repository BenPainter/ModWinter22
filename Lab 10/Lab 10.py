import math
array = [31, 72, 10, 32, 18, 95, 25, 50]


def sort_array(array, low, high):
   print(array)
   i_low = low
   i_high = high

   #values_found[Lower section, Higher section]
   values_found = [False, False]

   i_wall = math.floor((i_high + i_low) / 2)
   if not i_wall > high and not i_wall < low: 
    while i_low != i_wall or i_high != i_wall:
            if not values_found[0] and i_low != i_wall:
                if array[i_low] > array[i_wall]:
                    values_found[0] = True
                elif i_low < len(array):
                    i_low += 1

            if not values_found[1] and i_high != i_wall:
                if array[i_high] < array[i_wall]:
                    values_found[1] = True
                else:
                    i_high -= 1

            if values_found[0] == True and values_found[1] == True:
                array[i_low], array[i_high] = array[i_high], array[i_low]
                values_found = [False, False]

            if values_found[0] == True and i_high == i_wall:
                array[i_low], array[i_wall] = array[i_wall], array[i_low]
                values_found = [False, False]

            if values_found[1] == True and i_low == i_wall:
                array[i_high], array[i_wall] = array[i_wall], array[i_high]
                i_wall += 1
                values_found = [False, False]

    print(i_wall)
    if low != high:
        sort_array(array, low, i_wall - 1)
        sort_array(array, i_wall + 1, high)





sort_array(array, 0, len(array) - 1)
print(array)

