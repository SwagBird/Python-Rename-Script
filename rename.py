"""
Example of some simple python script that is used to rename the file in a directory. Learned from Corey Schafer 's Python Tutorial
at youtube. An example changes done to file is as follow:

Before : (001) - Hip Hop Jazz - Our Times.xxx
After  :  001 - Our Times - Hip Hop Jazz.xxx


"""

# Gonna use OS module to rename and change the dir.
import os

# Change our the working directory to our files's directory

f_dir = raw_input("Please enter the path of the files you want to rename")
f_dir = os.chdir("f_dir")

# listing the item in that dir
for files in f_dir:
  
  # splitext() will separate the file extension from the file name, thus f_title (files title) and f_ext (files extension)
  f_title, f_ext = listdir(files).splitext()
  
  # Same as above, split the file name in 3 section.
  f_number, f_album, f_name = " - ".split(f_title)
  
  # Remove the "()" bracket
  f_number = f_number.strip("()")
  
  # Change the arrange here to the style we want
  os.rename(files) = "{} - {} - {}{}".format(f_number, f_name, f_album, f_ext)
  
  
  





