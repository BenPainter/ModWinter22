# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      The program sorts a given array based off of the algorithm that was given.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was getting the code to know when to stop.
#      It would either keep on looping through it all or it would stop just after a few loops.
#      But, I was able to figure it out and now it runs the perfect amount of times.
# 5. How long did it take for you to complete the assignment?
#      4 hours


def main(array):
    if array != []:
        if type(array[0]) != type(array[1]):
            print("There are different types in the list")
        else:
            start = 0
            sort = False
            while not sort:
                sub1, sub2 = find_subList(array, start)

                if sub2[0] != 0:
                    array = sort_subList(array, sub1, sub2)
                else:
                    sort = True

                start = sub2[1]
                if sub2[1] == len(array) - 1 or sub1[1] == len(array) - 1:
                    start = 0
            display(array)
    else:
        print("Empty")



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

def display(array):
    print(array)

def sort_subList(array, sub1, sub2):
    sub1index = sub1[0]
    sub2index = sub2[0]
                                                                #A
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


def Test_cases():
    #Short List
    print("\nTest Case: Short List")
    array1 = [1, 7, 5]
    main(array1)

    #Long List
    print("\nTest Case: Long List")
    array2 = [5, 8, 1, 7, 2, 3, 1, 9, 4]
    main(array2)

    #Empty List
    print("\nTest Case: Empty List")
    array3 = []
    main(array3)

    #Already Sorted List
    print("\nTest Case: Already Sorted List")
    array4 = [1,2,3]
    main(array4)

    #Word List
    print("\nTest Case: Word List")
    array5 = ["banana", "a", "coast"]
    main(array5)

    #Combo List
    print("\nTest Case: Combo List")
    array6 = ["banana", 7,"5"]
    main(array6)


Test_cases()

