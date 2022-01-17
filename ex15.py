from sys import argv   # imports argv from sys

script, filename = argv  # using argv to get the file name

txt = open(filename)  # giving txt variable value of opened file


print(f"where is your file {filename}") # printing the filename in the text
print(txt.read()) # printing the content of the file using .read function

print("Type the filename again:")  # printing a message to type the filename again
file_again = input("> ") # with the input we are assigning value of input to file_again variable

txt_again = open(file_again) # to the txt_again variable assigning the opening file function

print(txt_again.read()) # reading the opened file and printing it out



'''option on;ly using input'''
filename = input("enter the filename you have created: ")

txt = open(filename)  # giving txt variable value of opened file

print(f"where is your file {filename}") # printing the filename in the text
print(txt.read()) # printing the content of the file using .read function

print("Type the filename again:")  # printing a message to type the filename again
file_again = input("> ") # with the input we are assigning value of input to file_again variable

txt_again = open(file_again) # to the txt_again variable assigning the opening file function

print(txt_again.read()) # reading the opened file and printing it out

