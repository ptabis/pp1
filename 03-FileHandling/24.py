tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
header = 'Imie,Nazwisko,Email\n'
with open('dane.csv', 'w') as f:
    f.write(header)
    for user in tab:
        f.write(user[0]+','+user[1]+','+user[2]+'\n')