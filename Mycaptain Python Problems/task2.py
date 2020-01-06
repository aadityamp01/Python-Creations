# Python program to accept a filename from the user and print the extension of that file

filename = input("Enter the Filename:: ")
f_extension = filename.split(".")
print ("The extension of the file is:: " + repr(f_extension[-1]))
