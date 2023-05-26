list(filter(lambda x : x % 2 == 1, range(1, 20)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

[x ** 2 for x in range (1, 11) if  x % 2 == 1]
[1, 9, 25, 49, 81]

[x for x in [3, 4, 5, 6, 7] if x > 5]
[6, 7]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
[6, 7]
