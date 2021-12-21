"""
Write a Python program to accept a filename from the user and print the extension of that.

Sample filename: abc.java

"""

filename = input("Please enter the filename: ")
file_extension = filename.split(".")
print("The file extension: " + repr(file_extension[-1]))

