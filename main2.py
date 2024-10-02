new_file = open('New file.txt', 'x')
new_file.close()

import os
print("checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the folder has been deleted recoery options are to restore the file data...")

    my_file = open("my_file.txt", "w")
    my_file.write("Hi")
    my_file.close()

    os.remove("Codingal.txt")

    os.rmdir('Operations on a File - Part 2 - Copy')