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

    with open(fileObj) as f:
        for line in f:
            file_in_buffer.append(line.strip())

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
        line_number = 1

        for lines in local_buffer:
            print(f"{line_number} " + lines)
            line_number += 1

        ##check with user if they'd like to edit file.
        edit = input("Do you want to edit the file (Y/N):")

        while True:
            ## circuit out if user wants to exit.
            if edit == "Y" or edit == "y":
                is_edit=True
            elif edit == "N" or edit == "n":
                print("Ok. Bye.")
                break
            else:
                print("Wrong selection, try again.")

            while is_edit:

                ##Enter line number to edit
                line_to_edit = int(input("Enter line number to edit:"))
                if line_to_edit > len(local_buffer) or line_to_edit < 1:
                    print("entered line number our of range")
                    is_edit = False
                else:
                    new_value = (f"Enter new data for line {line_number}:")
                    local_buffer[line_number-1] = new_value
                    print("Saving the file.")



    else:
        print ("Opening new file to write")
        print("*" * 50)
