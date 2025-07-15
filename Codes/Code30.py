# Write a Python program to sort a list of integers in ascending order using nested loops (without using built-in sort() or sorted() functions).

list1 = [4, 2, 3, -1, -2, 0, 1] # Given list of integers

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):

        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)