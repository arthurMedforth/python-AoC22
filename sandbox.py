def split_range(original_range):
    start, end = original_range
    midpoint = (start + end) // 2

    # Split the range into two smaller ranges
    first_half = list((start, midpoint))
    second_half = list((midpoint + 1, end))

    return first_half, second_half

# Example usage:
original_range = [1000, 1000]
smaller_ranges = split_range(original_range)

print("Original Range:", original_range)
print("Smaller Ranges:", list(smaller_ranges))