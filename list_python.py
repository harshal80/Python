marks = [3,5,6,"Harshal",True,6,7,2,32,45,23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3])#Negative index
#print(marks[len(marks)-3])#Positive index

if "6" in marks:
    print("Yes")
else:
    print("No")

#Same thing apples for stings as well!
if "Ha" in "Harshal": 
    print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst=[i*i for i in range (10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)