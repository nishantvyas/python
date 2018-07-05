"""
write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""
import zlib

class compress():
    """
    base class to define compress methods
    """
    def __init__(self):
        """
        initialize any variables at the time of instance creation.
        """
        self.string = None

    def compress_zlib(self, string):
        """
        compress input string with zlib method
        :param string:
        :return string:
        """
        #encode the input sting
        self.string = string.encode()
        return zlib.compress(self.string)

    def decompress_zlib(self, string):
        """
        compress input string with zlib method
        :param string:
        :return string:
        """
        #encode the input string
        self.string = string
        return zlib.decompress(self.string).decode()


if __name__ == "__main__":
    """
    """
    string = "hello world!hello world!hello world!hello world!"
    compressObject1 = compress()
    compressed_string = compressObject1.compress_zlib(string)
    print(compressed_string)
    print(compressObject1.decompress_zlib(compressed_string))