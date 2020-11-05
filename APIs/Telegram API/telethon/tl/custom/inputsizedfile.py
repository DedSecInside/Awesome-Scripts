from ..types import InputFile


class InputSizedFile(InputFile):
    """InputFile class with two extra parameters: md5 (digest) and size"""
    def __init__(self, id_, parts, name, md5, size):
        """
        Initialize an md5 hash.

        Args:
            self: (todo): write your description
            id_: (int): write your description
            parts: (todo): write your description
            name: (str): write your description
            md5: (todo): write your description
            size: (int): write your description
        """
        super().__init__(id_, parts, name, md5.hexdigest())
        self.md5 = md5.digest()
        self.size = size
