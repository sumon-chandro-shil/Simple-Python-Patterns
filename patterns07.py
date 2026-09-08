n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(i, end="")
    print()

"""
n = 5
Output:
55555
44444
33333
22222
11111
"""