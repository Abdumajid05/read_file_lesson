#Rread file and convert to list
def read_file(f):
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    #return 0 

#Print list from file"""
    f=open(f)
    a = f.readline()
    b = a.split(',')
    l=[]
    for i in b:
        l.append(int(i))
    return l
    """l=[]
    for i in a:
        l.append(i)
    return l"""
print(read_file('data.txt'))