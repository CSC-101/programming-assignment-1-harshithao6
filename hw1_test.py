import data
import hw1
import unittest


# Write your test cases for each part below.
# class TestCases(unittest.TestCase):
# Part 1
# def test_first_element_1(self):
#   input = [[1, 2], [3, 4]]
#  result = lab4.first_element(input)
# expected = [1, 3]
# self.assertEqual(expected, result)

class TestCases(unittest.TestCase):

    # TODO: look up test coverage :)
    # Part 1
    def test_vowel_count(self):
        input = "hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists(self):
        input = [[3,5,6],[4,3],[3,2]]
        result = hw1.short_lists(input)
        expected = [[4,3],[3,2]]
        self.assertEqual(expected,result)

    # Part 3
    def test_ascending_pairs(self):
        input = [[4,6,7],[4,3],[2,7]]
        result = hw1.ascending_pairs(input)
        expected = [[4,6,7],[3,4],[2,7]]
        self.assertEqual(expected,result)

    # Part 4
    def test_add_prices(self):
        money1 = data.Price(4,50)
        money2 = data.Price(5,50)
        result = hw1.add_prices(money1,money2)
        expected = 10.00
        self.assertEqual(expected,result)

    # Part 5
    def test_rectangle_area(self):
        point1 = data.Point(3,4)
        point2 = data.Point(2,8)
        myRect = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(myRect)
        expected = 4
        self.assertEqual(expected,result)



    # Part 6
    def test_books_by_author(self):
        book1 = data.Book(["Dr.Seuss","another author"],"Oh the places you'll go")
        book2 = data.Book(["E.B white","different author"],"Stuart Little")
        #input = "Dr.Seuss",[("Dr.Seuss","Oh the places you'll go"),["E.B white","Stuart Little"]]
        result = hw1.books_by_author("Dr.Seuss",[book1,book2])
        expected = ["Oh the places you'll go"]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound(self):
        point1 = data.Point(4,9)
        point2 = data.Point(8,5)
        startingRect = data.Rectangle(point1,point2)
        result = hw1.circle_bound(startingRect)
        expected = data.Circle((6.0,7.0),2.0)
        self.assertEqual(expected,result)

    # Part 8





if __name__ == '__main__':
    unittest.main()
