import string

from seedrandom import SeededRNG


class Generator:
    def __init__(self, source: bytes, salt: bytes):
        self._source = source
        self._salt = salt

        self._alphabet = ""
        self.set_rules()

    def set_rules(self, digits: bool = True, lowercase: bool = True, uppercase: bool = True, symbols: bool = False):
        alphabet = ""

        if digits:
            alphabet += string.digits
        if lowercase:
            alphabet += string.ascii_lowercase
        if uppercase:
            alphabet += string.ascii_uppercase
        if symbols:
            alphabet += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        self._alphabet = "".join(sorted(alphabet))

    def generate(self, length: int) -> str:
        if length <= 0:
            raise ValueError("Length must be > 0")

        string = ""
        for char_pos in range(length):
            if len(self._salt) > 0:
                salt = [self._salt]
            else:
                salt = []

            # Generate random index for each position and fetch char from alphabet
            rng = SeededRNG(self._source,
                            *salt,
                            self._alphabet.encode("utf-8"),
                            bytes([length]),
                            bytes([char_pos]))  # hashlib.md5 by default

            random_i = rng.randint(a=0, b=len(self._alphabet) - 1)
            string += self._alphabet[random_i]

        return string
