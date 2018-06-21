"""
Different methods of reading file.
"""
def readInChunks(fileObj, chunkSize=2048):
    """
    fine-grained control over how much to read in each iteration.
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.
    ***Note*** with this method one explicitly needs close the file at the end.

    :param fileObj:
    :param chunkSize:
    :return:
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

def readInLines(fileObj):
    """
    "with" is the nice and efficient pythonic way to read large files.
    Internally it does buffered IO (to optimized on costly IO operations) and memory management.
    1) file object is automatically closed after exiting from with execution block.
    2) exception handling inside the with block.
    3) memory for loop iterates through the f file object line by line.
    :param fileObj:
    :return:
    """
    with open(fileObj) as f:
        for data in f:
            yield data

if __name__ == "__main__":

    filename = 'textfile.txt'

    ### reading one line at a time using with
    for line in readInLines(filename):
        print(line.strip())

    print()
    
    ### reading by chunk
    f = open(filename)
    for chunk in readInChunks(f):
        print(chunk)
    f.close()

