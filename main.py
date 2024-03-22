

def generate_squares(start, end):
    squares = [x**2 for x in range(start, end)]
    return squares

result = generate_squares(1, 11)
print(result)