import math
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
    return count



# Part 2
# Define a function named short_lists that takes one parameter of type list[list[int]]. This function must return a new list
# consisting of those elements of the input list (in the same order) that are of length 2.

def short_lists(new:list[list[int]])->list:
    new_list=[]
    for i in range(len(new)):
        if(len(new[i]) == 2):
            new_list.append(new[i])
    return new_list



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
    return new_list


# Part 4
# Define a function named add_prices with two parameters each of type Price (defined in the provided files).
# This function must compute and return the sum of the input prices as a new Price object but initalized such that the number
# of cents is not above 99. There are multiple valid approaches to the implementation of this function including with or without
# the use of a conditional statement.
# Your implementation may assume that the prices passed to the function are properly formed such that the cents are within
# the range 0-99.

def add_prices(price1,price2):
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars+price2.dollars + (total_cents//100)

    total_cents = total_cents%100
    return total_dollars+total_cents


# Part 5
#Define a function named rectangle_area with one parameter of type Rectangle (defined in the provided files). This function must
# compute and return the area of the provided rectangle with the assumption that the rectangle is properly axis-aligned (
# i.e., the top-left corner is above and to the left of the bottom-right corner, the vertical sides of the rectangle are parallel
# to the y-axis, and the horizontal sides of the rectangle are parallel to the x-axis).

def rectangle_area(points: data.Rectangle)-> float:
    y_distance = points.top_left.y-points.bottom_right.y
    x_distance = points.bottom_right.x-points.top_left.x
    area = y_distance*x_distance
    return area

# Part 6
def books_by_author(author:str,b_list: list[data.Book]):
    return_list = []
    for i in range(len(b_list)):
        for x in b_list[i].authors:
            if x == author:
                return_list.append(b_list[i].title)
    return return_list


# Part 7
def circle_bound(fun:data.Rectangle):
    y_distance = (fun.top_left.y - fun.bottom_right.y)/2
    x_distance = (fun.bottom_right.x - fun.top_left.x)/2
    middle_x = fun.top_left.x + x_distance
    middle_y = fun.top_left.y - y_distance
    pythagX = pow((x_distance*2),2)
    print(pythagX)
    pythagY = pow((y_distance*2),2)
    radius = math.sqrt(pythagX+pythagY)

    return data.Circle((middle_x,middle_y),radius)



# Part 8

def below_pay_average(list: list[data.Employee]):
    # find average pay of all employees
    salary = 0
    for i in list:
        money = list[i].pay_rate
        salary = salary+money
    average = salary/len(list)
    for i in list:
        if list[i].pay_rate < average:
            return list[i].name

