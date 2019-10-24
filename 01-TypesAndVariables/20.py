import math

r = int(input("Podaj promień koła: "))
PI = math.pi

pole = PI*r*r
obw = 2*PI*r

print("Pole koła o promieniu {} wynosi {}.\nObwód koła o promieniu {} wynosi {}.".format(r, pole, r, obw))