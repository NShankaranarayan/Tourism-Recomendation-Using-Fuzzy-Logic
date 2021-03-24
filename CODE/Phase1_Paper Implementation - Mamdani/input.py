def init():
    Pric=input("Enter Pric [L/M/H]::")
    Dist=input("Enter Dist [L/M/H]::")
    Time=input("Enter Time [L/M/H]::")
    p=numbers_to_strings(Pric)
    d=numbers_to_strings(Dist)
    t=numbers_to_strings(Time)
    return (p,d,t)


def numbers_to_strings(argument):
    switcher = {
        "L": "LOW",
        "M": "MID",
        "H": "HIGH",
    }
    return switcher.get(argument)
