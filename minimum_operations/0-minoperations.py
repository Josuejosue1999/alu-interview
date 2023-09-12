#!/usr/bin/python3
#Minimum Operations

def min_operations_to_generate_h(n):
    clipboard = 0  # Initialize clipboard to 0 H's
    operations = 0  # Initialize the number of operations to 0

    while clipboard < n:
        if n % clipboard == 0:
            clipboard = clipboard * 2  # Double the clipboard size
            operations += 1
        else:
            clipboard += clipboard  # Copy all
            operations += 1

    return operations

n = 9
result = min_operations_to_generate_h(n)
print("Number of operations:", result)
