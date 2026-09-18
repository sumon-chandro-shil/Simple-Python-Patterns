n =  int(input("Enter a number: "))
count = 1
for i in range(1, n+1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

"""
Enter a number: 5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""