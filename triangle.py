import sys
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


class Triangle:
    def __init__(self, a, b, c):
        self.a_crds = a
        self.b_crds = b
        self.c_crds = c
        self.a = sqrt((b.x - c.x) ** 2 + (b.y - c.y) ** 2)
        self.b = sqrt((a.x - c.x) ** 2 + (a.y - c.y) ** 2)
        self.c = sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

    def __str__(self):
        return f"{self.a_crds.x} {self.a_crds.y} {self.b_crds.x} {self.b_crds.y} {self.c_crds.x} {self.c_crds.y}"

    def is_triangle(self):
        return (self.a < self.b + self.c) and (self.b < self.c + self.a) and (self.c < self.a + self.b)

    def is_rb(self):
        if self.is_triangle():
            return (self.a == self.b) or (self.b == self.c) or (self.c == self.a)
        return False

    def square(self):
        if self.is_triangle() and self.is_rb():
            p = (self.a + self.b + self.c) / 2
            s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            return round(s, 3)
        return -1


class TaskSolver:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.raw_data = list()
        self.data = list()
        self.mx_square = 0
        self.res_triangle = None

    def read_data(self):
        with open(self.src) as f:
            self.raw_data = list(map(lambda x: x.strip('\n').split(), f.readlines()))
        return self.raw_data

    def parse_data(self):
        k = len(self.raw_data)
        for i in range(k):
            is_num_row = True
            if len(self.raw_data[i]) == 6:
                for j in range(6):
                    try:
                        self.raw_data[i][j] = float(self.raw_data[i][j])
                    except ValueError:
                        is_num_row = False
                if is_num_row:
                    self.data.append(self.raw_data[i])
        return self.data

    def find_largest_triangle(self):
        for line in self.data:
            triangle = Triangle(Point(line[0], line[1]),
                                Point(line[2], line[3]),
                                Point(line[4], line[5]))
            if triangle.square() > self.mx_square:
                self.mx_square = triangle.square()
                self.res_triangle = triangle
        return self.mx_square

    def write_data(self):
        with open(self.dst, 'w') as f:
            if self.mx_square != 0:
                f.write(str(self.res_triangle))
                return str(self.res_triangle)
            return 0


def main(src, dst):
    task_solver = TaskSolver(src, dst)
    task_solver.read_data()
    task_solver.parse_data()
    task_solver.find_largest_triangle()
    print(task_solver.res_triangle.square())
    task_solver.write_data()


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2])

# triangle.py in.txt out.txt