txt = input("Podaj tekst: ")
txt_l = len(txt)
for l in range(0, txt_l):
    print(txt[txt_l-l-1], end="")