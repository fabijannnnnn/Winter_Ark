import os

print(os.path.exists('number.txt'))  # Should return True

list1 = []
list2 = []

with open('number.txt', 'r') as text_file:
    for line in text_file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()
print(list1)
print(list2)

index = 0
result = 0
for num1, num2 in zip(list1, list2):
    distance = abs(list1[index] - list2[index])
    result += distance
    print(distance)
    index += 1

print(result)