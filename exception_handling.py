# a = int(input("Enter the number: "))
# print(f"Multiplication table of {a} is : ")
# try:
#     for i in range(1, 11):
#         print(f"{a}X{i}={a*i}")
# except:
#     print("Invalid Input!")

# print("some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
