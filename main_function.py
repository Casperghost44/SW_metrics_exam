from math import hypot

def custom_hypot(parendicular, base):
    if (not isinstance(parendicular, int) or not isinstance(base, int)):
        if(not isinstance(parendicular, float) and not isinstance(base, float)):
            raise TypeError(f"{parendicular} or {base} is not valid input")
    if(base >= 0 and parendicular >= 0):
        return hypot(base, parendicular)
    raise TypeError("Invalid range")

