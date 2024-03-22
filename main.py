from square_generator.square_generator import SquareGenerator
from cubic_generator import CubicGenerator

a = SquareGenerator()
res = a.generate_squares(1, 11)
sq = a.calculate_square_roots(res)
print(res)
print(sq)
b = CubicGenerator()
c = b.generate_cubes(1, 11)
print(c)
#c = b.generate_squares(11, 1)
#print(c)
