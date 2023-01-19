# Readline Method -->
f = open('1001. First.py', 'r')
while True:
    line = f.readline()  # Reads a single line from the file
    if not line:
        break
    print(line)

# Writelines Method -->
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)  # Writes a sequence of strings
f.close()

# Seek Method -->
with open('file.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)  # Prints those 5 bytes

# Tell Method -->
with open('file.txt', 'r') as f:
    # Read the first 10 bytes
    data = f.read(10)

    # Save the current position
    current_position = f.tell()
    print(current_position)  # 10

    # Seek to the saved position
    f.seek(current_position)

# Truncate Method -->
with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)  # Truncate or cut the file to a specific size

with open('sample.txt', 'r') as f:
    print(f.read())  # Hello