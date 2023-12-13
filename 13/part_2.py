import sys
import numpy as np

data = sys.stdin.read().splitlines()
chunks = [data.split("\n") for data in "\n".join(data).split("\n\n")]

sol = 0
for chunk in chunks:
    chunk_array = np.array([list(row) for row in chunk])

    # Check for vertical reflection
    # For each possible split, check if the right and left are reflections of each other
    for split in range(1, len(chunk_array[0])):
        left = chunk_array[:, :split]
        right = chunk_array[:, split:]
        max_len = min(len(left[0]), len(right[0]))
        left = left[:, split-max_len:]
        right = right[:, :max_len]

        # Check if left is a smudged reflection of right
        right_flipped = np.flip(right, axis=1)
        num_diff = np.sum(left != right_flipped)

        if num_diff == 1:
            sol += split
            break
    
    # Check for horizontal reflection
    # For each possible split, check if the top and bottom are reflections of each other
    for split in range(1, len(chunk_array)):
        top = chunk_array[:split]
        bottom = chunk_array[split:]
        max_len = min(len(top), len(bottom))
        top = top[split-max_len:]
        bottom = bottom[:max_len]

        # Check if top is a smudged reflection of bottom
        bottom_flipped = np.flip(bottom, axis=0)
        num_diff = np.sum(top != bottom_flipped)
        
        if num_diff == 1:
            sol += split * 100
            break
    
print(sol)