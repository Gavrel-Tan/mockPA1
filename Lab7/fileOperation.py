# write
file = open("test.txt", "w")
file.write("new text")
# append
file = open("test.txt", "a")
file.write("new text2")
# read
file = open("test.txt", "a")
file.write("new text2")

file = open("test.txt", "r")
fileText = file.read()
print(fileText)
file.close()

with open("test.txt") as file:
    print(file.read())
