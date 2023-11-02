def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        total += float(n)
    return total / len(values)

if __name__ == "__main__":
 
    count = len(sys.argv)
    if count <= 1:
        print("No arguments were provided.")
    else:
        args = [float(arg) for arg in sys.argv[1:]]  # Convert command-line arguments to floats
        avg = average(args)
        print("Average is", avg)
else:
    print("Welcome, utils module has been imported and initialized!")
