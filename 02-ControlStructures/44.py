limit = int(input("Podaj limit prędkośći (km/h): "))
speed = int(input("Podaj prędkość pojazdu (km/h): "))

delta_speed = speed - limit

if delta_speed <= 10:
    print("Mandat (zł): {}".format(delta_speed*5))
else:
    print("Mandat (zł): {}".format(50+(delta_speed-10)*15))
