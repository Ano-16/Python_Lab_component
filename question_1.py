def reconstruct_path(ordered_part, jumbled_part):
    # The correct order of all Landmarks
    correct_order = ['Start', 'Clearing', 'River', 'Village', 'Cave']
    
    # Initialize the final path with the orderd list
    final_path = []
    
    # Pointer to track the position in the ordered list
    ordered_index = 0
    
    # Go through the correct order list
    for landmark in correct_order:
        # If the landmark is in the ordered_part and hasn't been added yet
        if ordered_index < len(ordered_part) and ordered_part[ordered_index] == landmark:
            final_path.append(landmark)
            ordered_index += 1
        # Otherwise, it should be in the jumbled part
        elif landmark in jumbled_part:
            final_path.append(landmark)
    
    return final_path

# Given Example
ordered_part = ['Start', 'River']
jumbled_part = ['Clearing', 'Village', 'Cave']
result = reconstruct_path(ordered_part, jumbled_part)
print(result)


