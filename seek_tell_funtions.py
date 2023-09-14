# with open("myfile.txt", "r") as f:
#     print(type(f))
#     # move to the 10th byte in the file
#     f.seek(10)

#     # read the next 5 byte
#     print(f.tell())
#     data = f.read(5)
#     print(data)

# tuncate()
with open("myfile.txt", "w") as f:
    f.write("Hello world!")
    f.truncate(5)

with open("myfile.txt", "r") as f:
    print(f.read())
