from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import colorama

N = 4  # Replace with your variant number

# Create objects
rect = Rectangle(N, N, "blue")
circle = Circle(N, "green")
square = Square(N, "red")

# Print information
print(rect)
print(circle)
print(square)

# Use an external package (colorama)
print(colorama.Fore.GREEN + "Hello, World!" + colorama.Style.RESET_ALL)
