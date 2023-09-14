# # map
# def cube(x):
#     return x * x * x


# print(cube(2))

# l = [3, 5, 5, 3, 3, 5, 6, 3]
# newl = []
# # for item in l:
# #     newl.append(cube(item))

# # newl = list(map(cube, l))
# # print(newl)


# # filter
# def fileter_fun(a):
#     return a > 4


# newnewl = list(filter(fileter_fun, l))

# print(newnewl)


# reduce

from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5]


# Calculate the sum of the number using the reduce function
def mysum(x, y):
    return x + y


sum = reduce(mysum, numbers)

# print the sum
print(sum)
