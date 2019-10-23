pin = "0805"
counter = 0
while True:
    if counter == 3:
        print("Karta płatnicza zostaje zablokowana")
        break
    user_pin = input("Podaj PIN: ")
    if user_pin == pin:
        print("PIN poprawny")
        break
    else:
        print("Kod PIN niepoprawny")
        counter += 1