n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i%2, end="")
    print()

"""
n = 5
Output:
11111
00000
11111
00000
11111
"""