"""
    The key function for working with files in Python is the open() function.
    The open() function takes two parameters; filename, and mode.

    There are four different methods (modes) for opening a file:
        "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        "a" - Append - Opens a file for appending, creates the file if it does not exist
        "w" - Write - Opens a file for writing, creates the file if it does not exist
        "x" - Create - Creates the specified file, returns an error if the file exis

    In addition you can specify if the file should be handled as binary or text mode:
        "t" - Text - Default value. Text mode
        "b" - Binary - Binary mode (e.g. images)

"""

#opens a file called demofile.txt the mode is r meaning that if the file doesn't exist it will not create and an error will be thrown. t means that the file will be handled in text more an dnot binary.
#Because "r" for read, and "t" for text are the default values, you do not really need to specify them.
f = open("C:\\Users\\carlos.alvarez\\Documents\\projects\\py\\python\\file_handling\\demofile.txt", "rt")


#The open() function returns a file object, which has a read() method for reading the content of the file:
print(f.read())


#Read part of files: return 5 first characters of the file
print(f.read(5))


#Read Lines with readline() method.  By calling readline() two times, you can read the two first lines:
print(f.readline())
print(f.readline())

#Looping through the file. By looping trough the lines of the file, you can read the whole file, line by line.
for line in f:
    print(line)

#It is always good practice to close the file when you are done with it.
# You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
f.close()