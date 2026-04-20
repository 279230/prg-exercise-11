my_list = [3, 8, 1, 2, 32]
my_list.sort()
print(my_list)   # [1, 2, 3, 8, 32]

my_list = [3, 8, 1, 2, 32]
new_list = sorted(my_list)
print(my_list)   # [3, 8, 1, 2, 32]   ← beze změny
print(new_list)  # [1, 2, 3, 8, 32]

my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list, reverse=True)
print(my_list)   # [32, 8, 3, 2, 1]

list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
print(list_of_words)   # ['MOO', 'woof', 'meeeoow', 'BZZZZZZ']

list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter

rectangles = [
    Rectangle(3, 5),
    Rectangle(10, 20),
    Rectangle(1, 1),
    Rectangle(7, 2),
    Rectangle(4, 8),
]

for rect in rectangles:
    print(rect.area())


