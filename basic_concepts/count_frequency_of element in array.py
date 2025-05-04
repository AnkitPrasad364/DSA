def count_frequencies(arr):
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    return freq_dict

# Taking input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Counting frequencies
frequencies = count_frequencies(arr)

# Printing the result
for key, value in frequencies.items():
    print(f"Element {key} appears {value} times")