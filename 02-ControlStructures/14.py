age = int(input("Podaj wiek psa w ludzkich latach: "))
if age < 2:
    print("Wiek psa wynosi: {} lata".format(age*10.5))
else:
    print("Wiek psa wynosi: {} lata".format((age-2)*4+21))