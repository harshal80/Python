x = 10  # global variable


def my_function():
    global x
    x = 4
    y = 5  # Local variable
    print(y)


my_function()
print(x)
print(
    y
)  # Theis will cause an error because y is a local vaiable and is not accessible outside of the functin
