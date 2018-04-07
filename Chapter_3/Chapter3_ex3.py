try:
    score = float(input("You have just received your test back, what was your score out of 0 - 1.0? "))
except:
    print("That is not a valid float or integer.")
    exit()

if score >= 1.0:
    print("That is impossible, but good on you for having immense self belief!")
elif score >= 0.9:
    print("You received an A grade!")
elif score >= 0.8:
    print("You received an B grade!")
elif score >= 0.7:
    print("You received an C grade!")
elif score >= 0.6:
    print("You received an D grade!")
else:
    print("You received an F grade!")