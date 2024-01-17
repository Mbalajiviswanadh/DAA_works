from itertools import product

def generate_strings(characters, k):
    all_combinations = product(characters, repeat=k)
    return (
        [''.join(combination) for combination in all_combinations]
            )

characters_input = input("Enter characters separated by spaces: ")
characters = characters_input.split()
k = int(input("Enter the value of k: "))

result_strings = generate_strings(characters, k)
for string in result_strings:
    print(string)
