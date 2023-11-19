even_numbers = [2, 4, 6, 8, 2, 4, 10]
odd_numbers = [1, 3, 5, 7, 3, 9]
combined_list = even_numbers + odd_numbers
number_occurrences = {}
for number in combined_list:
    if number in number_occurrences:
        number_occurrences[number] += 1
    else:
        number_occurrences[number] = 1

print("Combined List:", combined_list)
print("Number Occurrences:")
for number, count in number_occurrences.items():
    print(f"{number}: {count}")
