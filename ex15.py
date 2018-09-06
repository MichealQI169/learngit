from sys import argv
#import module
script,filename = argv
#argument variable
txt = open(filename)
#open file you build
print (f"Here's your file {filename}:")
print (txt.read())
#print you flie contect
print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
#do it again
