import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str)-> int:
    char = list(word)
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    for x in char:
        if x in vowels:
            count = count+1
    print(count)



# Part 2
# Define a function named short_lists that takes one parameter of type list[list[int]]. This function must return a new list
# consisting of those elements of the input list (in the same order) that are of length 2.

def short_lists(new:list[list[int]])->list:
    new_list=[]
    for i in range(len(new)):
        if(len(new[i]) == 2):
            new_list.append(new[i])
    print(new_list)




# Part 3
# Define a function named ascending_pairs that takes one parameter of type list[list[int]]. This function must return a new list
# with elements (the nested lists) matching those of the input list (in the same order) but such that any nested list of length 2
# in the result has its elements in ascending order (really, non-descending; i.e., the first element will be less than or equal to
# the second). The elements of nested lists of length not equal to 2 must remain in the same order as in the input.

def ascending_pairs(new: list[list[int]]) -> list:
    new_list = []
    for i in range(len(new)):
        if len(new[i]) == 2:
            e_list = []
            if new[i][0] >= new[i][1]:
                e_list.append(new[i][1])
                e_list.append(new[i][0])
                new_list.append(e_list)
            elif new[i][0] <= new[i][1]:
                e_list.append(new[i][0])
                e_list.append(new[i][1])
                new_list.append(e_list)
        else:
            new_list.append(new[i])
    print(new_list)


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


