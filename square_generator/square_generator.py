import math
class SquareGenerator:
    def generate_squares(start, end):
        if end <= start:
            raise ValueError("End of the range must be greater than the start.")

        squares = [x ** 2 for x in range(start, end)]
        return squares

    def calculate_square_roots(self, numbers):
        sq = [math.sqrt(num) for num in numbers]
        return sq