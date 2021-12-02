try:
    f = open("myContact.txt",encoding = 'utf-8')
    print(f.readlines())
except:
    print("Error")
finally:
 f = open("myContact.txt")
print(f)
f = open("myContact.txt", 'w')
#f = open("README.md", 'r+b')

f = open("myContact.txt",mode='w',encoding = 'utf-8')
print(f)
f.close()
