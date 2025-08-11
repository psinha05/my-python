#with open('user-info.txt', 'a') as file:
 #   file.write('Few user Information:\n')
  #  file.write('Alex\n')
   # file.write('Harsh\n')
    #file.write('Riya\n')
    #file.write('Maxx\n')
    #file.write('David\n')


with open('user-info.txt', 'r') as file:
    # content = file.read()   for read the file
     info = file.readlines()   # for reading the contents line by line
    # print(info)  # this info stored in List
for details in info:
    # print(details.rstrip())     # use rstrip for remove the unwanted spaces between the text stored in the file
      print(f'Welcome  {details.rstrip()}')
file.close()




# handling the file errors
try:
    with open('non_exist.text', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("sorry !, file not found")
except Exception as e:
    print(f"An error has occured : {e}")



# use 't' as text mode (default mode)
# use 'w' for write in the file.
# use 'a' append for append the contents in the file
# use 'r' for the read of the file, use file.read()
# use 'x' creates a new file but throws an error if the file is already exists
# use 'b': binary mode 9'rb' of 'wb')

# red(): Reads the entire content of the file (file.read())
# readline(): Reads one line at a time  (file.readline())
# readlines(): Reads all lines and returns a list of strings  (file.readlines())

# write(): Writes a string to the file (file.write("Hello, world !"))
# writelines(): Writes a list of strings to the file.
# close a file : file.close()

# with statement : Python provides a with statement which automatically handles file opening and closing.
