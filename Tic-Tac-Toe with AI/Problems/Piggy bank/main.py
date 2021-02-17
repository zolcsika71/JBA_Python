class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        cents_ = self.cents + deposit_cents
        if cents_ > 99:
            self.dollars += cents_ // 100
            self.cents = cents_ % 100
        else:
            self.cents = cents_


