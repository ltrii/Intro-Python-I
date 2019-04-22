"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# foo = open('foo.txt', 'r')
with open('foo.txt') as foo:
    read_data = foo.read()
read_data
foo.closed


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'r+') as bar:
    bar.write('A line of text\n')
    bar.write('A line of text\n')
    bar.write('A line of text\n')
    read_data_bar = bar.read()
read_data_bar
bar.closed