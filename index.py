
file = open("file.txt", "r")
print(file.read())

writeFile = open("writeFile.txt", "w")
writeFile.write("this is the new text");

try:
    file = open("readme.txt", "r")
    print(file.read())
except FileNotFoundError:
    print('file not found')
finally:
    print('Thank for patronizing us')
