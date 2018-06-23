"""
Text Editor - Notepad style application that can open, edit, and save text documents.
"""

from pathlib import Path
import os


def readInLine(fileObj):
    """

    :param fileObj:
    :return:
    """

    file_in_buffer = []

    with open(fileObj) as f:
        for line in f:
            file_in_buffer.append(line.strip())

    return file_in_buffer

def writeToFile(fileObj, listObj):
    """

    :param fileObj:
    :param listObj:
    :return:
    """

    f = open(fileObj,'w')

    for line in listObj:
        f.write(line)
        f.write("\n")


if __name__ == "__main__":
    """
    """

    filename = input("Enter file name to open:")

    ### pathlib.path.is_file checks if file exists

    if Path(filename).is_file():

        print("Content of the file")
        print("*" * 50)

        local_buffer = readInLine(filename)
        line_number = 1

        for lines in local_buffer:
            print(f"{line_number} " + lines)
            line_number += 1

        while True:

            ##check with user if they'd like to edit file.
            edit = input("Do you want to edit the file (Y/N):")

            ## circuit out if user wants to exit.
            if edit == "Y" or edit == "y":
                is_edit=True
            elif edit == "N" or edit == "n":
                print("Ok. Bye.")
                is_edit=False
                break
            else:
                print("Wrong selection, try again.")
                is_edit = False

            while is_edit:

                ##Enter line number to edit
                line_to_edit = int(input("Enter line number to edit:"))

                if line_to_edit > len(local_buffer) or line_to_edit < 1:
                    print("entered line number out of range")
                else:
                    new_value = input(f"Enter new data for line {line_to_edit}:")
                    local_buffer[line_to_edit-1] = new_value
                    writeToFile(filename,local_buffer)
                    print("Saving the file.")

                    ###os.system("clear")

                    i=1
                    for lines in local_buffer:
                        print(f"{i} " + lines)
                        i += 1

                    print("Content of the file")
                    print("*" * 50)

                is_edit = False

    else:
        print ("Opening new file to write")
        print("*" * 50)
