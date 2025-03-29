number = [1, 2, 2, 3, 4, 3, 91, 4, 3, 9, 4, 5, 2, 1, 9]
number_copy = number.copy()
for i in number_copy:
  # print(i)
  duplicate_numbers = number.count(i)
  if duplicate_numbers > 1:
    number.remove(i)

print(number)