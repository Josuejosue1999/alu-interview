#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a Pascal's triangle as a list of lists.
    
    Args:
        n (int): Number of rows to generate.

    Returns:
        List of lists representing Pascal's triangle.
    """

    if n <= 0:
        # Return an empty list for n <= 0
        return []
    
    pascal = [[1]]
    if n == 1:
        return pascal

    for i in range(1, n):
        left = -1
        right = 0
        in_pas = []
        for j in range(i + 1):
            num = 0
            if left > -1:
                num += pascal[i - 1][left]
            if right < i:
                num += pascal[i - 1][right]
            left += 1
            right += 1
            in_pas.append(num)
        pascal.append(in_pas)

    return pascal
