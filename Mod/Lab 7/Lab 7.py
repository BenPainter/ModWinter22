# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the progra


def main():
    array = read_file()
    start = 0
    sort = False
    while not sort:
        sub1, sub2 = find_subList(array, start)

        if sub2[0] != 0:
            array = sort_subList(array, sub1, sub2)
        else:
            sort = True
        
        print(array)
        start = sub2[1]
        if sub2[1] == len(array) - 1 or sub1[1] == len(array) - 1:
            start = 0



def read_file():
    array = [7, 1, 1, 5, 9, 4, 6, 2, 15, 5, 8, 1, 8, 58, 1]
    return array

def find_subList(array, start):
    if start != 0 and start < len(array) - 1:
        sub_start1 = start + 1
    else:
        sub_start1 = 0

    sub_end1 = loop_array(array, sub_start1)
    sub1 = [sub_start1, sub_end1]

    if sub_end1 != len(array) - 1:
        sub_start2 = sub_end1 + 1
        sub_end2 = loop_array(array, sub_start2)
        sub2 = [sub_start2, sub_end2]
        print(sub_start1,sub_start2)
        print(sub_end1,sub_end2)
    elif sub_start1 == 0 and sub_end1 == len(array) - 1:
        sub2 = [0, 0]
    else:
        sub2 = [1,1]

    return sub1, sub2




def loop_array(array, start):
    index = start + 1
    if index != len(array):

        subList_found = False
        while not subList_found:
            last_value = array[index - 1]
            current_value = array[index]
            if current_value < last_value:
                subList_found = True
                return index - 1

            if len(array) - 1 == index:
                subList_found = True
                return index
            index = index + 1
    else:
        return start

def display():
    pass

def sort_subList(array, sub1, sub2):
    sub1index = sub1[0]
    sub2index = sub2[0]
                                                                #A
    print(array)
    new_array = array[:]
    for i in range(0, (sub2[1] + 1) - sub1[0]):                 #B
        if sub1index > sub1[1] and sub2index > sub1[1]:
            return new_array                                    #C
        elif sub1index > sub1[1]:
            new_array[i + sub1[0]] = array[sub2index]
            sub2index  = sub2index + 1                          #D
        elif sub2index > sub2[1]:
            new_array[i + sub1[0]] = array[sub1index]
            sub1index  = sub1index + 1                          #E
        elif array[sub1index] <= array[sub2index]:
            new_array[i + sub1[0]] = array[sub1index]
            sub1index  = sub1index + 1                          #F
        elif array[sub1index] > array[sub2index]:
            new_array[i + sub1[0]] = array[sub2index]
            sub2index  = sub2index + 1                          #G
    
    return new_array                                            #H



main()