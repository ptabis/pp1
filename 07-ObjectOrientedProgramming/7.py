class Student():
    album = 1000
    uczelnia = "UEK Kraków"
    def __init__(self, imie, nazwisko, kierunek):
        Student.album += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albumu = Student.album
        self.kierunek = kierunek
    def __str__(self):
        return f"{self.imie} {self.nazwisko.upper()} ({self.nr_albumu}), {self.kierunek}, {Student.uczelnia}"

s1 = Student("Wacław", "Potocki", "Informatyka")
s2 = Student("Robert", "Konrad", "Informatyka")
s3 = Student("Albert", "Chłop", "Ekonomia")
print(s1)
print(s2)
print(s3)