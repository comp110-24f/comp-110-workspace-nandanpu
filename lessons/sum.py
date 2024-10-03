def sum(num1: int, num2: int) -> int: 
    """Add two numbers together"""
    return num1 + num2

print(sum(1, 3))

import numpy as np

# Define the sample points
x = np.linspace(0, 1, 11)

# Define the function sin(x)
f_x = np.sin(x)

# Define the polynomial approximation p(x) = x - x^3/6 + x^5/120
p_x = x - (x**3)/6 + (x**5)/120

# Calculate the error as the norm of the difference
error = np.linalg.norm(f_x - p_x)

print(f"Approximation error: {error:.4e}")