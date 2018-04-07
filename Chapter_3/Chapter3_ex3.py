try:
    score = float(input("You have just received your test back that was given a mark between 0 - 1.0, what was your score? "))
except:
    print("That is not a valid float or integer.")
    exit()

if score >= 1.0:
    print("That is impossible, but good on you for having immense self belief!")
elif score >= 0.9:
    print("You received an A grade!")
elif score >= 0.8:
    print("You received a B grade!")
elif score >= 0.7:
    print("You received a C grade!")
elif score >= 0.6:
    print("You received a D grade!")
else:
    print("You received an F grade!")