celcius_temperature = int(input("What is the temperature in degrees celcius at the moment? "))
farenheit_temperature = (celcius_temperature) * 1.8 + 32
if celcius_temperature <= 0:
    print("Wow, that is cold! {} degrees farenheit - you should grab a jacket!".format(farenheit_temperature))
elif (celcius_temperature > 0) & (celcius_temperature < 30):
    print("{} farenheit...acceptable weather!".format(farenheit_temperature))
else:
    print("{} farenheit!?!? Madness! Get into the shade!!".format(farenheit_temperature))