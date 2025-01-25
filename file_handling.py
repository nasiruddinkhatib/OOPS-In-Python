# We use here read(r)  mode
# a = open("Myfile.txt","r")
# c = a.readlines() #readline will read the first row written in the txt file if we again call readline it will read the next line
# print(c)
# a.close()   # this will close the file that we have opened it is very important to close the file


# We use here write Mode
# a = open("Myfile.txt","w") # this will open the file in the write mode
# c = a.write("Hii Have a nice Day\nWhat is the plan tomorrow\n yes going to play cricket ")  # it will write the data in the created txt file
# print(c)
# a.close()

# try and except part of file handling this is use to check whether the file exist or not
# try:
#     a = open("Myfile.txt","r") # this will check that file is exist or not if file name is not exist then it will throw an error message
#     c = a.read()
#     print(c)
#     a.close()
# except:                       #this is an exception it will print the error message
#     print("file not exist")


#New File now we wil create a new file using python code by using (x) keyword this will create a new file
# file = open("hello.txt","x")
# file.read()
# file.close()
#
# #New File to read(r) this created file we have write this code
# file = open("hello.txt","r")
# content = file.read()
# print(content)
# file.close()

#New file Append(a) function we use and added some data in file
# file = open("hello.txt","a")     #append function will add data which we written and many time we run it will print that data again and again
# d = file.write("\nTata Motors is a good")
# print(d)
# file.close()

# import os
# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")
#     print("File Successfully Deleted")
# else:
#     print("File does not exist")


