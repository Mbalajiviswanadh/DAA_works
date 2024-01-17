def generate_permutations(elements, current_permutation=[]):
    permutations = []

    if not elements:
        # If there are no elements left, return the current permutation
        return [current_permutation]
    else:
        for i in range(len(elements)):
            # Choose the i-th element as the next element in the permutation
            next_element = elements[i]

            # Exclude the chosen element from the remaining elements
            remaining_elements = elements[:i] + elements[i + 1:]

            # Recursively generate permutations with the chosen element
            permutations += generate_permutations(remaining_elements, current_permutation + [next_element])

    return permutations

user_input = input("Enter elements separated by spaces: ")
elements = user_input.split()

permutations = generate_permutations(elements)

for p in permutations:
    print(" ".join(p))
10