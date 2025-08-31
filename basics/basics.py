
b=5
print("{} {}".format("value is",b))

values = [1,2,3,"Azhar",4]
print(values[-1])
print(values[1:3])
values.insert(3,"test")
print(values)
values.append("end")
print(values)
values[3] = "TEST"
print(values)
del values[1]
print(values)

a={1: "Test", 2: "Name", "k": 9}
print(a)

dict = {}
dict["firstname"] = "Azhar"
dict["lastname"] = "Mohd"
dict["gender"] = "Male"
print(dict)


greeting = "Good Morning"
if greeting == "Good Morning":
    print("condition matches")
else:
    print("condition do not match")
print("out of If else")


abc = [2,3,5,7,9]
for i in abc:
    print(i*2)

# 1+2+3+4+5
summation = 0
#xyz = [1,2,3,4,5]
for j in range(1,6):
    summation = summation+j
print(summation)

print("***************")

# 1+2+3+4+5
summation = 0
#xyz = [1,2,3,4,5]
for k in range(1,10,5):
    print(k)

print("*******************")

y=4
while y>1:
    if y !=3:
        print(y)
    y = y-1

print(y)


def GreetMe(name):
    print("Good Morning"+name)

GreetMe("Azhar")

def add(a,b):
    #print(a+b)
    return a+b

print(add(2,3))

print("**********************")

str = "azharulla.mohammed1701@gmail.com"
print(str[0])
print(str[0:5])

print(str.split(".")[1])

print("*************************")

#file = open('text.txt')
#print(file.read())
#print(file.read(7))
#line = file.readline()
#while line !="":
    #print(line)
    #line = file.readline()
#for line in file.readlines():
    #print(line)
#file.close()

with open('text.txt', 'r') as file:
    content = file.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

