file=open('file.txt','r')
print(file.read())
file.close()

file=open('file.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close

file=open('file.txt','a')
file.write("Hi!I am Penguin and I am 1yr old")
file.close