# %%
##
class Point:
    pass  # place holder


p1 = Point()
p2 = Point()
print(p1)
print(p1, p2)
print(type(p1))
print(type(p2))


# %%
##
class Point:
    def __init__(self):  # bez ustawiania parametrów na wejściu
        self.x = 0
        self.y = 0


p1 = Point()  # powstaje punkt o współrzędnych domyślnych
p2 = Point()
print(p1.x, p1.y)
print(p2.x, p2.y)


# %%
##
class Point:
    def __init__(self, x=0, y=0):  # można też ustawić wartości domyślne na wejściu
        self.x = x
        self.y = y


p1 = Point(2, 3)
p2 = Point()
print(p1.x, p1.y)
print(p2.x, p2.y)


# %%
##
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to_new_cords(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(2, 3)
print(p1.x, p1.y)
# # nowe przypisanie zmiennych, można zastąpić metodą w klasie
# p1.x = 9
# p1.y = 12
# print(p1.x, p1.y)
p1.move_to_new_cords(9, 12)
print(p1.x, p1.y)


# %%
##
class Point:
    points_counter = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points_counter += 1

    def move_to_new_cords(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(2, 3)
p2 = Point(9, 7)
print(Point.points_counter, p2.points_counter)


# %%
##
class Widget:
    def __init__(self, label, shape):
        self.label = label
        self.shape = shape


class Button(Widget):
    def __init__(self, label, shape, size):
        super().__init__(label, shape)
        self.size = size

    def handle_click(self):
        return 'Klik!'


b = Button('my button', 'rectangle', 'large')
print(b.label, b.shape, b.size)
print(b.handle_click())


# %%
##
class New:
    def __init__(self):
        pass
