import math


class SquareGenerator:
    def generate_squares(start, end):
        squares = [x ** 2 for x in range(start, end)]
        return squares

    def calculate_square_roots(self, numbers):
        sq = [math.sqrt(num) for num in numbers]
        return sq


a = SquareGenerator()
res = a.generate_squares(1, 11)
sq = a.calculate_square_roots(res)
print(res)
print(sq)
