# To delete a file, you must import the OS module, and run its os.remove() function:
import os

# Remove the file "demofile.txt":
os.remove("demofile.txt")

#   check if the file exists before removing it. To avoid getting an error, you might want to check if the file exists before you try to delete it:
# Check if file exists, then delete it:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



#To delete an entire folder, use the os.rmdir() method: You can only remove empty folders.
os.rmdir("myfolder")
