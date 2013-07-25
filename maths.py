# Import the maths
import math
import decimal

# Set it to be really accurate.
decimal.getcontext().prec = 1000

# Set my deltas to be really accurate
k = decimal.Decimal("0.0000000001")
delta = decimal.Decimal("0.0000000001")

# What are we making a start as
a = decimal.Decimal("5.0")
# Calculating the gradient with this
m = abs(((a**k)-1)/k)

# b is the value I am subtracting or adding for my binary search algorithm
b = decimal.Decimal("2.5")

# While the gradient isn't equal to 1 + my delta (delta is how accurate it is
while m != 1 + delta:
    # if the a value is too big, make it a bit smaller
    if m > 1:
        a = a - b
        
    # if the a value is too small, make it a bit larger
    elif m < 1:
        a = a + b
        
    # Make b smaller
    b = b / 2
    
    # Recalculate the gradient
    m = abs(((a**k-1)/k))
    # Print the working total
    print a

# Print it one last time when we are done!
print a