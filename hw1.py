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


vowel_count("barn")

# Part 2
# Define a function named short_lists that takes one parameter of type list[list[int]]. This function must return a new list
# consisting of those elements of the input list (in the same order) that are of length 2.

def short_lists(new:list[list[int]])->list:
    new_list=[]
    for i in range(len(new)):
        if(len(new[i]) == 2):
            new_list.append(new[i])
    print(new_list)

short_lists([[3,2],[4,5,6],[5,6,]])


# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


