student = 'Mateusz'
stypendium = 950
wydatki = 920

assert type(student) == str, "Student == tekst"
assert type(stypendium) == int, "Stypendium == liczba"
assert type(wydatki) == int, "Wydatki == liczba"
assert wydatki < stypendium, "Wy < st"
print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))