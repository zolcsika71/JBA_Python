class Date:

    def __init__(self, day, month):
        self.day = day
        self.month = month

    # use appropriate decorator
    @property
    def date(self):
        return self.day + '/' + self.month
