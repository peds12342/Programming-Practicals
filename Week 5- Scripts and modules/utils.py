def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        total += float(n)
    return total / len(values)

# Initialization statement
print("Welcome, utils module has been imported and initialized!")