class Puppy:
    n_puppies = 0

    def __new__(cls):
        if 0 <= cls.n_puppies < 10:
            cls.n_puppies += 1
