class Miasto:
    def __init__(self, nazwa, populacja):
        self.nazwa = nazwa
        self.populacja = populacja
    def __str__(self):
        return str(self.nazwa)+","+str(self.populacja)