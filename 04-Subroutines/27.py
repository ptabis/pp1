txt = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
def czestotliwoscSamoglosek(txt):
    samogloski = ['e', 'y', 'u', 'i', 'o', 'a']
    wyrazy = txt.split(" ")
    c = 0
    for l in txt:
        if l in samogloski:
            c += 1
    return c/len(wyrazy)
print("W tekście występuje {} samogłosek na wyraz.".format(czestotliwoscSamoglosek(txt)))