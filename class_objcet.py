class person:
    name = "harshal"
    occupation = "sofware developer"
    netwrorth = 1000

    def info(self):
        print(f"{self.name}is a {self.occupation}")


a = person()
a.name = "suresh"
a.occupation = "Accountant"
# print(a.name, a.occupation)
a.info()
