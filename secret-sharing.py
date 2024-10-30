import json

def decode_value(value, base):
    """Decode a number from a given base to decimal."""
    return int(value, base)

def lagrange_interpolation(points):
    """Perform Lagrange interpolation to find the constant term of the polynomial."""
    n = len(points)
    c = 0  # This will hold the constant term

    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                term *= (0 - xj) / (xi - xj)
        c += term

    return c

def main():
    # Load the JSON input from a file (for example: 'input.json')
    with open('input.json') as f:
        data = json.load(f)

    # Read n and k
    n = data["keys"]["n"]
    k = data["keys"]["k"]

    # Prepare points for interpolation
    points = []
    for key in data.keys():
        if key not in ["keys"]:
            base = int(data[key]["base"])
            value = data[key]["value"]
            decoded_value = decode_value(value, base)
            points.append((int(key), decoded_value))

    # We can use only the first k points for interpolation
    points = points[:k]

    # Find the constant term c using Lagrange interpolation
    c = lagrange_interpolation(points)

    # Output the result
    print(f"The constant term (c) of the polynomial is: {c}")
if __name__ == "__main__":
    main()