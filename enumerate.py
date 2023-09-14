marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(marks)
#     if index == 3:
#         print("Harshal,awesome!")
#     index += 1

for index, mark in enumerate(marks, start=1):
    print(index == 3)
    if index == 3:
        print("Harshal,awesome!")
