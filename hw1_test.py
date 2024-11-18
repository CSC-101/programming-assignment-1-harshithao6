import data
import hw1
import unittest
import math


# Write your test cases for each part below.
# class TestCases(unittest.TestCase):
# Part 1
# def test_first_element_1(self):
#   input = [[1, 2], [3, 4]]
#  result = lab4.first_element(input)
# expected = [1, 3]
# self.assertEqual(expected, result)

class TestCases(unittest.TestCase):

    # Part 1
    def test_vowel_count1(self):
        input = "hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        input = "whatever"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)



    # Part 2
    def test_short_lists1(self):
        input = [[3,5,6],[4,3],[3,2]]
        result = hw1.short_lists(input)
        expected = [[4,3],[3,2]]
        self.assertEqual(expected,result)

    def test_short_lists2(self):
        input = [[5,6,7],[9,8,7],[9,8]]
        result = hw1.short_lists(input)
        expected = [[9,8]]
        self.assertEqual(expected,result)

    # Part 3
    def test_ascending_pairs1(self):
        input = [[4,6,7],[4,3],[2,7]]
        result = hw1.ascending_pairs(input)
        expected = [[4,6,7],[3,4],[2,7]]
        self.assertEqual(expected,result)

    def test_ascending_pairs2(self):
        input = [[9,8,7],[9,8],[4,7]]
        result = hw1.ascending_pairs(input)
        expected = [[9,8,7],[8,9],[4,7]]
        self.assertEqual(expected,result)

    # Part 4
    def test_add_prices1(self):
        money1 = data.Price(4,50)
        money2 = data.Price(5,50)
        result = hw1.add_prices(money1,money2)
        expected = 10.00
        self.assertEqual(expected,result)

    def test_add_prices2(self):
        money1 = data.Price(6, 40)
        money2 = data.Price(8, 30)
        result = hw1.add_prices(money1, money2)
        expected = 84
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area1(self):
        point1 = data.Point(3,4)
        point2 = data.Point(2,8)
        myRect = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(myRect)
        expected = 4
        self.assertEqual(expected,result)

    def test_rectangle_area2(self):
        point1 = data.Point(6,5)
        point2 = data.Point(7,2)
        myRect = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(myRect)
        expected = 3
        self.assertEqual(expected,result)



    # Part 6
    def test_books_by_author1(self):
        book1 = data.Book(["Dr.Seuss","another author"],"Oh the places you'll go")
        book2 = data.Book(["E.B white","different author"],"Stuart Little")
        result = hw1.books_by_author("Dr.Seuss",[book1,book2])
        expected = ["Oh the places you'll go"]
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        book1 = data.Book(["jk rowling","another author"],"Harry Potter")
        book2 = data.Book(["Charles dickens","other author"],"Bleak House")
        result = hw1.books_by_author("jk rowling",[book1,book2])
        expected = ["Harry Potter"]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound1(self):
        point1 = data.Point(4,9)
        point2 = data.Point(8,5)
        startingRect = data.Rectangle(point1,point2)
        result = hw1.circle_bound(startingRect)
        expected = data.Circle((6.0,7.0),(math.sqrt(32)))
        self.assertEqual(expected,result)

    def test_circle_bound2(self):
        point1 = data.Point(2,10)
        point2 = data.Point(10,2)
        startingRect = data.Rectangle(point1,point2)
        result = hw1.circle_bound(startingRect)
        expected = data.Circle((6.0,6.0),(math.sqrt(128)))
        self.assertEqual(expected,result)

    # Part 8
    def test_below_pay_average1(self):
        emp1 = data.Employee("john",50)
        emp2 = data.Employee("sia", 30)
        emp3 = data.Employee("laasya", 10)
        emp4 = data.Employee("Harshi", 10)
        employees = [emp1,emp2,emp3,emp4]
        result = hw1.below_pay_average(employees)
        expected = ["laasya","Harshi"]

    def test_below_pay_average2(self):
        emp1 = data.Employee("john",30)
        emp2 = data.Employee("sia", 15)
        emp3 = data.Employee("laasya", 40)
        emp4 = data.Employee("Harshi", 25)
        employees = [emp1,emp2,emp3,emp4]
        result = hw1.below_pay_average(employees)
        expected = ["Harshi","sia"]



if __name__ == '__main__':
    unittest.main()
