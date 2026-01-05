def minimum_distance(X, Y, Z):
    # Case 1: Construction is NOT between home and office
    if not ((0 < Y < X) or (X < Y < 0)):
        return abs(X)

    # Case 2: Construction is between home and office
    # Check if contractor is reachable
    if (0 < Y < Z) or (Z < Y < 0):
        return -1

    # Calculate total distance
    distance = abs(Z)              # Home -> Contractor
    distance += abs(Z - Y)          # Contractor -> Construction
    distance += abs(X - Y)          # Construction -> Office

    return distance
