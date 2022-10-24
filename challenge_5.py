# opening the file demo.txt
file=open("demo.txt", 'w')
file.write("Welcome to python programming. ")
file.close()
# reading the file
file=open("demo.txt", 'r')
content= file.read()
# displaying the content
print(content)
file.close()
# adding additional text to the file
file=open("demo.txt",'a')
file.write("Hai, I am Anjali Ashok")
file=open("demo.txt",'r')
content=file.read()
print(content)
file.close()



