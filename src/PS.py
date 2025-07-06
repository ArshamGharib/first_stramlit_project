import random
import string
from abc import ABC, abstractmethod


class PasswordGenereator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenereator):
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self) -> str:
        return ''.join([random.choice(string.digits)
                        for _ in range(self.length)])


class RandomPassword(PasswordGenereator):
    def __init__(self, length: int = 4, include_numbers: bool = False,
                 include_symbols: bool = False):
        self.length = length
        self.char = string.ascii_letters
        if include_numbers:
            self.char += string.digits
        if include_symbols:
            self.char += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.char) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenereator):
    def __init__(
                self,
                number_of_words: int = 4,
                seprator: str = '-',
                cap: bool = False,
                vocab: list = None
    ):
        if vocab is None:
            vocab = ["lantern", "breeze", "mosaic", "clutch", "orbit",
                     "thistle", "gravel", "whistle", "drift", "velvet"]
        self.vocab = vocab
        self.number_of_words = number_of_words
        self.seprator = seprator
        self.cap = cap

    def generate(self):
        password = [random.choice(self.vocab)
                    for _ in range(self.number_of_words)]
        if self.cap:
            password = [word.upper() if random.choice([True, False])
                        else word.lower()
                        for word in password]
        return self.seprator.join(password)


if __name__ == '__main__':
    obj = RandomPassword()
    print(obj.generate())
