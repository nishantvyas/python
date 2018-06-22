"""
Text Editor - Notepad style application that can open, edit, and save text documents.
"""

from pathlib import Path

def readInLine(fileObj):
    """

    :param fileObj:
    :return:
    """

    file_in_buffer = []
    line_number = 1

    with open(fileObj) as f:
        for line in f:
            file_in_buffer.append(f"{line_number} " + line.strip())
            line_number += 1

    return file_in_buffer

if __name__ == "__main__":
    """
    """

    filename = input("Enter file name to open:")

    ### pathlib.path.is_file checks if file exists

    if Path(filename).is_file():
        print("Content of the file")
        print("*" * 50)
        local_buffer = readInLine(filename)
        for lines in local_buffer:
            print(lines)
    else:
        print ("Opening new file to write")
        print("*" * 50)
