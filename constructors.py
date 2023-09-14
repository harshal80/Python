class perosn:
    def __init__(self, n, o):
        print("hey I am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = perosn("harshal", "Developer")
b = perosn("Divesh", "HR")
a.info()
b.info()
# a = perosn()
# # print(a.name)
# a.name = "divesh"
# a.occ = "HR"
# a.info()
