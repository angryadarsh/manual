'''
# Write a file in python 
#with open('WriteAstrix.txt', 'a') as f:
    #f.write('\n[2]\n')
    #f.write('\tName :\n')
    #f.write('\tEmp_id :\n')
    #f.write('\tRole :\n')
    #f.write('\tcontact :\n')

    
#find specific word in txt file 
file = open("WriteAstrix.txt")
print(file.read())
search_word = input("enter a word you want to search in file: ")
if(search_word in file.read()):
    print("word found")
else:
    print("word not found")
with open('example.txt') as f:
    if 'blabla' in f.read():
        print("true")
        
#find specific word in txt file 
with open('WriteAstrix.txt') as f:
    search_word = input("enter a word you want to search in file: ")
    if search_word in f.read():
        print("true")
        
    else:
        print("false")'''

f = open('WriteAstrix.txt')
content = f.readlines()
print(content[9])
