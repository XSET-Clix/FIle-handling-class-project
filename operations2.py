file = open("fortnite.txt")
#print(file.read())
print(file.readline())
file.close()
#remove lines starting with Fortnite

file1 = open('fortnite.txt', 'r')

file2 = open('fortniteupdated.txt', 'w')


for line in file1.readlines():
    if not (line.startswith('Fortnite')):
        print(line)
        
        
        file2.write(line)
        
file2.close()
file1.close()