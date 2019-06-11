import string
import random


class Generator:

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    def secure_password(self, length):
        return ''.join(random.SystemRandom().choice(self.alphabet) for _ in range(length))
