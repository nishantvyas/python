#!/anaconda3/bin/python
# coding: utf-8

"""
Copy address from clipboard or command line argument and open google map to map it.
"""

import webbrowser, sys, pyperclip
if __name__ == "__main__":
    """
    """
    if len(sys.argv) > 1:
        # check if command line argument had anything
        address = ' '.join(sys.argv[1:])
    else:
        #get it from clipboard
        address = pyperclip.paste()

    ##open the google maps URL
    ##https://www.google.com/maps/place/<ADDRESS>
    url = "https://www.google.com/maps/place/" + address
    webbrowser.open(url)