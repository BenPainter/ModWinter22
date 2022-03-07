'''
Function main():
    array <- read_file()
    start <- 0
    sort <- False
    While not sort:
        sub1, sub2 <- find_subList(array, start)
        If sub2[0] != 0:
            array <- sort_subList(array, sub1, sub2)
        Else:
            sort <- True
        
        start <- sub2[1]
        If sub2[1] == len(array) - 1 or sub1[1] == len(array) - 1:
            start <- 0


Function find_subList(array, start):

    If start != 0 and start < len(array) - 1:
        sub_start1 <- start + 1
    Else:
        sub_start1 <- 0
    sub_end1 <- loop_array(array, sub_start1)
    sub1 <- [sub_start1, sub_end1]

    If sub_end1 != len(array) - 1:
        sub_start2 <- sub_end1 + 1
        sub_end2 <- loop_array(array, sub_start2)
        sub2 <- [sub_start2, sub_end2]
    Else:
        sub2 = [1, 0]

    Return sub1, sub2




Function loop_array(array, start):
    index <- start + 1
    If index != len(array):
        subList_found <- False
        While not subList_found:
            last_value <- array[index - 1]
            current_value <- array[index]
            If current_value < last_value:
                subList_found <- True
                return index - 1

            If len(array) - 1 == index:
                subList_found <- True
                return index
            index <- index + 1
    Else:
        Return start

Function sort_subList(array, sub1, sub2):
    sub1index <- sub1[0]
    sub2index <- sub2[0]
    new_array <- array[:]
    For i in range(0, (sub2[1] + 1) - sub1[0]):
        
        If sub1index > sub1[1] and sub2index > sub1[1]:
            return new_array
        Elif sub1index > sub1[1]:
            new_array[i + sub1[0]] <- array[sub2index]
            sub2index  <- sub2index + 1
        Elif sub2index > sub2[1]:
            new_array[i + sub1[0]] <- array[sub1index]
            sub1index  <- sub1index + 1

        Elif array[sub1index] <= array[sub2index]:
            new_array[i + sub1[0]] <- array[sub1index]
            sub1index  <- sub1index + 1
        Elif array[sub1index] > array[sub2index]:
            new_array[i + sub1[0]] <- array[sub2index]
            sub2index  <- sub2index + 1
    
    Return new_array


'''