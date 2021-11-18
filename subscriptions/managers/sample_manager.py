import random


class SampleManager:
    @classmethod
    def list(cls, start, end, size):
        return random.sample(range(start, end), size)
