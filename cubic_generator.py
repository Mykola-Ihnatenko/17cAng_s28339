from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end <= start:
            raise ValueError("End of the range must be greater than the start.")

        cubes = [x ** 3 for x in range(start, end)]
        return cubes
