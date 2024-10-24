import math
import data

#All tests for design recipe is the code for the test cases

# Write your functions for each part in the space below.
# Part 1
#purpose: to find the amount of vowels
# input: a word that is a string
# output: a counter that is an int
def vowel_count(word:str)-> int:
    char = list(word)
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    for x in char:
        if x in vowels:
            count = count+1
    return count



# Part 2
# Purpose: to find a  new list consisting of those elements of the input list (in the same order) that are of length 2.
# input: an embedded list
# output: a list with the elements that have a length of 2 in the original list
def short_lists(new:list[list[int]])->list:
    new_list=[]
    for i in range(len(new)):
        if(len(new[i]) == 2):
            new_list.append(new[i])
    return new_list



# Part 3

#purpose: To find a new list with elements (the nested lists) matching those of the input list (in the same order)
# but such that any nested list of length 2 in the result has its elements in ascending order
# input: an embedded list
# output: a new list with elements (the nested lists) matching those of the input
# list (in the same order) but such that any nested list of length 2 in the result has
# its elements in ascending order
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
#Purpose: To find the sum of the input prices as a new Price object but initalized such that the number
# of cents is not above 99.
# Your implementation may assume that the prices passed to the function are properly formed such that the cents are within
# the range 0-99.

#input = 2 price objects
#output = float with total of the 2 price objects

def add_prices(price1,price2):
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars+price2.dollars + (total_cents//100)

    total_cents = total_cents%100
    return total_dollars+total_cents


# Part 5
#purpose: return the area of the provided rectangle
#input: a rectangle object
#output: area of the rectangle as an int
def rectangle_area(points: data.Rectangle)-> float:
    y_distance = points.top_left.y-points.bottom_right.y
    x_distance = points.bottom_right.x-points.top_left.x
    area = y_distance*x_distance
    return area

# Part 6
#purpose: to return the titles of books with a specific author
#input: an author name and a list of book objects
# output: list of strings
def books_by_author(author:str,b_list: list[data.Book]):
    return_list = []
    for i in range(len(b_list)):
        for x in b_list[i].authors:
            if x == author:
                return_list.append(b_list[i].title)
    return return_list


# Part 7
#Purpose: to convert a rectangle into a circle
#input: rectangle object
#output: circle object
def circle_bound(fun:data.Rectangle):
    y_distance = (fun.top_left.y - fun.bottom_right.y)/2
    x_distance = (fun.bottom_right.x - fun.top_left.x)/2
    middle_x = fun.top_left.x + x_distance
    middle_y = fun.top_left.y - y_distance
    pythagX = math.pow((x_distance*2),2)
    pythagY = math.pow((y_distance*2),2)
    radius1 = math.sqrt(pythagX+pythagY)

    return data.Circle((middle_x,middle_y),radius1)




# Part 8
#Purpose: find the employees that are payed less than the average salary
#input: list of employee objects
#output: list of strings
def below_pay_average(E_list: list[data.Employee]):
    # find average pay of all employees
    salary = 0
    Underpayed =[]
    for i in range(len(E_list)):
        money = E_list[i].pay_rate
        salary = salary+money
    average = salary/len(E_list)
    for i in range(len(E_list)):
        if E_list[i].pay_rate < average:
            Underpayed.append(E_list[i].name)
    return Underpayed

