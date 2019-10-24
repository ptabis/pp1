celsius = int(input("Podaj temperaturę w stopniach Celsiusa: "))
fahrenheit = (celsius * 1.8)+32
kelvin = celsius + 273.15
print("{} C = {} F\n{} C = {} K".format(celsius, fahrenheit, celsius, kelvin))