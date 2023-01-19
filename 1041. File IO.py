f = open('1001. First.py', 'r') # To open a File 
# r = read
# w = write
# a = append
# x = create
# rt = read as text
# rb = read as binary

text = f.read() # Read from the file
print(text)
f.close() # Closing a file

with open('1001. First.py', 'r') as f:
    text = f.read() # Read from the file
    print(text)
    # does not requires to close the file in "with open"