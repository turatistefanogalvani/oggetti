class Rettangolo:
    def __init__(self, base, altezza, colore):
        self.base = base
        self.altezza = altezza
        self.colore = colore

    def area_rettangolo(self):
        return self.base * self.altezza

    def print_rettangolo(self):
        print(self.base)
        print(self.altezza)
        print(self.colore)
        