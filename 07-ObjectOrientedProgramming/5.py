class Piosenka():
    def __init__(self, wykonawca, utwor, album, rok):
        self.wykonawca = wykonawca
        self.utwor = utwor
        self.album = album
        self.rok = rok
    def __str__(self):
        return """
Wykonawca: {}
Utwór: {}
Album: {}
Rok: {}
                """.format(self.wykonawca, self.utwor, self.album, self.rok)
p = Piosenka("a", "b", "c", 2019)
print(p)