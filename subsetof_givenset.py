def isSubsetSum(set, n, target_sum):
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if set[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set[i - 1]]

    subset = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            subset.append(set[i - 1])
            j -= set[i - 1]
        i -= 1

    return subset[::-1]

# Take user input for the set of non-negative integers
user_input_set = input("Enter the set of non-negative integers separated by spaces: ")
set = list(map(int, user_input_set.split()))

# Take user input for the target sum
target_sum = int(input("Enter the target sum: "))

# Find and print the subset with the given target sum
result_subset = isSubsetSum(set, len(set), target_sum)

if result_subset:
    print("Subset with sum", target_sum, "found:", result_subset)
else:
    print("No subset with sum", target_sum, "found.")
