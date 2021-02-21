import BubbleSort as b

length = int(input("How many Numbers do you want to sort "))
a = []
for i in range(length):
    inputs = int(input())
    a.append(inputs)

x = b.bubble_sort(a)
print(x)