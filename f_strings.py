letter="Hey my name is {1} and I am from {0}"
country="India"
name="Harshal"

print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"we use f-string  like this: Hey my name is {{name}}and I from{{country}}")
price=49.09999
txt=f"for only {prince:.2f}dollars"
print(txt)
print(txt.format())
print(type(f"{2*30}"))